# python_intro.py
"""Python Essentials: Introduction to Python.
<Ana Bacon>
<MTH 420>
<04/04/2025>
"""


# Problem 1 (write code below)


# Problem 2
def sphere_volume(r):
    """ Return the volume of the sphere of radius 'r'.
    Use 3.14159 for pi in your computation.
    """

# Problem 3
def isolate(a, b, c, d, e):
    """ Print the arguments separated by spaces, but print 5 spaces on either
    side of b.
    """
    print(a, b, c, sep="     ", end=" ")
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
    if length % 2 == 0:
        return my_string[ :half_index]
    else:
        return my_string[ :half_index]
    
def backward(my_string):
    """ Return the reverse of the string 'my_string'.

    Examples:
        >>> backward("python")
        'nohtyp'
        >>> backward("ipython")
        'nohtypi'
    """
    return my_string[ ::-1]


    

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



    
# Problem 8
def alt_harmonic(n):
    """ Return the partial sum of the first n terms of the alternating
    harmonic series, which approximates ln(2).
    """
    terms = [((-1) ** (i + 1)) / i for i in range(1, n+1)]
    return sum(terms)


    
    
if __name_ == "__main__":
    print("Hello, world!")     #Indent with four spaces(NOT a tab).
    
    
return (4/3) * 3.14159 r ** 3

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    