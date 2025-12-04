# File: EnigmaRotor.py
# """This module defines the EnigmaRotor class for the Enigma simulator."""

class EnigmaRotor:
    def __init__(self, permutation):
        """Initializes a rotor with its permutation and sets offset to 0."""
        self._permutation = permutation
        self._offset = 0

    def get_offset(self):
        """Returns the current offset (0–25)."""
        return self._offset

    def get_permutation(self):
        """Returns the permutation string for this rotor."""
        return self._permutation

    def advance(self):
        """Advances the rotor by one position, cycling after 25."""
        self._offset = (self._offset + 1) % 26
