# File: EnigmaModel.py

""" This is the starter file for the Enigma project. """
from EnigmaView import EnigmaView
from EnigmaRotor import EnigmaRotor
from EnigmaConstants import ROTOR_PERMUTATIONS

class EnigmaModel:

    def __init__(self):
        """Creates a new EnigmaModel with no views."""
        self._views = [ ]

        self._key_states = {chr(i): False for i in range(ord('A'), ord('Z') + 1)}
        self._lamp_states = {chr(i): False for i in range(ord('A'), ord('Z') + 1)}

        # Create three rotors using the permutations defined in EnigmaConstants
        self._rotors = [EnigmaRotor(p) for p in ROTOR_PERMUTATIONS]

    def add_view(self, view):
        """Adds a view to this model."""
        self._views.append(view)

    def update(self):
        """Sends an update request to all the views."""
        for view in self._views:
            view.update()

    def is_key_down(self, letter):
        return self._key_states.get(letter, False)

    def is_lamp_on(self, letter):
        return self._lamp_states.get(letter, False)

    def key_pressed(self, letter):
        self._key_states[letter] = True
        self._lamp_states[letter] = True  #light up the same lettter for which key has been decided to press
        self.update()

    def key_released(self, letter):
        self._key_states[letter] = False
        self._lamp_states[letter] = False  #turn off the lamp when key is released
        self.update()

    def get_rotor_letter(self, index):
        rotor = self._rotors[index]
        offset = rotor.get_offset()
        return chr(ord('A') + offset)

    def rotor_clicked(self, index):
        self._rotors[index].advance()
        self.update()

def enigma():
    """Runs the Enigma simulator."""
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

# Startup code

if __name__ == "__main__":
    enigma()
