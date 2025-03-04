from dataclasses import dataclass
from typing import Optional

from FunctionalMatch import var, structural_match, instantiate, JSONPath
from FunctionalMatch.PropositionalLogic import *
from FunctionalMatch.example.Node import Node
from FunctionalMatch.language.LanguageMainPoint import parse_query



def raw_example():
    l1 = Node.leaf(1)
    l2 = Node.leaf(2)
    l3 = Node.leaf(3)
    s1 = Node(0, l2, l3)
    r = Node(5, s1, l1)

    q = Node(var("x"), var("l"), var("r"))
    b, result = structural_match(q,
                                 r,
                                 True,
                                 Or(LEq(var("x"), 0), Eq(JSONPath("$.left.val"), 0)))
    print(b)
    print(result)

    instance = instantiate(q, **{"x": 23, "l": l1})
    print(instance)


if __name__ == '__main__':
    result = parse_query("/home/giacomo/PyCharmProjects/FunctionalMatch/query_test.txt")
    print(result)