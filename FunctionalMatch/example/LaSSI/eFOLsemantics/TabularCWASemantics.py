import os
import pickle
from collections import defaultdict
from typing import List

import pandas
from functools import reduce

from FunctionalMatch.example.LaSSI.eFOLsemantics.ExpandConstituents import ExpandConstituents
from FunctionalMatch.example.parmenides.Formulae import Formula
from FunctionalMatch.utils import CountingDictionary

def with_variables_from(f, l, minimal_constituents: CountingDictionary, fn, selection=False):
    from FunctionalMatch.example.parmenides.formula_utils import semantic
    pdf = reduce(lambda x,y: x.merge(y, how="cross"),[pandas.DataFrame({str(x): [1,0]}) for x in l])
    L = []
    for x in pdf.to_dict(orient='records'):
        d = dict()
        for k,v in x.items():
            d[minimal_constituents.fromId(int(k))] = v
        x[fn] = semantic(f, d)
        if not selection or x[fn]>0.0:
            L.append(x)
    return pandas.DataFrame(L)

def with_true_variables_from(l):
    return pandas.DataFrame({str(x): [1] for x in l})


class TabularCWASemantics:
    def __init__(self, sentence_list:List[Formula], cache_folder):
        self.sentence_list = []
        self.sentence_to_id = dict()
        for idx in range(len(sentence_list)):
            self.sentence_to_id[sentence_list[idx]] = idx
            self.sentence_list.append(sentence_list[idx])
        # self.kb = kb
        self.minimal_constituents = CountingDictionary()
        self.U = None
        self.minimal_constituent_dict = defaultdict(set)
        self.buildup = False
        self.ec = None
        self.cache_folder = cache_folder

        #getSentenceAtomsFromId
        for sentence_id in range(len(self.sentence_list)):
            # collect_sentence_constituents
            from FunctionalMatch.example.parmenides.formula_utils import getAtoms
            # getSentenceAtomsFromId, for arg
            for x in getAtoms(self.sentence_list[sentence_id]):
                self.minimal_constituent_dict[sentence_id].add(self.minimal_constituents.add(x))

        d_folder = os.path.join(self.cache_folder, "_d.pickle")
        cd_folder = os.path.join(self.cache_folder, "_cd.pickle")
        with open(d_folder, "wb") as p:
            pickle.dump(self.minimal_constituent_dict, p, protocol=pickle.HIGHEST_PROTOCOL)
        with open(cd_folder, "wb") as p:
            pickle.dump(self.minimal_constituents, p, protocol=pickle.HIGHEST_PROTOCOL)
        self.ec = ExpandConstituents(self.cache_folder, self.minimal_constituents.getAllObjects())

    def __call__(self, i, j):
        return self.get_straightforward_id_similarity(self.sentence_to_id[i], self.sentence_to_id[j])

    def _mutual_truth(self, i, j):
        test = self.ec.determine(i, j) #self.get_mutual_truth(i, j)
        # relation = Relation()
        # relation.add_attributes([str(i), str(j)])
        from FunctionalMatch.example.LaSSI.eFOLsemantics.Enums import PairwiseCases
        if (test == PairwiseCases.NonImplying):
            return pandas.DataFrame({str(i): [0,0,1,1],
                     str(j): [0,1,0,1]})
        elif (test == PairwiseCases.Implying):
            return pandas.DataFrame({str(i): [0, 0, 1],
                            str(j): [0, 1, 1]  })
        elif (test == PairwiseCases.MutuallyExclusive):
            return pandas.DataFrame({str(i): [0, 1],
                           str(j): [1,0]})
        elif (test == PairwiseCases.Equivalent):
            return pandas.DataFrame({str(i): [0, 1],
                           str(j): [0,1]})

    def _universal_truth(self, S, T):
        L = list()
        N = len(S.union(T))
        if N == 0:
            # relation = Relation(name="R")
            return pandas.DataFrame({})
        if N == len(S.intersection(T)) and N == 1:
            return pandas.DataFrame({str(list(S)[0]):[0,1]})
        else:
            for i in S:
                for j in T:
                    if i != j:
                        L.append(self._mutual_truth(i, j))
            return reduce(lambda x, y: x.merge(y), L)

    def get_straightforward_id_similarity(self, i, j):
        Ri = with_variables_from(self.sentence_list[i], self.minimal_constituent_dict[i], self.minimal_constituents, "R" + str(i), True)
        Rj = with_variables_from(self.sentence_list[j], self.minimal_constituent_dict[j], self.minimal_constituents, "R" + str(j))
        result = self._universal_truth(set(self.minimal_constituent_dict[i]), set(self.minimal_constituent_dict[j])).merge(Ri).merge(Rj)[list(set(Ri.columns).union(set(Rj.columns)))].drop_duplicates()[["R" + str(j)]].prod(axis=1)
        total = result.sum(axis=0)/len(result)
        # print(f"{i}~{j} := {total}")
        return total

    def buildReport(self):
        from bs4 import Tag
        from FunctionalMatch.example.parmenides.formula_utils import latex_formula_rendering
        html = Tag(name="html")
        body = Tag(name="body")

        for i in enumerate(self.sentence_list):
            sentence = self.sentence_list[i]
            minimal_constituents = self.minimal_constituents[i]

            h1 = Tag(name="h1")
            h1.append(f"Sentence #{i}")
            body.append(h1)

            p1 = Tag(name="p")
            p1.append("Logic form: ")
            p1.append(latex_formula_rendering(sentence))
            body.append(p1)

            p2 = Tag(name="p")
            p2.append("Minimal Constituents:")
            body.append(p2)

            ul = Tag(name="ul")
            for x in minimal_constituents:
                li = Tag(name="li")
                li.append(latex_formula_rendering(x))
                ul.append(li)
            body.append(ul)
        html.append(body)
        html.decode()


