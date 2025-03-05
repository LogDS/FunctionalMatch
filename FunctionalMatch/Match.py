__author__ = "Giacomo Bergami"
__copyright__ = "Copyright 2025, Functional Match"
__credits__ = ["Giacomo Bergami"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Giacomo Bergami"
__email__ = "bergamigiacomo@gmail.com"
__status__ = "Production"

# from collections import defaultdict
from dataclasses import dataclass
from typing import Optional, List
# from FunctionalMatch import structural_match
from FunctionalMatch.PropositionalLogic import Prop
from FunctionalMatch.TransformationResults import ReplaceWith
from FunctionalMatch.utils import FrozenDict


@dataclass(eq=True, order=True, frozen=True)
class ExternalMatchByExtesion:
    function_name: str
    module: str

    def __call__(self, x):
        import importlib
        mod = importlib.import_module(self.module) #__import__(self.module)
        func = getattr(mod, self.function_name)
        return func(x)

@dataclass(eq=True, order=True, frozen=True)
class Match:
    query: list
    nested: bool
    where: Optional[Prop]
    extension: List[ExternalMatchByExtesion]
    replacement: ReplaceWith

    def structural_match_single_query(self, query, target, number="0"):
        outcome = []
        from FunctionalMatch.functions.structural_match import _structural_match
        result = _structural_match(query, target, dict())
        current = f"${number}"
        if result is not None:
            result[current] = target
            outcome.append(result)
        if self.nested and (result is not None):
            for k, x in result.items():
                if k != current:
                    do_extend, dd = self.structural_match(x, query, f"{number}/{k}") ## TODO: revise recursive call after update
                    if do_extend and len(dd) > 0:
                        outcome += dd
        return outcome

    def structural_match(self, query, target, number):
        outcome = self.structural_match_single_query(query, target, number)
        if self.where is not None:
            from FunctionalMatch.functions.Where import where
            test, outcome = where(outcome, self.where)
        else:
            test = len(outcome) > 0
        return test, outcome

    def structural_match_main_loop(self, targets):
        results = dict()
        for entry_idx, x in enumerate(targets):
            for query_idx, q in enumerate(self.query):
                test, outcome = self.structural_match(q, x, str(query_idx))
                if test:
                    if query_idx not in results:
                        results[query_idx] = list() #dict()
                    # if entry_idx not in results[query_idx]:
                    #     results[query_idx][entry_idx] = list()
                    if len(outcome) > 0:
                        results[query_idx].extend(outcome) #[entry_idx]

        ## All the queries should have at least one match. If this does not happen, then no sensible result can be obtained
        if len(results) != len(self.query):
            return False, []

        ## The actual equijoin boils down to equi-join over the values, so to derive different possible matches
        from FunctionalMatch.functions.structural_match import equi_join_dictionaries
        outcome = equi_join_dictionaries(list(results.values()))

        if (self.extension is not None) and (
                isinstance(self.extension , list) or isinstance(self.extension ,
                                                                              tuple)) and all(
                map(callable, self.extension )) and len(self.extension ) > 0:
            tmp = []
            for x in outcome:
                for extension_match_function in self.extension:
                    x = extension_match_function(x if isinstance(x, FrozenDict) else FrozenDict.from_dictionary(x))
                tmp.append(x)
            outcome = tmp
        if self.where is not None:
            from FunctionalMatch.functions.Where import where
            test, outcome = where(outcome, self.where)
        else:
            test = len(outcome) > 0
        if test:
            if self.replacement is None:
                return test, outcome
            else:
                outcome = [self.replacement(obj) for obj in outcome]
        return test, outcome

    # def deprecated_structural_match(self, target: object, Q=None, start_number=""):
    #     if Q is None:
    #         Q = self.query
    #     if isinstance(Q, list):
    #         outcome = [self.structural_match_single_query(query, target, f"{start_number}/{number}" if len(start_number)>0 else f"{number}") for number, query in enumerate(Q)]
    #         from FunctionalMatch.functions.structural_match import equi_join_dictionaries
    #         outcome = equi_join_dictionaries(outcome)
    #     else:
    #         outcome = self.structural_match_single_query(Q, target)
    #     if (self.extension is not None) and (
    #             isinstance(self.extension , list) or isinstance(self.extension ,
    #                                                                           tuple)) and all(
    #             map(callable, self.extension )) and len(self.extension ) > 0:
    #         tmp = []
    #         for x in outcome:
    #             for extension_match_function in self.extension:
    #                 x = extension_match_function(x if isinstance(x, FrozenDict) else FrozenDict.from_dictionary(x))
    #             tmp.append(x)
    #         outcome = tmp
    #     if self.where is not None:
    #         from FunctionalMatch.functions.Where import where
    #         test, outcome = where(outcome, self.where)
    #     else:
    #         test = len(outcome) > 0
    #     if test:
    #         if self.replacement is None:
    #             return test, outcome
    #         else:
    #             outcome = [self.replacement(obj) for obj in outcome]
    #     return test, outcome

    def __call__(self, x):
        if isinstance(x, list) or isinstance(x, tuple) or isinstance(x, set):
            return self.structural_match_main_loop(x)
        elif isinstance(x, dict):
            raise RuntimeError("Unsupported structure match (dict)")
        else:
            return self.structural_match_main_loop([x])


