import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from automaton.automaton import Automaton


class DFA(Automaton):

    def __init__(self, config_file):
        super().__init__(config_file)
        print("More precisely, a DFA.")

    def validate(self):
        return super().validate()

    def read_input(self, input_str):
        pass

    def accepts_input(self, input_str):
        return "I don't know what inputs to accept... yet!"


if __name__ == "__main__":

    num_args = len(sys.argv)
    if num_args > 1:
        print(f"I see you provided {num_args-1} argument{'s' if num_args > 2 else ''} from the console.")
        print("Here's a list with all the system arguments:")
        for i, arg in enumerate(sys.argv):
            print(f"Argument {i}: {arg:>32}")
        print()

    dfa = DFA('your_config_file')    
    print(dfa.validate())
    if dfa.validate():
        print(dfa.accepts_input('yout input'))
