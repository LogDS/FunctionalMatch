
from dataclasses import dataclass
from typing import Union

from FunctionalMatch.Match import Match
from FunctionalMatch.ReturningFirstObjects import FromJSONPath, FromVariable, Invent


@dataclass(frozen=True, eq=True, order=True)
class Query:
    select: Match
    as_: Union[Invent, FromVariable, FromJSONPath]

    def __call__(self, obj):
        test, outcome_list = self.select(obj)
        if not test:
            return test, []  # Rationale: no outcome is available, if the test is false
        results = []
        for dct in outcome_list:
            result = self.as_(dct)
            if result is not None:
                results.append(result.obj)
        return True, results

