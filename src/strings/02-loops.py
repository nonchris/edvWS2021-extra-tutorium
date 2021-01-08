# simple demonstration of all 'three' loop methods (and recursion, 'cause it's cool!)

my_sentence = "Python is really good for beginners, trust me!"

# integrating over this string in four ways, but always with the same result

"""
Best option for a simple, fast iteration over a finite number of itemns
"""
for letter in my_sentence:
    # print(letter)
    pass  # just here to make this file executable without print statement

"""
To demonstrate that a for loop does nothing other than iterating trough an object
and using object[index] until it got all indices covered
Means that 'arrays' is one index and not 'a', 'r', 'a'...
This example uses python lists and no numpy arrays!
Numpy arrays have built-in functionality for iterations so you don't need loops at all!
"""
my_list = ["arrays", "have", "this", "as", "i", "n", "d", "e", "x"]
for letter in my_list:
    # print(letter)  # this shows that 'letter' is just a descriptive name for that variable
    pass  # just here to make this file executable without print statement

"""
Best for iterations over something you can't really count
This example is bad for demonstration, see below for a better one
"""
i = 0
while i < len(my_sentence):
    # print(my_sentence[i])
    i += 1

"""
The best way to iterate over items that have an index!
Especially when aiming only for each n-th item, or comparing things.
"""
for i in range(0, len(my_sentence)):
    # print(my_sentence[i])
    pass

"""
Recursion
The holy grale of avoiding loops
Recursion means that a function calls itself until a break condition is met
"""


def print_val(string, index):
    """
    This function calls itself with an other index
    Each time it prints a number, increases the index
    And calls the same function again
    It needs the word / sentence as string
    And an integer as index
    """
    if index < len(string):
        print(string[index])  # printing string at index
        print_val(string, index + 1)  # calling fucntion with incremented index


# staring recursive function
print_val(my_sentence, 0)

"""
A better for i loop example
Yes, you could do this with a while-loop
But for is more efficient and provides less room for failure
"""
for i in range(len(my_sentence)):
    if i % 2 == 0:
        # print(my_sentence[i] * 2)
        pass
    else:
        # print(my_sentence[i])
        pass

"""
Better while-Loop example
A loop that runs until you write 'Stop, please!'.
"""
word = ""
while word != "stop, please!":
    print("Say something: ")
    word = input()
    if word.lower() == "stop":
        print("Be polite please...")
    elif word == "please":
        print("Way better, but no.")

print("okay, bye")
