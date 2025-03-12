import os
import pickle
from collections import defaultdict
from typing import List

import pandas
from functools import reduce

from FunctionalMatch.example.LaSSI.eFOLsemantics.ExpandConstituents import ExpandConstituents
from FunctionalMatch.example.parmenides.Formulae import Formula
from FunctionalMatch.example.parmenides.formula_utils import latex_rendering
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

    def getImplExpansions(self, minimal_constituent_idx):
        return self.ec.getImplExpansions(minimal_constituent_idx)

    def getEqExpansions(self, minimal_constituent_idx):
        return self.ec.getEqExpansions(minimal_constituent_idx)

    def getImplExpansionExplanation(self, minimal_constituent_idx, rw=None):
        return self.ec.getImplExpansionExplanation(minimal_constituent_idx, rw)

    def getEqExpansionExplanation(self, minimal_constituent_idx, rw=None):
        return self.ec.getEqExpansionExplanation(minimal_constituent_idx, rw)

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

    def buildReport(self, file):
        from bs4 import Tag
        from FunctionalMatch.example.parmenides.formula_utils import latex_formula_rendering
        html = Tag(name="html")
        body = Tag(name="body")

        p_ = Tag(name="h1")
        p_.append("Constutents DB")
        body.append(p_)
        ol = Tag(name="ol")
        constituents = self.minimal_constituents.getAllObjects()
        for idx, x in enumerate(constituents):
            li = Tag(name="li")
            li["id"] = f"constituent{idx}"
            li.append(latex_formula_rendering(x))

            pp = Tag(name="p")
            pp.append("Eq Rewriting:")
            li.append(pp)
            ool = Tag(name="ol")
            eqex = self.getEqExpansions(idx)
            meqex = {x:idx2+1 for idx2, x in enumerate(eqex)}
            fmeqex = self.getEqExpansionExplanation(idx, meqex)
            for x in eqex:
                lli = Tag(name="li")
                lli.append(latex_formula_rendering(x))
                uuul = Tag(name="ul")
                for rule in fmeqex[x]:
                    llli = Tag(name="li")
                    llli.append(latex_rendering(rule))
                    uuul.append(llli)
                lli.append(uuul)
                ool.append(lli)
            li.append(ool)

            pp = Tag(name="p")
            pp.append("Impl Rewriting:")
            li.append(pp)
            imex = self.getImplExpansions(idx)
            mimex = {x:idx2+1 for idx2, x in enumerate(imex)}
            fmimex = self.getImplExpansionExplanation(idx, mimex)
            ool = Tag(name="ol")
            for x in imex:
                lli = Tag(name="li")
                lli.append(latex_formula_rendering(x))
                uuul = Tag(name="ul")
                for rule in fmimex[x]:
                    llli = Tag(name="li")
                    llli.append(latex_rendering(rule))
                    uuul.append(llli)
                lli.append(uuul)
                ool.append(lli)
            li.append(ool)

            ol.append(li)
        body.append(ol)

        p_ = Tag(name="h1")
        p_.append("Sentences DB")
        body.append(p_)
        uul = Tag(name="ul")
        body.append(uul)

        for i, sentence in enumerate(self.sentence_list):
            minimal_constituents = self.minimal_constituent_dict[i]
            ref = f"Sentence{i}"
            Sentence = f"Sentence #{i}"

            lli = Tag(name="li")
            lla = Tag(name="a")
            lla["href"] = f"#{ref}"
            lla.append(Sentence)
            lli.append(lla)
            uul.append(lli)

            h1 = Tag(name="h2")
            a = Tag(name="a")
            h1["id"] = ref
            a.append(Sentence)
            h1.append(a)
            body.append(h1)

            p1 = Tag(name="p")
            p1.append("Logic form: ")
            p1.append(latex_formula_rendering(sentence))
            body.append(p1)

            p2 = Tag(name="p")
            p2.append("Minimal Constituents:")
            body.append(p2)
            ol = Tag(name="ul")
            for x_idx in minimal_constituents:
                li = Tag(name="li")
                ali = Tag(name="a")
                ali["href"] = f"#constituent{x_idx}"
                ali.append(str(x_idx))
                ali.append(latex_formula_rendering(constituents[x_idx]))
                li.append(ali)
                ol.append(li)


            body.append(ol)
        html.append(body)
        html.decode()

        with open(file, "w") as f:
            f.write(str(html))


