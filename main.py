import logging

from FunctionalMatch.example.LaSSI.eFOLsemantics.TabularCWASemantics import TabularCWASemantics
# from FunctionalMatch import var, structural_match, instantiate, JSONPath
from FunctionalMatch.example.parmenides.Formulae import FUnaryPredicate, FVariable, FBinaryPredicate
# from FunctionalMatch.example.LaSSI.eFOLsemantics.knowledge_expansion import knowledge_expansion
from FunctionalMatch.language.LanguageMainPoint import parse_query


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
    from FunctionalMatch.example.parmenides.Parmenides import ParmenidesSingleton
    logging.basicConfig(level=logging.INFO)
    ParmenidesSingleton.instance()
    ParmenidesSingleton.init("/home/giacomo/PyCharmProjects/FunctionalMatch/data/cache", "giacomo", "omocaig",
                             "localhost", 5432, False, parmenides)

    # queries = parse_query("/query_impl.txt")

    traffic = FVariable("traffic", "Noun", None, None, 1)
    city_center = FVariable("city center", "Noun", None, None, 1)
    adj1 = FVariable("busy", "JJ", None, None, 1)
    adj2 = FVariable("fast", "JJ", None, None, 1)
    ncl = FVariable("Newcastle", "LOC", None, None, 1)
    fast_traffic = FVariable("traffic", "Noun", None, adj2, 1)
    datum = FUnaryPredicate("flow", traffic, 1.0, frozenset({"ciao": "giacomo"}.items()))
    datum2 = FBinaryPredicate("have", city_center, adj1, -1, frozenset())
    datum3 = FBinaryPredicate("have", city_center, city_center, -1, frozenset())
    datum4 = FBinaryPredicate("have", city_center, adj2, -1, frozenset())
    datum5 = FUnaryPredicate("be", fast_traffic, 1.0, frozenset({"ciao": "giacomo"}.items()))
    datum6 = FBinaryPredicate("have", ncl, traffic, -1, frozenset())
    datum7 = FUnaryPredicate("be", adj2, -1, frozenset({"SPACE": ncl}.items()))

    sentences = [datum, datum2, datum3, datum4, datum5, datum6, datum7]

    from FunctionalMatch.example.LaSSI.eFOLsemantics.TBoxReasoning import TBoxReasoningSingleton
    print("Init TBox Reasoning Rules")
    TBoxReasoningSingleton.instance()
    # TBoxReasoningSingleton.init("/home/giacomo/PyCharmProjects/FunctionalMatch/query_test.txt",
    #                             "/home/giacomo/PyCharmProjects/FunctionalMatch/query_test.txt")
    TBoxReasoningSingleton.init("/home/giacomo/PyCharmProjects/FunctionalMatch/query_impl.txt",
                                "/home/giacomo/PyCharmProjects/FunctionalMatch/query_eq.txt")

    print("Initializing all the data and performing the expansion")
    cwa = TabularCWASemantics(sentences, "/home/giacomo/PyCharmProjects/FunctionalMatch/data/cache")

    print("Building Report!")
    cwa.buildReport("/home/giacomo/PyCharmProjects/FunctionalMatch/report.html")

    # l1 = Node.leaf(1)
    # l2 = Node.leaf(2)
    # l3 = Node.leaf(3)
    # s1 = Node(0, l2, l3)
    # datum = Node(5, s1, l1)
    # result = ObjDepthDeterminer.get_depth_dictionary(datum)

    # print(knowledge_expansion(datum, queries))
    # print(knowledge_expansion(datum2, queries))
    # print(knowledge_expansion(datum3, queries))
    # print(knowledge_expansion(datum4, queries))
    # print(knowledge_expansion(datum6, queries))
    # print(knowledge_expansion(datum7, queries))
    # for query in queries:
    #     result = query([datum, datum2, datum3])
    #     print(result)

    ## STOP PARMENIDES
    ParmenidesSingleton.stop()

def parmenides_db_write():
    from FunctionalMatch.example.parmenides.Parmenides import Parmenides
    logging.basicConfig(level=logging.INFO)
    p = Parmenides("/home/giacomo/PyCharmProjects/FunctionalMatch/data/cache","giacomo", "omocaig", "localhost", 5432, onStorage=False)
    import os

    p.start("parmenides.ttl" if os.path.isfile("parmenides.ttl") else None)
    #generate_parmenides_graph(p, "/home/giacomo/PyCharmProjects/FunctionalMatch/data")
    p.stop()

def simpler_test():
    adj2 = FVariable("fast", "JJ", None, None, 1)
    ncl = FVariable("Newcastle", "LOC", None, None, 1)
    becl = FUnaryPredicate("be", adj2, -1, frozenset({"SPACE": ncl}.items()))

    ## INIT PARMENIDES
    import os
    parmenides = "parmenides.ttl" if os.path.isfile("parmenides.ttl") else None
    from FunctionalMatch.example.parmenides.Parmenides import ParmenidesSingleton
    logging.basicConfig(level=logging.INFO)
    ParmenidesSingleton.instance()
    ParmenidesSingleton.init("/home/giacomo/PyCharmProjects/FunctionalMatch/data/cache", "giacomo", "omocaig",
                             "localhost", 5432, False, parmenides)

    queries = parse_query("/home/giacomo/PyCharmProjects/FunctionalMatch/query_test.txt")

    from FunctionalMatch.example.LaSSI.eFOLsemantics.TBoxReasoning import knowledge_expansion
    print(knowledge_expansion(becl, queries))

    ## STOP PARMENIDES
    ParmenidesSingleton.stop()


def formulae_rewriting_test():
    import os
    parmenides = "parmenides.ttl" if os.path.isfile("parmenides.ttl") else None
    from FunctionalMatch.example.parmenides.Parmenides import ParmenidesSingleton
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
    # simpler_test()