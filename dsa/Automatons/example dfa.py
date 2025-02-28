from pyformlang.finite_automaton import DeterministicFiniteAutomaton, State, Symbol

# Define states
q0 = State(0)  # Even number of 'a's (Start/Accepting state)
q1 = State(1)  # Odd number of 'a's

# Define input symbols
a = Symbol("a")
b = Symbol("b")  # Any other symbol

# Create DFA
dfa = DeterministicFiniteAutomaton()

# Set start state
dfa.add_start_state(q0)

# Set accepting state(s)
dfa.add_final_state(q0)

# Define transitions
dfa.add_transition(q0, a, q1)  # 'a' flips state
dfa.add_transition(q1, a, q0)  # 'a' flips back
dfa.add_transition(q0, b, q0)  # 'b' doesn't change state
dfa.add_transition(q1, b, q1)  # 'b' doesn't change state

# **Test the DFA**
def test_string(s):
    return dfa.accepts([Symbol(c) for c in s])

# **Example Tests**
inputstrings=["","aa","aba","abba"]
for inputstring  in inputstrings:
    if test_string(inputstring):
        print(inputstring," is accepted")
    else:
        print(inputstring," is not accepted")

 # True
