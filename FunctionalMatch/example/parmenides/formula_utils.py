import latextools

from FunctionalMatch.example.parmenides.Formulae import Formula
from bs4 import BeautifulSoup, Tag

def latex_rendering(strx):
    latex_eq = latextools.render_snippet(
        r'$' + strx + '$',
        commands=[latextools.cmd.all_math])
    svg_eq = latex_eq.as_svg()
    import base64
    encoded = base64.b64encode(str.encode(svg_eq.content))
    svg = 'data:image/svg+xml;base64,{}'.format(encoded.decode())
    img = Tag(name="img")
    img["src"] = svg
    img["style"] = "width: 10vw; min-width: 50px;"
    return img

def latex_formula_rendering(formula:Formula):
    return latex_rendering(str(formula))

def practicalInstance(self, class_, name):
    return isinstance(self, class_) or type(self).__name__ == name

def getAtoms(self):
    """
    This function decomposes the formula (self) in its atomic constituents, returned as a bag of atoms
    """
    from FunctionalMatch.example.parmenides.Formulae import FUnaryPredicate, FBinaryPredicate, FAnd, FNot, FOr
    if practicalInstance(self, FUnaryPredicate, "FUnaryPredicate") or practicalInstance(self, FBinaryPredicate, "FBinaryPredicate"):
        return {self}
    elif practicalInstance(self, FAnd, "FAnd") or practicalInstance(self, FOr, "FOr"):
        s = set()
        for x in self.args:
            s = s.union(getAtoms(x))
        return s
    elif practicalInstance(self, FNot, "FNot"):
        return {self.arg}
    else:
        print("WARNING: cannot perform the atomization of a variable")
        return {}

from FunctionalMatch.example.parmenides.Formulae import *

def semantic(self, d: Dict[Formula, bool]):
    """
    This function decomposes the formula (self) in its atomic constituents, returned as a bag of atoms
    """
    if practicalInstance(self, FUnaryPredicate, "FUnaryPredicate") or practicalInstance(self, FBinaryPredicate,
                                                                                        "FBinaryPredicate"):
        assert self in d
        return d[self]
    elif practicalInstance(self, FAnd, "FAnd"):
        return min(map(lambda x: semantic(x, d), self.args))
    elif practicalInstance(self, FOr, "FOr"):
        return max(map(lambda x: semantic(x, d), self.args))
    elif practicalInstance(self, FNot, "FNot"):
        return 1 - semantic(self.arg, d)
    else:
        print("WARNING: cannot perform the atomization of a variable")
        return 0