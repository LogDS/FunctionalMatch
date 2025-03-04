
from dataclasses import dataclass
from typing import Union

from FunctionalMatch.Match import Match
from FunctionalMatch.ReturningFirstObjects import FromJSONPath, FromVariable, Invent


@dataclass(frozen=True, eq=True, order=True)
class Query:
    select: Match
    as_: Union[Invent, FromVariable, FromJSONPath]


def query_interpreter(query: Query, obj:object):
    test, outcome_list = query.select(obj)
    if not test:
        return test, outcome_list
    for dct in outcome_list:
        dct = query.as_(dct)
