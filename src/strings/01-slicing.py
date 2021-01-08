# slicing strings vs numpy-arrays

import numpy as np

ship = "Rheinchifffahrt"

#  Slicing has always the same syntax:
#  [start : end : steps]
#  index/ start begins with zero
#  steps can be negative

#  fix typo in variable ship
fist_part = ship[:5]        # indices 0 to 4
second_part = ship[5:]      # indices 5 to end

# note that the old value of ship is overwritten
ship = fist_part + 's' + second_part

print(ship)


# creating numpy array from 0 to 10, steps = 2
# note that we use 0 and 11 to do that (12 would also work)
array = np.arange(0, 11, 2)
print(array)
print()

# slicing is identical...
ship_slice = ship[5: len(ship)]  # len() isn't needed

part = array[2: array.size]  # array.size not needed, len(array) would be bad practice!

print(ship_slice)
print(part)

# ...but modifying data os different...
# ship_slice[0] = "S"  # raises a TypeError
part[0] = 42  # works fine

print(part)
print()

# ...'out of range' slicing behave the same way again.
# backward slicing
strange_ship = ship[-5:]  # last five letters

strange_array = array[-5:]  # last five numbers

print(ship)
print(strange_ship)
print(array)
print(strange_array)

# bot raise IndexError when going over max index
# ship[len(ship) + 1]  # raises error
# array[array.size + 1]  # raises error