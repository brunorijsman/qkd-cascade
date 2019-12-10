import copy
import random

class Key:

    def __init__(self):
        """
        Create an empty key.
        """

        self._size = 0
        self._bits = {}  # Bits are stored as dictionary, indexed by index [0..size), value 0 or 1.

    @staticmethod
    def create_random_key(size, seed=None):
        """
        Create an random key.

        Args:
            size (int): The size of the key in bits. Must be >= 0.
            seed(None or int): The seed value for the random number generator for algorithm. Using
                the same seed value is guaranteed to produce the same key. This is intended to
                allow experiments or test cases to be reproduced exactly.

        Returns:
            A new key of the specified size with random bits.
        """

        # Validate arguments.
        assert isinstance(size, int)
        assert size >= 0
        assert seed is None or isinstance(seed, int)

        # Create a new random key.
        # pylint:disable=protected-access
        key = Key()
        key._size = size
        local_random = random.Random(seed)
        for i in range(size):
            key._bits[i] = local_random.randint(0, 1)

        return key

    def __repr__(self):
        """
        Get the unambiguous string representation of the key.

        Returns:
            The unambiguous string representation of the key.
        """
        return "Key: " + self.__str__()

    def __str__(self):
        """
        Get the human-readable string representation of the key.

        Returns:
            The human-readable string representation of the key.
        """
        string = ""
        for i in range(self._size):
            string += str(self._bits[i])
        return string

    @property
    def size(self):
        """
        Get the size of the key in bits.

        Returns:
            The size of the key in bits.
        """
        return self._size

    def get_bit(self, index):
        """
        Get the value of the key bit at a given index.

        Args:
            index (int): The index of the bit. Index must be in range [0, key.size).

        Returns:
            The value (0 or 1) of the key bit at the given index.
        """

        # Validate arguments.
        assert isinstance(index, int)
        assert 0 <= index < self._size

        # Return the bit value.
        return self._bits[index]

    def set_bit(self, index, value):
        """
        Set the value of the key bit at a given index.

        Args:
            index (int): The index of the bit. Index must be in range [0, key.size).
            value (int): The new value of the bit. Must be 0 or 1.
        """

        # Validate arguments.
        assert isinstance(index, int)
        assert 0 <= index < self._size
        assert isinstance(value, int)
        assert value in [0, 1]

        # Set the bit value.
        self._bits[index] = value

    def flip_bit(self, index):
        """
        Flip the value of the key bit at a given index (0 to 1, and vice versa).

        Args:
            index (int): The index of the bit. Index must be in range [0, key.size).
        """

        # Validate arguments.
        assert isinstance(index, int)
        assert 0 <= index < self._size

        # Flip the bit value.
        self._bits[index] = 1 - self._bits[index]

    def copy(self, error_count=0):
        """
        Copy a key and optionally apply noise.

        Args:
            error_count (int): The exact number of bits that are flipped in the copy of the key.

        Returns:
            A new Key instance, which is a copy of this key, with noise applied if asked for.
        """

        # Validate arguments.
        assert isinstance(error_count, int)
        assert 0 <= error_count <= self._size

        # Create a new key which is a copy of this one.
        # pylint:disable=protected-access
        key = Key()
        key._size = self._size
        key._bits = copy.deepcopy(self._bits)

        # Apply noise.
        bits_to_flip = random.sample(self._bits.keys(), error_count)
        for index in bits_to_flip:
            self._bits[index] = 1 - self._bits[index]

        return key

    def difference(self, other_key):
        """
        Return the number of bits that are different between this key and the other_key (also known
        as the Hamming distance).

        Args:
            other_key (Key): The other key that this key has to be compared with. Must be the same
                size as this key.

        Returns:
            The number of bits that are different between this key and the other key.
        """

        # Validate arguments.
        # pylint:disable=protected-access
        assert isinstance(other_key, Key)
        assert self._size == other_key._size

        # Compute difference.
        difference = 0
        for i in range(self._size):
            if self._bits[i] != other_key._bits[i]:
                difference += 1
        return difference
