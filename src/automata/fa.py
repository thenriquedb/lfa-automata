from abc import ABC, abstractmethod


class FA():
    def __init__(self, alphabet):
        self.alphabet = alphabet
        self.states = set()
        self.transitions = dict()
        self.valid_transitions = dict()
        self.initial = None
        self.current_state = None
        self.finals = set()
        self.__has_error = False

    def clear_afd(self):
        """Inicializa as variaveis utilizadas no processamento de cadeias"""
        self.__has_error = False
        self.__current_state = self.initial

    @property
    def has_error(self):
        return self.__has_error

    def current_state(self):
        return self.__current_state

    def _state_is_valid(self, state):
        if state in self.states:
            return True
        return False

    def _symbol_is_valid(self, symbol):
        if len(symbol) != 1 or symbol in self.alphabet:
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

    @abstractmethod
    def create_transition(self, origin: int, destiny: int, symbol: str):
        pass

    def change_initial_state(self, id: int):
        """Define um estado já existente como inicial"""
        if not self._state_is_valid(id):
            return

        self.initial = id

    def change_final_state(self, id: int, final: bool):
        """Define um estado já existente como final"""
        if not self._state_is_valid(id):
            return
        if final:
            self.finals = self.finals.union({id})
        else:
            self.finals = self.finals.difference({id})

    def config_state(self, state, initial=False, final=False):
        if not self._state_is_valid(state):
            return

        if initial:
            self.initial = state
        if final:
            self.finals.add(state)
        elif self._state_is_valid(state) and state in self.finals:
            self.finals.remove(state)

    @abstractmethod
    def move(self, string: str):
        """
        Partindo do estado atual, processa a cadeia e retorna o estado de parada. 
        Se ocorrer error, defina a variável __has_error como True
        """
        pass

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
        for symbol in self.alphabet:
            string += '{}, '.format(str(symbol))
        string += '} \n'

        string += '  T = { '
        for (state, symbol) in self.transitions.keys():
            destiny = self.transitions[(state, symbol)]
            string += '({},{}) --> {}, '.format(state, symbol, destiny)
        string += '} \n'

        string += '  Valid T = { '
        for state in self.valid_transitions.keys():
            destiny = self.valid_transitions[state]
            string += '{} --> {}, '.format(state, destiny)
        string += '} \n'

        string += '  I = {} \n'.format(self.initial)

        string += '  F = { '
        for state in self.finals:
            string += '{}'.format(str(state))
        string += ' } \n'

        return string
