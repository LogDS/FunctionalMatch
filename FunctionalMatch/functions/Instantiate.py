__author__ = "Giacomo Bergami"
__copyright__ = "Copyright 2025, Functional Match"
__credits__ = ["Giacomo Bergami"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Giacomo Bergami"
__email__ = "bergamigiacomo@gmail.com"
__status__ = "Production"


from dataclasses import is_dataclass, fields, dataclass
from dacite import from_dict
# from FunctionalMatch.utils import FrozenDict

def replaceWith(query:object, replacement_map, value_map):
    raise RuntimeError("Not implemented")
    # for key, value in replacement_map.items():
    #     from FunctionalMatch.PropositionalLogic import var_interpret
    #     result = var_interpret(key, value_map)
    #     if result is not None:
    #         if isinstance(result, list):
    #             for x in result:


def instantiate(query:object, kwargs):
    if type(query).__name__ == "Variable":
        return kwargs.get(query.name, None)
    elif is_dataclass(query):
        obj_inst = dict()
        for field in fields(query):
            obj_inst[field.name] = instantiate(getattr(query, field.name), kwargs)
        return from_dict(type(query), obj_inst)
    else:
        return query

