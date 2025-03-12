from collections import defaultdict


def knowledge_expansion(sentence, queries):
    """
    :param sentence:    Single atom/proposition
    """
    from FunctionalMatch.example.parmenides.Parmenides import ParmenidesSingleton
    assert ParmenidesSingleton.isReady()
    from FunctionalMatch.example.parmenides.Formulae import FAnd, FOr
    assert (not isinstance(sentence, FAnd)) and (not isinstance(sentence, FOr))
    S = dict()
    S[sentence] = list()
    # previous_size = 0
    toVisit = {sentence}
    while len(toVisit) > 0:
        # previous_size = len(S)
        tmp = set()
        for src in toVisit:
            for idx, query in enumerate(queries):
                hasResult, outcomes = query([src])
                if hasResult:
                    for x in outcomes:
                        S[src].append((idx,x))
                        if x not in S:
                            S[x] = list()
                            tmp.add(x)
        toVisit = tmp
    return S #Expanded knowledge


class TBoxReasoningSingleton(object):
    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @staticmethod
    def isReady():
        return (TBoxReasoningSingleton._instance is not None) and (TBoxReasoningSingleton._instance.rules is not None)

    @classmethod
    def instance(cls):
        if cls._instance is None:
            print('Creating new instance')
            cls._instance = cls.__new__(cls)
            cls._instance.rules = None
        return cls._instance

    @staticmethod
    def init(impl_file, eq_file):
        if TBoxReasoningSingleton._instance.rules is None:
            TBoxReasoningSingleton._instance.rules = TBoxReasoning(impl_file, eq_file)

    @staticmethod
    def knowledge_expand(formula, isImpl):
        assert TBoxReasoningSingleton.isReady()
        return knowledge_expansion(formula, TBoxReasoningSingleton.get_eq_rules() if (not isImpl) else TBoxReasoningSingleton.get_impl_rules())

    @staticmethod
    def get_eq_rules():
        assert TBoxReasoningSingleton.isReady()
        return TBoxReasoningSingleton._instance.rules.get_eq_rules()

    @staticmethod
    def get_impl_rules():
        assert TBoxReasoningSingleton.isReady()
        return TBoxReasoningSingleton._instance.rules.get_impl_rules()


class TBoxReasoning(object):

    def __init__(self, impl_file, eq_file):
        self.eq_file = eq_file
        self.impl_file = impl_file
        from FunctionalMatch.language.LanguageMainPoint import parse_query
        self.eq_rules = parse_query(eq_file)
        self.impl_rules = parse_query(impl_file)

    def get_eq_rules(self):
        return self.eq_rules

    def get_impl_rules(self):
        return self.impl_rules