from dataclasses import dataclass
from typing import Optional

# from FunctionalMatch import var, structural_match, instantiate, JSONPath
from FunctionalMatch.PropositionalLogic import *
from FunctionalMatch.example.Node import Node
from FunctionalMatch.language.LanguageMainPoint import parse_query
from FunctionalMatch.utils import ObjDepthDeterminer


# def raw_ex():
#     l1 = Node.leaf(1)
#     l2 = Node.leaf(2)
#     l3 = Node.leaf(3)
#     s1 = Node(0, l2, l3)
#     r = Node(5, s1, l1)
#
#     from FunctionalMatch.functions.structural_match import var
#     q = Node(var("x"), var("l"), var("r"))
#     b, result = structural_match(q,
#                                  r,
#                                  True,
#                                  Or(LEq(var("x"), 0), Eq(JSONPath("$.left.val"), 0)))
#     print(b)
#     print(result)
#
#     instance = instantiate(q, **{"x": 23, "l": l1})
#     print(instance)


def tst_query():
    queries = parse_query("/home/giacomo/PyCharmProjects/FunctionalMatch/query_test.txt")

    l1 = Node.leaf(1)
    l2 = Node.leaf(2)
    l3 = Node.leaf(3)
    s1 = Node(0, l2, l3)
    datum = Node(5, s1, l1)
    # result = ObjDepthDeterminer.get_depth_dictionary(datum)

    for query in queries:
        result = query([datum])
        print(result)

def parmenides_db_write():
    from FunctionalMatch.example.parmenides.Parmenides import Parmenides, generate_parmenides_graph
    p = Parmenides("giacomo", "omocaig", "localhost", 5432)
    p.start()
    generate_parmenides_graph(p, "/home/giacomo/PyCharmProjects/FunctionalMatch/data")
    p.stop()

if __name__ == '__main__':
    parmenides_db_write()