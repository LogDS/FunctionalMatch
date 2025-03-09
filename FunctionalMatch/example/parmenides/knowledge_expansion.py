

def knowledge_expansion(sentence, queries):
    from FunctionalMatch.example.parmenides.Parmenides import ParmenidesSingleton
    assert ParmenidesSingleton.isReady()
    S = {sentence}
    previous_size = 0
    while len(S) > previous_size:
        previous_size = len(S)
        for query in queries:
            hasResult, outcomes = query(list(S))
            if hasResult:
                for x in outcomes:
                    S.add(x)
    return S #Expanded knowledge