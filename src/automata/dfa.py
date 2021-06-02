from .fa import FA


class DFA(FA):
    def __init__(self, alfabeto):
        FA.__init__(self, alfabeto)

    def __update_transitions_history(self, origin: str, destiny: str, symbol: str):
        """
        Armazena o histórico de todas as transições realizadas sem repetições.
        Este método é fundamental para a implementação do algoritmo de remoção
        de estados Inalcançáveis.
        Args:
            origin (str): Estado de origem
            destiny (str): Estado de destino

        Returns:
            Cada estado é representado com uma lista de tupla,
            onde o primeiro valor é o estado que alcança e o segundo é o simbolo.
            Por exemplo:
            {
                1: [(2, 'a'), (2, 'a')],
                2: [(1, 'a')],
                5: [(5, 'a')]
            }
        """
        valid_transitions = self.valid_transitions
        if origin in valid_transitions.keys():
            transtion = valid_transitions[origin]
            valid_transitions[origin] = transtion.union({(destiny, symbol)})
        else:
            new_set = set()
            new_set.add((destiny, symbol))
            valid_transitions[origin] = new_set

        self.valid_transitions = valid_transitions
        return valid_transitions

    def create_transition(self, origin: str, destiny: str, symbol: str):
        """Cria uma nova transição de estado

        Args:
            origin (str): Estado de origem
            destiny (str): Estado de destino
            symbol (str): Simbôlo da transição

        Returns:
            (boolean): Retorna True em caso de sucesso ou False se ocorrer algum erro
        """
        if not self._state_is_valid(origin):
            return False
        if not self._state_is_valid(destiny):
            return False
        if not self._symbol_is_valid(symbol):
            return False

        self.__update_transitions_history(origin, destiny, symbol)
        self.transitions[(origin, symbol)] = destiny

        return True

    def move(self, string: str):
        """
        Partindo do estado atual, processa a cadeia e retorna o estado de parada.
        Se ocorrer error, defina a variável __has_error como True
        """
        for symbol in string:
            if not self._symbol_is_valid(symbol):
                self.__hasError = True
                break

            if(self.__current_state, symbol) in self.transitions.keys():
                new_state = self.transitions[(self.__current_state, symbol)]
                self.__current_state = new_state
            else:
                self.__hasError = True
                break

            return self.__current_state

    def __remove_unreachable_states(self):
        """
        Remove os estados inalcançaveis e suas transições
        """
        reachable_states = self.__get_reachable_states()

        # Remove transições desnecessárias
        new_transitions = dict()
        for (state, transitions) in self.valid_transitions.items():
            if state in reachable_states:
                new_transitions[state] = transitions

        # Remove estados inalcançaveis
        states = self.states
        new_states = filter(lambda state: state in reachable_states, states)

        self.states = list(new_states)
        self.valid_transitions = new_transitions

    def __get_reachable_states(self):
        """
        Retorna todos os estados alcançaveis através do estado inicial.

        Returns:
            Um conjunto com os estados que são aalcançaveis através do estado inicial 
        """
        reachable_states = set()
        states_to_check = []
        states_to_check.append(self.initial)
        reachable_states.add(self.initial)

        while len(states_to_check) != 0:
            checking_state = states_to_check.pop()

            visited_states = []
            if checking_state in self.valid_transitions.keys():
                visited_states = self.valid_transitions[checking_state]

            for state in visited_states:
                if state in visited_states:
                    reachable_states.add(state[0])

                if state not in reachable_states:
                    states_to_check.append(state[0])

            return reachable_states

    def minify(self):
        self.__remove_unreachable_states()
