from automata import DFA

if __name__ == '__main__':
    # automata = Automata()
    # automata.read_jff('../static/comecam-aa-ou-bb.xml')

    # print('States')
    # for state in automata.states_to_list():
    #     print(state)

    # print('\nTransitions')
    # for state in automata.transitions_to_list():
    #     print(state)

    # automata.to_jff()
    # afd.re
    # afd.read_jff('../static/comecam-aa-ou-bb.xml')

    afd = DFA(['a', 'b'])

    afd.create_state('q0', initial=True)
    afd.create_state('q1', final=True)
    afd.create_state('q2', final=True)

    afd.create_transition('q0', 'q1', 'a')
    afd.create_transition('q0', 'q2', 'b')

    afd.create_transition('q1', 'q0', 'b')
    afd.create_transition('q1', 'q1', 'a')

    afd.create_transition('q2', 'q0', 'a')
    afd.create_transition('q2', 'q2', 'b')

    # afd.minify()
    print(afd)

    string = 'aababbabb'
    print('Cadeia valida') if afd.check(string) else print('Cadeia invalida')

    # print(afd.check('aa'))
    # afd.create_transition('SN', 'sn', 1)
