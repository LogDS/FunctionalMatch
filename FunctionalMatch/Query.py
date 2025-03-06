__author__ = "Giacomo Bergami"
__copyright__ = "Copyright 2025, Functional Match"
__credits__ = ["Giacomo Bergami"]
__license__ = "GPLv3"
__version__ = "2.0"
__maintainer__ = "Giacomo Bergami"
__email__ = "bergamigiacomo@gmail.com"
__status__ = "Production"

from collections import defaultdict
from dataclasses import dataclass
from typing import Union

from FunctionalMatch.Match import Match
from FunctionalMatch.ReturningFirstObjects import FromJSONPath, FromVariable, Invent
from FunctionalMatch.functions.Reference import Reference


@dataclass(frozen=True, eq=True, order=True)
class Query:
    select: Match
    as_: Union[Invent, FromVariable, FromJSONPath]

    def __call__(self, obj):
        assert isinstance(obj, list) or isinstance(obj, tuple) or isinstance(obj, set)
        obj = list(obj)
        obj_dict = dict()
        for x in obj:
            from FunctionalMatch.utils import ObjDepthDeterminer
            obj_dict[x] = ObjDepthDeterminer.get_depth_dictionary(x)

        test, outcome_list = self.select(obj)
        if not test:
            return test, []  # Rationale: no outcome is available, if the test is false
        results = []

        ## Grouping the outcome list by root objects
        q = self.select.matching_obj_vars
        grouped_results = defaultdict(list)
        for dct in outcome_list:
            ls = []
            for x in q:
                assert x in dct
                curr_obj = dct[x]
                curr = Reference.from_object(curr_obj)
                found = False
                for root, result in obj_dict.items():
                    if curr in result.root_to_ancestors_ref or curr_obj in result.root_to_ancestors:
                        ls.append(root)
                        found = True
                        break
                assert found
            assert len(ls) == len(q)
            grouped_results[tuple(ls)].append(dct)

        for dct in outcome_list:
            result = self.as_(dct)
            if result is not None:
                results.append(result.obj)
        return True, results

