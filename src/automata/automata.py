
import xmltodict
from xml.dom.minidom import parseString
from dicttoxml import dicttoxml
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

    def read_jff(self, path: str):
        with open(path) as fd:
            self.__doc = xmltodict.parse(fd.read())
            return self.__doc

    def __export_jff_file(self, xml, path: str):
        print(xml)
        with open(path, 'w') as file:
            file.write(str(xml))

    def to_jff(self, path="../static/generated-xml.xml"):
        data = {
            "structure": {
                "automaton": {
                    "transitions": self.transitions,
                    "states": self.states_to_list(),
                }
            }
        }

        xml_str = dicttoxml(data, attr_type=False)
        dom = parseString(xml_str)
        print(dom.toprettyxml())
        # print etree.tostring(x, pretty_print=True)

        # dom = xml.dom.minidom (str(xml))
        # xml.dom.minidom().

        self.__export_jff_file(dom.toprettyxml(), path)
