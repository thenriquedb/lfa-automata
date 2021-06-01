from automata import Automata, AFD

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
    afd = AFD(['a', 'b'])
    # afd.re
    # afd.read_jff('../static/comecam-aa-ou-bb.xml')

    for i in range(1, 5):
        afd.create_state(i)

    afd.config_state(1, initial=True)
    afd.config_state(4, final=True)

    afd.create_transition(1, 2, 'a')
    afd.create_transition(2, 1, 'a')
    afd.create_transition(3, 4, 'a')
    afd.create_transition(4, 3, 'a')
    afd.create_transition(1, 3, 'b')
    afd.create_transition(3, 1, 'b')
    afd.create_transition(4, 4, 'b')
    afd.create_transition(4, 2, 'b')

    print(afd)

    string = 'abbaab'
    # print(afd.check('aa'))
    # afd.create_transition('SN', 'sn', 1)
