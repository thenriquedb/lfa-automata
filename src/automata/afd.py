
class AFD:
    def __init__(self, alfabeto) -> None:
        self.states = list()
        self.alfabeto = alfabeto
        self.transitions = dict()
        self.initial = None
        self.finals = list()
        self.hasError = False

    def _stateIsValid(self, state):
        if state in self.states:
            return True
        return False

    def _symbolIsValid(self, symbol):
        if symbol in self.alfabeto:
            return True
        return False

    def clear(self):
        print('clear afd')

    def createState(self, name):
        if not None in self.states:
            self.states.append(name)

    def createTransition(self, origin, destiny, symbol):
        if not self._stateIsValid(origin):
            return False
        if not self._stateIsValid(destiny):
            return False
        if not self._symbolIsValid(symbol):
            return False

        self.transitions[(origin, destiny)] = destiny

    def configState(self, state, initial=False, final=False):
        if not self._stateIsValid(state):
            return

        if initial:
            self.initial = state
        if final:
            self.finals.append(state)
        elif self._stateIsValid(state) and state in self.finals:
            self.finals.remove(state)

    def check(self, string):
        state = self.initial

        for symbol in string:
            if not (state, symbol) in self.transitions:
                return False
            else:
                self.transitions[(state, symbol)] = state

        return state in self.finals

    def __str__(self):
        return 'print'


if __name__ == '__main__':
    afd = AFD(['a', 'b'])

    for i in range(1, 5):
        afd.createState(i)

    afd.configState(1, initial=True)
    afd.configState(4)

    afd.createTransition(1, 2, 'a')
    afd.createTransition(2, 1, 'a')
    afd.createTransition(3, 4, 'a')
    afd.createTransition(4, 3, 'a')
    afd.createTransition(1, 3, 'b')
    afd.createTransition(3, 1, 'b')
    afd.createTransition(4, 4, 'b')
    afd.createTransition(4, 2, 'b')

    print(afd)

    string = 'abbaab'
    afd.clear()
    # print(afd.check('aa'))
    # afd.createTransition('SN', 'sn', 1)
