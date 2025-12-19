# File: EnigmaRotor.py

#  Invert a rotor permutation so that we can go backwards through it
def invert_key(permutation):
    inverse = [''] * 26
    for i, ch in enumerate(permutation):
        idx = ord(ch) - ord('A')   #Get the encrypted letter
        inverse[idx] = chr(ord('A') + i) #Map back to the original letter
    return ''.join(inverse)

#Class EnigmaRotor that we call upon in the EnigmaModel.py
class EnigmaRotor:
    def __init__(self, permutation):
        self._forward_permutation = permutation
        self._backward_permutation = invert_key(permutation)
        self._offset = 0

    #Returns the current offset (0–25). used when applying the rotor permutation
    def get_offset(self):
        return self._offset
    # returns the forward permutation string
    def get_forward_permutation(self):
        return self._forward_permutation
    # returns the backward permutation string
    def get_backward_permutation(self):
        return self._backward_permutation

    # Return True if wrapped around from Z then back to A, rerutns a boolean TRUE if thats the case
    def advance(self):
        self._offset = (self._offset + 1) % 26
        return self._offset == 0  
    
    def set_offset(self, offset: int):
        self._offset = offset % 26



#   applies a rotor permutation in a forward direction, also taking the offset into account
def apply_permutation_forward(index, permutation, offset):
    shifted_index = (index + offset) % 26  # the rotor is "rotated" so the index is shifted by the offset, and then gets the permutation applied
    # Apply the permutation mapping
    permuted_char = permutation[shifted_index]
    permuted_index = ord(permuted_char) - ord('A')
    # undo the shidt after the permutation
    final_index = (permuted_index - offset) % 26
    return final_index

def apply_permutation_backward(index, permutation, offset):
    shifted_index = (index + offset) % 26
    permuted_char = permutation[shifted_index]
    permuted_index = ord(permuted_char) - ord('A')
    final_index = (permuted_index - offset) % 26
    return final_index
    