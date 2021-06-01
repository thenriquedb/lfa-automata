from automata import Automata


class AFD(Automata):
    def __init__(self, alfabeto):
        self.states = set()
        self.alfabeto = alfabeto
        self.transitions = dict()
        self.initial = None
        self.finals = set()

    def clear_afd(self):
        """Inicializa as variaveis utilizadas no processamento de cadeias"""
        self.__hasError = False
        self.__current_state = self.initial

    @property
    def has_error(self):
        return self.__has_error

    @property
    def current_state(self):
        return self.__current_state

    def __state_is_valid(self, state):
        if state in self.states:
            return True
        return False

    def __symbol_is_valid(self, symbol):
        if len(symbol) != 1 or symbol in self.alfabeto:
            return True
        return False

    def create_state(self, id: int, initial=False, final=False):
        if id in self.states:
            return False

        self.states = self.states.union({id})

        if initial:
            self.initial = id
        if final:
            self.finals = self.finals.union({id})

        return True

    def create_transition(self, origin: int, destiny: int, symbol: str):
        if not self.__state_is_valid(origin):
            return False
        if not self.__state_is_valid(destiny):
            return False
        if not self.__symbol_is_valid(symbol):
            return False

        self.transitions[(origin, symbol)] = destiny

    def change_initial_state(self, id: int):
        """Define um estado já existente como inicial"""
        if not self.__state_is_valid(id):
            return

        self.initial = id

    def change_final_state(self, id: int, final: bool):
        """Define um estado já existente como final"""
        if not self.__state_is_valid(id):
            return
        if final:
            self.finals = self.finals.union({id})
        else:
            self.finals = self.finals.difference({id})

    def config_state(self, state, initial=False, final=False):
        if not self.__state_is_valid(state):
            return

        if initial:
            self.initial = state
        if final:
            self.finals.add(state)
        elif self.__state_is_valid(state) and state in self.finals:
            self.finals.remove(state)

    def move(self, string: str):
        """
        Partindo do estado atual, processa a cadeia e retorna o estado de parada. 
        Se ocorrer error, defina a variável __has_error como True
        """
        for symbol in string:
            if not self.__symbol_is_valid(symbol):
                self.__hasError = True
                break

            if(self.__current_state, symbol) in self.transitions.keys():
                new_state = self.transitions[(self.__current_state, symbol)]
                self.__current_state = new_state
            else:
                self.__hasError = True
                break

            return self.__current_state

    def check(self, string):
        state = self.initial

        for symbol in string:
            if not (state, symbol) in self.transitions:
                return False
            else:
                self.transitions[(state, symbol)] = state

        return state in self.finals

    def __str__(self):
        string = 'AFD(E, A, T,i, F): \n'

        string += '  S = { '
        for state in self.states:
            string += '{}, '.format(str(state))
        string += '} \n'

        string += '  A = { '
        for symbol in self.alfabeto:
            string += '{}, '.format(str(symbol))
        string += '} \n'

        string += '  T = { '
        for (state, symbol) in self.transitions.keys():
            destiny = self.transitions[(state, symbol)]
            string += '({},{}) --> {} '.format(state, symbol, destiny)
        string += '} \n'

        string += '  I = {} \n'.format(self.initial)

        string += '  F = { '
        for state in self.finals:
            string += '{}'.format(str(state))
        string += ' } \n'

        return string
