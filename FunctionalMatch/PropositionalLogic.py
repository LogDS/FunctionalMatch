__author__ = "Giacomo Bergami"
__copyright__ = "Copyright 2025, Functional Match"
__credits__ = ["Giacomo Bergami"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Giacomo Bergami"
__email__ = "bergamigiacomo@gmail.com"
__status__ = "Production"

from collections import defaultdict
from dataclasses import dataclass, is_dataclass, asdict
from typing import Union

import dacite

from FunctionalMatch.utils import FrozenDict

def var_interpret(obj, kwargs:dict|FrozenDict, keepList=False):
    from FunctionalMatch import JSONPath
    from FunctionalMatch.functions.structural_match import Variable
    from jsonpath_ng import jsonpath, parse
    if isinstance(obj, Variable):
        return kwargs.get(obj.name, None)
    elif isinstance(obj, JSONPath):
        val = obj.expression.find(':')
        if val == -1:
            if obj.expression.startswith('$'):
                pathing_over_expr = obj.expression
                pathing_object = kwargs.get("$", None)
            else:
                return kwargs.get(obj.expression, None)
        else:
            pathing_over_expr = obj.expression[val+1:]
            pathing_object = kwargs.get(obj.expression[:val], None)
        if pathing_object is not None and is_dataclass(pathing_object):
                jsonpath_expr = parse(pathing_over_expr)
                L = [match.value for match in jsonpath_expr.find(asdict(pathing_object))]
                return L[0] if (not keepList) and (len(L) == 1) else L
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
            if obj.expression.startswith('$'):
                pathing_var = "$"
                pathing_over_expr = obj.expression
                pathing_object = kwargs.get("$", None)
            else:
                pathing_var = obj.expression
                return kwargs.get(obj.expression, None)
        else:
            pathing_var = obj.expression[:val]
            pathing_over_expr = obj.expression[val+1:]
            pathing_object = kwargs.get(obj.expression[:val], None)
        if pathing_object is not None and is_dataclass(pathing_object):
                jsonpath_expr = parse(pathing_over_expr)
                name_object = type(pathing_object)
                result_dct = jsonpath_expr.update(asdict(pathing_object), value)
                result_obj = dacite.from_dict(name_object, result_dct)
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
        right = var_interpret(self.right, kwargs)
        return left == right

@dataclass(frozen=True, eq=True, order=True)
class NEq:
    left: object
    right: object

    def interpretation(self, kwargs):
        left = var_interpret(self.left, kwargs)
        right = var_interpret(self.right, kwargs)
        return left == right

@dataclass(frozen=True, eq=True, order=True)
class LEq:
    left: object
    right: object

    def interpretation(self, kwargs):
        left = var_interpret(self.left, kwargs)
        right = var_interpret(self.right, kwargs)
        return left <= right

@dataclass(frozen=True, eq=True, order=True)
class GEq:
    left: object
    right: object

    def interpretation(self, kwargs):
        left = var_interpret(self.left, kwargs)
        right = var_interpret(self.right, kwargs)
        return left >= right

@dataclass(frozen=True, eq=True, order=True)
class LT:
    left: object
    right: object

    def interpretation(self, kwargs):
        left = var_interpret(self.left, kwargs)
        right = var_interpret(self.right, kwargs)
        return left < right

@dataclass(frozen=True, eq=True, order=True)
class GT:
    left: object
    right: object

    def interpretation(self, kwargs):
        left = var_interpret(self.left, kwargs)
        right = var_interpret(self.right, kwargs)
        return left < right

@dataclass(frozen=True, eq=True, order=True)
class IsIn:
    left: object
    right: object

    def interpretation(self, kwargs):
        left = var_interpret(self.left, kwargs)
        right = var_interpret(self.right, kwargs)
        return left in right

@dataclass(frozen=True, eq=True, order=True)
class Empty:
    left: object

    def interpretation(self, kwargs):
        left = var_interpret(self.left, kwargs)
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

    def __call__(self, x):
        import importlib
        mod = importlib.import_module(self.module) #__import__(self.module)
        func = getattr(mod, self.function_name)
        return func(x)

Prop = Union[And, Or, Impl, Not, Eq, NEq, LEq, GEq, LT, GT, IsIn, Empty, ExternalPredicateByExtesion]