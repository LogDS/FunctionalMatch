from dataclasses import dataclass, is_dataclass, fields
from types import MappingProxyType


@dataclass(frozen=True, eq=True, order=True)
class Variable:
    name: str

@dataclass(frozen=True, eq=True, order=True)
class Ignore:
    pass

ignore_instance = Ignore()

def var(x):
    if x == "$":
        raise TypeError("$ is not a valid variable name")
    return Variable(x)


@dataclass(frozen=True, eq=True, order=True)
class JSONPath:
    expression: str


def _structural_match(query:object, target:object, match_result):
    if type(query).__name__ == "Ignore":
        return match_result
    if type(query).__name__ == "Variable":
        match_result[query.name] = target
        return match_result
    elif type(query).__name__ == "tuple":
        if not query[0] == type(target).__name__:
            return None
        from FunctionalMatch.utils import FrozenDict
        assert isinstance(query[1], FrozenDict)
        for k, v in query[1].items():
            if not hasattr(target, k):
                return None
            match_result = _structural_match(v, getattr(target, k), match_result)
        return match_result
    elif is_dataclass(query):
        if not type(target).__name__ == type(query).__name__:
            return None
        for field in fields(target):
            match_result = _structural_match(getattr(query, field.name), getattr(target, field.name), match_result)
            if match_result is None:
                return match_result
        return match_result
    else:
        if query == target:
            return match_result
        else:
            return None


def equi_join_dictionaries(ls):
    if len(ls) <= 1:
        return ls
    else:
        left = ls[0]
        right = ls[1]
        tmp = []
        for left_dict in left:
            for right_dict in right:
                if all(map(lambda y: left_dict[y] == right_dict[y], set(left_dict.keys()).intersection(right_dict.keys()))):
                    tmp.append(left_dict.update(right_dict))
        if len(tmp) == 0:
            return tmp
        ls.insert(0, tmp)
        return equi_join_dictionaries(ls)


def structural_match(query:object, target:object, doNested=False, condition=None, extension_match_function_list=None):
    outcome = []
    result = _structural_match(query, target, dict())
    if result is not None:
        result["$"] = target
        outcome.append(result)
    if doNested:
        for k, x in result.items():
            if k != "$":
                do_extend, dd = structural_match(query, x, True)
                if do_extend:
                    outcome += dd
    if (extension_match_function_list is not None) and (isinstance(extension_match_function_list, list) or isinstance(extension_match_function_list, tuple)) and all(map(callable, extension_match_function_list)) and len(extension_match_function_list)>0:
        tmp = []
        for x in outcome:
            extension = [extension_match_function(x) for extension_match_function in extension_match_function_list]
            extension.insert(0, x)
            tmp.extend(equi_join_dictionaries(extension))
        outcome = tmp
    if condition is not None:
        from FunctionalMatch.functions.Where import where
        return where(outcome, condition)
    else:
        return len(outcome)>0, outcome
