def is_palindrome(val: int) -> bool:
    """
    Checks if word is the same forwards and backwards
    Takes an integer
    Returns bool
    """

    s = str(val)
    # returns the boolean value of that expression
    return s == s[::-1]


greatest = 0
factor1 = 0
factor2 = 0
# using tow for loops to cover each multiplication
for i in range(100, 1000):
    for j in range(100, 1000):
        val = i * j
        # check if number is a palindrome
        if is_palindrome(val):
            # basic compare
            if val > greatest:
                # print(val)
                greatest = val

                factor1 = i
                factor2 = j

print(f'Größtes Palindrom {factor1} x {factor2} = {greatest}')
