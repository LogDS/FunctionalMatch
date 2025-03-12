__author__ = "Giacomo Bergami"
__copyright__ = "Copyright 2025, Functional Match"
__credits__ = ["Giacomo Bergami"]
__license__ = "GPLv3"
__version__ = "2.0"
__maintainer__ = "Giacomo Bergami"
__email__ = "bergamigiacomo@gmail.com"
__status__ = "Production"

from collections import defaultdict
from dataclasses import dataclass, is_dataclass, asdict, fields
from typing import Union, Optional

import dacite

from FunctionalMatch.utils import FrozenDict

def navigate_dataclass(obj, jsonpath_expr):
    from jsonpath_ng import Root, Child, Fields, Index
    if isinstance(jsonpath_expr, Root):
        return obj
    if isinstance(jsonpath_expr, Child):
        return navigate_dataclass(navigate_dataclass(obj, jsonpath_expr.left), jsonpath_expr.right)
    if isinstance(jsonpath_expr, Fields):
        L = []
        allFields = False
        for field in jsonpath_expr.fields:
            if field == "*":
                allFields = True
                L.extend([getattr(obj, field.name) for field in  fields(obj)])
            else:
                if hasattr(obj, field):
                    L.append(getattr(obj, field))
        if (not allFields) and len(L) == 1:
            return L[0]
        else:
            return L
    elif isinstance(jsonpath_expr, Index):
        return obj[jsonpath_expr.index]

def jpath_interpret(obj, path):
    if (path == "$"):
        return obj
    from jsonpath_ng import jsonpath, parse
    jsonpath_expr = parse(path)
    L = [match.value for match in jsonpath_expr.find(asdict(obj))]
    assert len(L)==1
    L0_type = type(navigate_dataclass(obj, jsonpath_expr))
    if is_dataclass(L0_type):
        return dacite.from_dict(L0_type, L[0])
    return L[0]

def jpath_update(obj, path, value):
    from jsonpath_ng import jsonpath, parse
    jsonpath_expr = parse(path)
    name_object = type(obj)
    result_dct = jsonpath_expr.update(asdict(obj), value)
    if (name_object != type(result_dct)) and ((not is_dataclass(obj)) or isinstance(result_dct, dict)):
        assert isinstance(result_dct, dict)
        result_obj = dacite.from_dict(name_object, result_dct)
    else:
        result_obj = result_dct
    return result_obj

def var_interpret(obj, kwargs:dict|FrozenDict):
    from FunctionalMatch import JSONPath
    from FunctionalMatch.functions.structural_match import Variable
    from jsonpath_ng import jsonpath, parse
    if isinstance(obj, Variable):
        return kwargs.get(obj.name, None)
    elif isinstance(obj, JSONPath):
        val = obj.expression.find(':')
        if val == -1:
            raise RuntimeError("ERROR: the var update has tp be set in the following way: <var>:json_expression")
            # if obj.expression.startswith('$'):
            #     pathing_over_expr = obj.expression
            #     pathing_object = kwargs.get("$", None)
            # else:
            #     return kwargs.get(obj.expression, None)
        else:
            pathing_over_expr = obj.expression[val+1:]
            pathing_object = kwargs.get(obj.expression[:val], None)
        if pathing_object is not None and is_dataclass(pathing_object):
                jsonpath_expr = parse(pathing_over_expr)
                L = [match.value for match in jsonpath_expr.find(asdict(pathing_object))]
                return navigate_dataclass(pathing_object, jsonpath_expr)
                # return L[0] if (not keepList) and (len(L) == 1) else L
        else:
            return None
    else:
        return obj

def var_update(value, obj, kwargs:FrozenDict):
    from FunctionalMatch import JSONPath
    from FunctionalMatch.functions.structural_match import Variable
    if isinstance(kwargs, dict):
        kwargs = FrozenDict.from_dictionary(kwargs)
    from jsonpath_ng import jsonpath, parse
    if isinstance(obj, Variable):
        return kwargs.update(obj.name, value)
    elif isinstance(obj, JSONPath):
        val = obj.expression.find(':')
        pathing_var = None
        if val == -1:
            raise RuntimeError("ERROR: the var update has tp be set in the following way: <var>:json_expression")
            # if obj.expression.startswith('$'):
            #     pathing_var = "$"
            #     pathing_over_expr = obj.expression
            #     pathing_object = kwargs.get("$", None)
            # else:
            #     pathing_var = obj.expression
            #     return kwargs.get(obj.expression, None)
        else:
            pathing_var = obj.expression[:val]
            pathing_over_expr = obj.expression[val+1:]
            pathing_object = kwargs.get(obj.expression[:val], None)
        if pathing_object is not None and is_dataclass(pathing_object):
                jsonpath_expr = parse(pathing_over_expr)
                name_object = type(pathing_object)
                result_dct = jsonpath_expr.update(asdict(pathing_object), value)
                if (name_object != type(result_dct)) and ((not is_dataclass(pathing_object)) or (isinstance(result_dct, dict))):
                    result_obj = dacite.from_dict(name_object, result_dct)
                else:
                    result_obj = result_dct
                return kwargs.update(pathing_var, result_obj)
        else:
            return kwargs
    else:
        return kwargs




@dataclass(frozen=True, eq=True, order=True)
class Eq:
    left: object
    right: object

    def interpretation(self, kwargs):
        left = var_interpret(self.left, kwargs)
        if left is None:
            return True
        right = var_interpret(self.right, kwargs)
        if right is None:
            return True
        return left == right

@dataclass(frozen=True, eq=True, order=True)
class NEq:
    left: object
    right: object

    def interpretation(self, kwargs):
        left = var_interpret(self.left, kwargs)
        if left is None:
            return True
        right = var_interpret(self.right, kwargs)
        if right is None:
            return True
        return left == right

@dataclass(frozen=True, eq=True, order=True)
class LEq:
    left: object
    right: object

    def interpretation(self, kwargs):
        left = var_interpret(self.left, kwargs)
        if left is None:
            return True
        right = var_interpret(self.right, kwargs)
        if right is None:
            return True
        return left <= right

@dataclass(frozen=True, eq=True, order=True)
class GEq:
    left: object
    right: object

    def interpretation(self, kwargs):
        left = var_interpret(self.left, kwargs)
        if left is None:
            return True
        right = var_interpret(self.right, kwargs)
        if right is None:
            return True
        return left >= right

@dataclass(frozen=True, eq=True, order=True)
class LT:
    left: object
    right: object

    def interpretation(self, kwargs):
        left = var_interpret(self.left, kwargs)
        if left is None:
            return True
        right = var_interpret(self.right, kwargs)
        if right is None:
            return True
        return left < right

@dataclass(frozen=True, eq=True, order=True)
class GT:
    left: object
    right: object

    def interpretation(self, kwargs):
        left = var_interpret(self.left, kwargs)
        if left is None:
            return True
        right = var_interpret(self.right, kwargs)
        if right is None:
            return True
        return left < right

@dataclass(frozen=True, eq=True, order=True)
class IsIn:
    left: object
    right: object

    def interpretation(self, kwargs):
        left = var_interpret(self.left, kwargs)
        if left is None:
            return True
        right = var_interpret(self.right, kwargs)
        if right is None:
            return True
        return left in right

@dataclass(frozen=True, eq=True, order=True)
class Empty:
    left: object

    def interpretation(self, kwargs):
        left = var_interpret(self.left, kwargs)
        if left is None:
            return True
        if isinstance(left, list) or isinstance(left, tuple) or isinstance(left, dict) or isinstance(left, defaultdict):
            return len(left) == 0
        return False

atom = Union[Eq, NEq, LEq, GEq, LT, GT, IsIn, Empty]

@dataclass(frozen=True, eq=True, order=True)
class And:
    left: 'Prop'
    right: 'Prop'

    def interpretation(self, kwargs):
        if not self.left.interpretation(kwargs):
            return False
        return self.right.interpretation(kwargs)


@dataclass(frozen=True, eq=True, order=True)
class Or:
    left: 'Prop'
    right: 'Prop'

    def interpretation(self, kwargs):
        if self.left.interpretation(kwargs):
            return True
        return self.right.interpretation(kwargs)

@dataclass(frozen=True, eq=True, order=True)
class Impl:
    left: 'Prop'
    right: 'Prop'

    def interpretation(self, kwargs):
        if not self.left.interpretation(kwargs):
            return True
        return self.right.interpretation(kwargs)

@dataclass(frozen=True, eq=True, order=True)
class Not:
    left: 'Prop'

    def interpretation(self, kwargs):
        return not self.left.interpretation(kwargs)

@dataclass(eq=True, order=True, frozen=True)
class ExternalPredicateByExtesion:
    module: str
    function_name: str
    extra_args: Optional[FrozenDict] = None

    def __call__(self, x):
        import importlib
        mod = importlib.import_module(self.module) #__import__(self.module)
        func = getattr(mod, self.function_name)
        assert isinstance(x, dict) or isinstance(x, FrozenDict)
        d = dict()
        for k, v in x.items():
            d[k] = v
        if self.extra_args is not None:
            for k, v in self.extra_args.items():
                d[k] = v
        return func(FrozenDict.from_dictionary(d))

    def interpretation(self, kwargs):
        return self.__call__(kwargs)


Prop = Union[And, Or, Impl, Not, Eq, NEq, LEq, GEq, LT, GT, IsIn, Empty, ExternalPredicateByExtesion]