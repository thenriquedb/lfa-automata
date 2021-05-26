
import xmltodict
from .helpers import map_states, map_transitions


class Automata:
    def __init__(self):
        self.__doc = None

    @property
    def states(self):
        return self.__doc['structure']['automaton']['state']

    @property
    def transitions(self):
        return self.__doc['structure']['automaton']['transition']

    def states_to_list(self):
        return list(map(map_states, self.states))

    def transitions_to_list(self):
        return list(map(map_transitions, self.transitions))

    def read_jflap(self, path: str):
        with open(path) as fd:
            self.__doc = xmltodict.parse(fd.read())
            return self.__doc
