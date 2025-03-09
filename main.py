import json
import logging
from dataclasses import dataclass
from typing import Optional

# from FunctionalMatch import var, structural_match, instantiate, JSONPath
from FunctionalMatch.PropositionalLogic import *
from FunctionalMatch.example.Node import Node
from FunctionalMatch.example.parmenides.Formulae import formula_from_dict, FUnaryPredicate, FVariable, FBinaryPredicate
from FunctionalMatch.example.parmenides.knowledge_expansion import knowledge_expansion
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
    ## INIT PARMENIDES
    import os
    parmenides = "parmenides.ttl" if os.path.isfile("parmenides.ttl") else None
    from FunctionalMatch.example.parmenides.Parmenides import Parmenides, generate_parmenides_graph, ParmenidesSingleton
    logging.basicConfig(level=logging.INFO)
    ParmenidesSingleton.instance()
    ParmenidesSingleton.init("/home/giacomo/PyCharmProjects/FunctionalMatch/data/cache", "giacomo", "omocaig",
                             "localhost", 5432, False, parmenides)

    queries = parse_query("/home/giacomo/PyCharmProjects/FunctionalMatch/query_test.txt")

    traffic = FVariable("traffic", "Noun", None, None, 1)
    city_center = FVariable("city center", "Noun", None, None, 1)
    adj1 = FVariable("busy", "JJ", None, None, 1)
    datum2 = FBinaryPredicate("have", city_center, adj1, -1, frozenset())
    datum3 = FBinaryPredicate("have", city_center, city_center, -1, frozenset())
    datum = FUnaryPredicate("flow", traffic, 1.0, frozenset({"ciao": "giacomo"}.items()))
    # l1 = Node.leaf(1)
    # l2 = Node.leaf(2)
    # l3 = Node.leaf(3)
    # s1 = Node(0, l2, l3)
    # datum = Node(5, s1, l1)
    # result = ObjDepthDeterminer.get_depth_dictionary(datum)

    print(knowledge_expansion(datum, queries))
    print(knowledge_expansion(datum2, queries))
    print(knowledge_expansion(datum3, queries))
    # for query in queries:
    #     result = query([datum, datum2, datum3])
    #     print(result)

    ## STOP PARMENIDES
    ParmenidesSingleton.stop()

def parmenides_db_write():
    from FunctionalMatch.example.parmenides.Parmenides import Parmenides, generate_parmenides_graph
    logging.basicConfig(level=logging.INFO)
    p = Parmenides("/home/giacomo/PyCharmProjects/FunctionalMatch/data/cache","giacomo", "omocaig", "localhost", 5432, onStorage=False)
    import os

    p.start("parmenides.ttl" if os.path.isfile("parmenides.ttl") else None)
    #generate_parmenides_graph(p, "/home/giacomo/PyCharmProjects/FunctionalMatch/data")
    p.stop()


def formulae_rewriting_test():
    import os
    parmenides = "parmenides.ttl" if os.path.isfile("parmenides.ttl") else None
    from FunctionalMatch.example.parmenides.Parmenides import Parmenides, generate_parmenides_graph, ParmenidesSingleton
    logging.basicConfig(level=logging.INFO)
    ParmenidesSingleton.instance()
    ParmenidesSingleton.init("/home/giacomo/PyCharmProjects/FunctionalMatch/data/cache","giacomo", "omocaig", "localhost", 5432, False, parmenides)
    # with open("/home/giacomo/projects/LaSSI/catabolites/all_newcastle/logical_rewriting.json", "r") as f:
    #     data = json.load(f)
    # assert isinstance(data, list)
    # for dct in data:
    #     this = formula_from_dict(dct)
    #     print(this)
    l = ParmenidesSingleton.get().getOutgoingNodes("flow", "adjectivalForm")
    ParmenidesSingleton.stop()


if __name__ == '__main__':
    tst_query()