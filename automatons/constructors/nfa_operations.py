from automatons.classes.nfa import NFA


def concat_automatons(automatons: list) -> NFA:
    nfa = NFA()
    nfa.root.by_eps.add(automatons[0].root)
    automatons[0].sink.by_eps.add(automatons[1].root)
    automatons[1].sink.by_eps.add(nfa.sink)

    nfa.sink.terminal = automatons[-1].sink.terminal
    nfa.add_nodes(automatons)
    return nfa


def unite_automatons(automatons: list) -> NFA:
    nfa = NFA()
    for a in automatons:
        nfa.root.by_eps.add(a.root)
        a.sink.by_eps.add(nfa.sink)

    nfa.add_nodes(automatons)
    return nfa


def closure_automaton(automaton) -> NFA:
    nfa = NFA()
    nfa.root.by_eps.add(automaton.root)
    nfa.root.by_eps.add(nfa.sink)
    nfa.sink.by_eps.add(automaton.root)
    automaton.sink.by_eps.add(nfa.sink)

    nfa.sink.terminal = automaton.sink.terminal
    nfa.add_nodes([automaton])
    return nfa
