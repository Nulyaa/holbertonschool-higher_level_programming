#!/usr/bin/python3
"""
This module defines a class Square with size and position attributes.
"""

class Square:
    """A class that defines a square with its size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the square.

        Args:
            size: The size of the square.
            position: A tuple of two integers representing the position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            if all(isinstance(i, int) for i in value) and all(i >= 0 for i in value):
                self.__position = value
            else:
                raise TypeError("position must be a tuple of 2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 integers")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")  # Just print an empty line if the square's size is 0
        else:
            # Print the vertical space (y-offset) first
            for _ in range(self.__position[1]):
                print()
            # Print the square, each row prefixed with horizontal space (x-offset)
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
