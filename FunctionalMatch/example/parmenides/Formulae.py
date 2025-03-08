__author__ = "Giacomo Bergami"
__copyright__ = "Copyright 2024, Giacomo Bergami"
__credits__ = ["Giacomo Bergami"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Giacomo Bergami"
__email__ = "bergamigiacomo@gmail.com"
__status__ = "Production"

import copy
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Tuple, Dict, Union

class Formula:

    def __str__(self):
        return "Formula(?)"


def print_proprieties(proprieties, cop=None):
    if isinstance(proprieties, dict) or isinstance(proprieties, defaultdict):
        proprieties = proprieties.items()
    L = []
    for k, v in proprieties:
        k = k.replace("_", "\\_").replace(" ", "\; ")
        if isinstance(v, list) or isinstance(v, tuple):
            for x in v:
                L.append("\\texttt{" + str(k) + "}: " + str(x) if not isinstance(x, str) else x.replace("_", "\\_"))
        else:
            L.append("\\texttt{" + str(k) + "}: " + str(v) if not isinstance(v, str) else v.replace("_", "\\_"))
    if cop is not None:
        L.append("\\texttt{JJ}: " + str(cop))
    if len(L) > 0:
        return "_{" + ",\; ".join(L) + "}"
    else:
        return ""


@dataclass(order=True, frozen=True, eq=True)
class FVariable(Formula):
    name: str
    type: str
    specification: str  # extra
    cop: Formula
    id: int
    properties: frozenset = field(default_factory=lambda: frozenset())
    meta: str = field(default_factory=lambda: "FVariable")
    matched: bool = field(default_factory=lambda: False)

    def __str__(self):
        name = self.name
        if name is None:
            name = "?"
        else:
            name = "\\textsf{" + name + "}"
        if self.specification is not None:
            name += (" [\\textup{of}] " + str(self.specification))
            name = "\\left[" + name + "\\right]^{\\texttt{" + str(self.id) + "}}"
        else:
            name = "{" + name + "}^{\\texttt{" + str(self.id) + "}}"
        return name + print_proprieties(self.properties, self.cop)




@dataclass(order=True, frozen=True, eq=True)
class FUnaryPredicate(Formula):
    rel: str
    arg: Formula
    score: float
    properties: frozenset
    meta: str = field(default_factory=lambda: "FUnaryPredicate")
    matched: bool = field(default_factory=lambda: False)

    def __str__(self):
        name = self.rel
        if name is None:
            name = "?"
        else:
            name = "\\textit{" + name + "}"
        return name + print_proprieties(self.properties) + (("(" + str(self.arg) + ")") if self.arg is not None else "(?)")



@dataclass(order=True, frozen=True, eq=True)
class FBinaryPredicate(Formula):
    rel: str
    src: Formula
    dst: Formula
    score: float
    properties: frozenset
    meta: str = field(default_factory=lambda: "FBinaryPredicate")
    matched: bool = field(default_factory=lambda: False)

    def __str__(self):
        name = self.rel
        if name is None:
            name = "?"
        else:
            name = "\\textit{" + name + "}"
        s = "("
        if self.src is not None:
            s += (str(self.src) + ",")
        else:
            s += "?,"
        if self.dst is not None:
            s += (str(self.dst) + ")")
        else:
            s += "?)"
        return name + print_proprieties(self.properties) +s




@dataclass(order=True, frozen=True, eq=True)
class FAnd(Formula):
    args: Tuple[Formula]
    meta: str = field(default_factory=lambda: "FAnd")
    matched: bool = field(default_factory=lambda: False)

    def __str__(self):
        return "\\left(" + (" \\wedge ".join(map(str, self.args))) + "\\right)"



@dataclass(order=True, frozen=True, eq=True)
class FOr(Formula):
    args: Tuple[Formula]
    meta: str = field(default_factory=lambda: "FOr")
    matched: bool = field(default_factory=lambda: False)

    def __str__(self):
        return "\\left(" + (" \\vee ".join(map(str, self.args))) + "\\right)"





@dataclass(order=True, frozen=True, eq=True)
class FNot(Formula):
    arg: Formula
    meta: str = field(default_factory=lambda: "FNot")
    matched: bool = field(default_factory=lambda: False)

    def __str__(self):
        return " \\neg \\left(" + str(self.arg) + "\\right)"




def formula_from_dict(f: Union[dict, str]):
    """
    Loading a json file in its object-dictionary rerpesentation into formulaes.
    This is mainly used to run the pipeline from one point at a time.
    """
    if f is None:
        return None
    if isinstance(f, str):
        return f
    from collections.abc import Iterable
    if isinstance(f, Iterable) and not (isinstance(f, dict)):
        return list(map(formula_from_dict, f))
    assert "meta" in f
    meta = f["meta"]
    if meta == "FNot":
        return FNot(arg=formula_from_dict(f["arg"]))
    if meta == "FOr":
        return FOr(args=tuple(map(formula_from_dict, f["args"])))
    if meta == "FAnd":
        return FAnd(args=tuple(map(formula_from_dict, f["args"])))
    if meta == "FVariable":
        name = str(f["name"]) if "name" in f and f["name"] is not None else None
        type = str(f["type"]) if "name" in f and f["type"] is not None else None
        id = int(f["id"]) if "id" in f and f["id"] is not None else -1
        specification = formula_from_dict(f["specification"]) if "specification" in f and f["specification"] is not None else None
        cop = formula_from_dict(f["cop"]) if "cop" in f else None
        return FVariable(name=name, type=type, specification=specification, cop=cop, id=id)
    if meta == "FUnaryPredicate":
        rel = str(f["rel"]) if "rel" in f and f["rel"] is not None else ""
        arg = formula_from_dict(f["arg"]) if "arg" in f and f["arg"] is not None else None
        score = float(f["score"]) if "score" in f else 1.0
        properties = defaultdict(list)
        if "properties" in f:
            for k, v in f["properties"].items():
                for x in v:
                    properties[k].append(formula_from_dict(x))
        properties = {k: tuple(v) for k, v in properties.items()}
        return FUnaryPredicate(rel, arg, score, frozenset(properties.items()))
    if meta == "FBinaryPredicate":
        rel = str(f["rel"]) if "rel" in f else ""
        src = formula_from_dict(f["src"]) if "src" in f else None
        dst = formula_from_dict(f["dst"]) if "dst" in f else None
        score = float(f["score"]) if "score" in f else 1.0
        properties = defaultdict(list)
        if "properties" in f:
            for k, v in f["properties"].items():
                for x in v:
                    properties[k].append(formula_from_dict(x))
        properties = {k: tuple(v) for k, v in properties.items()}
        return FBinaryPredicate(rel, src, dst, score, frozenset(properties.items()))
