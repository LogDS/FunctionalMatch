from dataclasses import dataclass, is_dataclass, fields

from dacite import from_dict

from FunctionalMatch import JSONPath
from FunctionalMatch.ReturningFirstObjects import MatchedObjects
from FunctionalMatch.functions.Reference import Reference
from FunctionalMatch.functions.structural_match import Variable
from FunctionalMatch.utils import FrozenDict

def replace_with(obj, d: dict):
    ref = Reference.from_object(obj)
    if ref in d:
        obj = d[ref]
    elif obj in d:
        obj = d[obj]
    elif is_dataclass(obj):
        obj_inst = dict()
        for field in fields(obj):
            obj_inst[field.name] = replace_with(getattr(obj, field.name), d)
        return from_dict(type(obj), obj_inst)
    if isinstance(obj, Reference):
        return obj.get()
    else:
        return obj


@dataclass(frozen=True, order=True, eq=True)
class ReplaceWith:
    replacement: FrozenDict

    def __call__(self, obj: MatchedObjects) -> MatchedObjects:
        replaced_dict = dict()
        for k, v in self.replacement.items():
            if isinstance(k, Variable) and k in obj.variables:
                k = Reference.from_object(obj.variables[k.name])
            if isinstance(v, Variable) and v in obj.variables:
                v = Reference.from_object(obj.variables[k.name])
            replaced_dict[k] = v
        return MatchedObjects(replace_with(obj.obj, replaced_dict), obj.variables)


@dataclass(frozen=True, order=True, eq=True)
class UpdateWith:
    """
    Updates a match (:jsonpath) with either a value or some transformation function (value)
    """
    jsonpath: str
    value: object

    def __call__(self, obj: MatchedObjects) -> MatchedObjects:
        assert obj.variables["^"] == obj
        from FunctionalMatch.PropositionalLogic import var_interpret
        l = var_interpret(JSONPath(self.jsonpath), obj.variables, True)
        if len(l) == 0:
            return obj
        dd = dict()
        for x in l:
            if callable(self.value):
                dd[x] = self.value(x)
            else:
                dd[x] = self.value
        return ReplaceWith(**dd)(obj)