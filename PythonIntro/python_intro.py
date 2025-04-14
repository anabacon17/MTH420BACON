# python_intro.py
"""Python Essentials: Introduction to Python.
<Ana Bacon>
<MTH 420>
<04/04/2025>
"""


# Problem 1 (write code below)
if __Ana Bacon__ == "__main__":
    print("Hello, world!")     #Indent with four spaces(NOT a tab).

# Problem 2
def sphere_volume(r):
    """ Return the volume of the sphere of radius 'r'.
    Use 3.14159 for pi in your computation.
    """
    pi=3.14159
    volume = (4/3) * pi * (r**3)
    return volume

if __name__ = "__main__":
    radius = 5
    volume = sphere_volume(radius)
    print(f"The volume of the sphere with radius {radius} is: {volume}")





# Problem 3
def isolate(a, b, c, d, e):
    """ Print the arguments separated by spaces, but print 5 spaces on either
    side of b.
    """
    print(a, ' ' * 5 + b ' ' * 5, c, sep=' ')
    print(d, e)

isolate("Hello", "World", "Python", "is", "great")



# Problem 4
def first_half(my_string):
    """ Return the first half of the string 'my_string'. Exclude the
    middle character if there are an odd number of characters.

    Examples:
        >>> first_half("python")
        'pyt'
        >>> first_half("ipython")
        'ipy'
    """
    length=len(my_string)
    half_index = length // 2
    if length % 2 = 0:
        return my_string[ :half_index]
    else:
        return my_string[ :half_index]
    
def backward(my_string)
    """ Return the reverse of the string 'my_string'.

    Examples:
        >>> backward("python")
        'nohtyp'
        >>> backward("ipython")
        'nohtypi'
    """
    return my_string[ ::-1]

if__name__ == "__main__":
    print(first_half("python"))
    print(first_hald("ipython"))
    
    print(backward("python"))
    print(backward("ipython"))
    

# Problem 5
def list_ops():
    """ Define a list with the entries "bear", "ant", "cat", and "dog".
    Perform the following operations on the list:
        - Append "eagle".
        - Replace the entry at index 2 with "fox".
        - Remove (or pop) the entry at index 1.
        - Sort the list in reverse alphabetical order.
        - Replace "eagle" with "hawk".
        - Add the string "hunter" to the last entry in the list.
    Return the resulting list.

    Examples:
        >>> list_ops()
        ['fox', 'hawk', 'dog', 'bearhunter']
    """
my_list = ["bear", "ant", "cat", "dog"]
print("Initial list:", my_list)

my_list.append("eagle")
print("After appending 'eagle':", my_list)

my_list[2] = "fox"
print("After replacinf index 2 with 'fox':", my_list)

my_list.sort(reverse=True)
print("After sorting in reverse alphabetical order:", my_list)

eagle_index = my_list.index("eagle")
my_list[eagle_index] = "hawk"
print("After replacing 'eagle' with 'hawk':", my_list)

return my_list

if__name__ == "__main__":
    result = list_ops()
    pring("Final results:", result)


# Problem 6
def pig_latin(word):
    """ Translate the string 'word' into Pig Latin, and return the new word.

    Examples:
        >>> pig_latin("apple")
        'applehay'
        >>> pig_latin("banana")
        'ananabay'
    """
    vowels = "aeiou"
    first_letter = word[0].lower()
    
    if first_letter in vowels:
        return word + "hay"
    else: 
        return word[1:] + first_letter + "ay"
    
if __name__ == "__main__":
    print(pig_latin("apple"))
    print(pig_latin("banana"))
    print(pig_latin("cherry"))


# Problem 7
def palindrome():
    """ Find and retun the largest panindromic number made from the product
    of two 3-digit numbers.
    """
    largest_palindrome = 0
    
    for i in range(100, 1000):
        for j in range (i, 1000):
            product = i * j
            if str(product) == str(product)[::-1]:
                if product > largest_palindrome:
                    largest_palidrome = product
    
    return largest_palindrome

if__name__ == "__main__":
    result = palindrome()
    print("The largest palindrome number madre from the product of two 3-digit numbers is:", result)

    
# Problem 8
def alt_harmonic(n):
    """ Return the partial sum of the first n terms of the alternating
    harmonic series, which approximates ln(2).
    """
    terms = [((-1) ** (i + 1)) / i for i in range(1, n+1)]
    return sum(terms)

if __name__ == "__main__":
    n = 500000
    result = alt_harmonic(n)
    print(f"The partial sum of the first {n} terms of the alternating harmonic series is approximately: {result:.5f}")
    
    
