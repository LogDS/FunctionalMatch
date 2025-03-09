from FunctionalMatch.example.parmenides.Formulae import FVariable
from FunctionalMatch.example.parmenides.Parmenides import ParmenidesSingleton


def adjectivalForm(d, **kwargs):
    var = kwargs.get("variable", None)
    result = kwargs.get("result", None)
    assert var is not None
    assert result is not None
    assert isinstance(var, str)
    assert isinstance(result, str)
    adjForm = d.get(var)
    assert isinstance(adjForm, str)
    S = ParmenidesSingleton.get().getOutgoingNodes(adjForm, "adjectivalForm")
    if len(S) == 0:
        return []
    else:
        L = []
        for x in S:
            dd = {k:v for k,v in d.items()}
            dd[result] = x
            L.append(dd)
        return L


def partOf(d, **kwargs):
    var = kwargs.get("variable", None)
    result = kwargs.get("result", None)
    assert var is not None
    assert result is not None
    assert isinstance(var, str)
    assert isinstance(result, str)
    adjForm = d.get(var)
    assert isinstance(adjForm, str)
    S = ParmenidesSingleton.get().getOutgoingNodes(adjForm, "partOf")
    if len(S) == 0:
        return []
    else:
        L = []
        for x in S:
            dd = {k:v for k,v in d.items()}
            dd[result] = x
            L.append(dd)
        return L

def addAdjective(d, **kwargs):
    if d is None:
        print("No variable to add the adjective: returning NONE")
        return None
    if isinstance(d, FVariable) or type(d).__name__ == "FVariable":
        var = kwargs.get("adjective", None)
        assert var is not None
        assert isinstance(var, str)
        return d.add_adjective(var)
    else:
        raise RuntimeError("ERROR: we can add an adjective only to something that is a variable!")