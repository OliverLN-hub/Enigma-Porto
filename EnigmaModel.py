# File: EnigmaModel.py

from EnigmaView import EnigmaView
from EnigmaRotor import EnigmaRotor
from EnigmaRotor import apply_permutation_forward, apply_permutation_backward
from EnigmaConstants import ROTOR_PERMUTATIONS, REFLECTOR_PERMUTATION


# Supporter functions to make conversion easier
def letter_to_index(letter):
    return ord(letter) - ord('A')

def index_to_letter(index):
    return chr(ord('A') + index)


class EnigmaModel:
    # Initializes the Enigma model
    def __init__(self):
        self._views = []

        # Checks the state of the buttons on the Enigma keyboard
        self._key_states = {chr(i): False for i in range(ord('A'), ord('Z') + 1)}

        # Checks the state of the lamps on the Enigma lampboard
        self._lamp_states = {chr(i): False for i in range(ord('A'), ord('Z') + 1)}

        # Create three rotors using the permutations defined in EnigmaConstants
        self._rotors = [EnigmaRotor(p) for p in ROTOR_PERMUTATIONS]

    # Adds a view to the list of views
    def add_view(self, view):
        self._views.append(view)

#   Sends an update request to all the views.
    def update(self):
        for view in self._views:
            view.update()

    def is_key_down(self, letter):
        return self._key_states.get(letter, False)

    def is_lamp_on(self, letter):
        return self._lamp_states.get(letter, False)


    def key_pressed(self, letter):
        fast = self._rotors[2]     # right rotor
        medium = self._rotors[1]  # middle rotor
        slow = self._rotors[0]   # left rotor

        # Advances the fast/right rotor. If it wraps around, advance the medium rotor, if that also the continue to slow rotor
        carry = fast.advance()
        if carry:
            carry2 = medium.advance()
            if carry2:
                slow.advance()

        # converts the pressed to an index 0-25
        index = letter_to_index(letter)

        # Forward (right -> left)
        for rotor in reversed(self._rotors):
            index = apply_permutation_forward(
                index,
                rotor.get_forward_permutation(),
                rotor.get_offset()
            )

        # Find reflected letter and convert it from A to Z and back to a 0-25 index
        index = ord(REFLECTOR_PERMUTATION[index]) - ord('A')

        # Backward (left to right)
        for rotor in self._rotors:
            index = apply_permutation_backward(
                index,
                rotor.get_backward_permutation(),
                rotor.get_offset()
            )

        # Convert index -> letter and light that lamp
        encrypted_letter = index_to_letter(index)
        self._lamp_states[encrypted_letter] = True

        self.update()


    def key_released(self, letter):
        self._key_states[letter] = False

        # Turn off ALL lamps when any key is released
        for L in self._lamp_states:
            self._lamp_states[L] = False

        self.update()

    # Returns the letter showing on rotor <index>
    def get_rotor_letter(self, index):
        rotor = self._rotors[index]
        offset = rotor.get_offset()
        return index_to_letter(offset)
    
    # Returns the offset (0-25) of rotor <index>
    def rotor_clicked(self, index):
        self._rotors[index].advance()
        self.update()


def enigma():
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)


# Startup code
if __name__ == "__main__":
    enigma()
