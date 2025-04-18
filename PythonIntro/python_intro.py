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
    return (4/3) * 3.14159 * r**3

# Problem 3
def isolate(a, b, c, d, e):
    """ Print the arguments separated by spaces, but print 5 spaces on either
    side of b.
    """
    print(a, b, c, sep="     ", end=" ")
    print(d, e)
    



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
    half_index=len(my_string) // 2
    return my_string[:half_index]
    
def backward(my_string):
    """ Return the reverse of the string 'my_string'.

    Examples:
        >>> backward("python")
        'nohtyp'
        >>> backward("ipython")
        'nohtypi'
    """
    return my_string[::-1]


    

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

    my_list.append("eagle")

    my_list[2] = "fox"
    
    my_list.pop(1)

    my_list.sort(reverse=True)
    
    bird_index = my_list.index("eagle")
    
    my_list[bird_index] = "hawk"
    
    my_list[-1] += "hunter"

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
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    if word[0] in vowels:
        return word + "hay"
    else: 
        return word[1:] + word[0] + "ay"
    



# Problem 7
def palindrome():
    """ Find and retun the largest panindromic number made from the product
    of two 3-digit numbers.
    """
    largest_palindrome = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            if str(product) == str(product)[::-1]:
                if product > largest_palindrome:
                    largest_palindrome = product
    return largest_palindrome

    
# Problem 8
def alt_harmonic(n):
    """ Return the partial sum of the first n terms of the alternating
    harmonic series, which approximates ln(2).
    """
    terms = [((-1) ** (i + 1)) / i for i in range(1, n+1)]
    return sum(terms)


    
    
if __name__ == "__main__":
    print("Hello, world!")     #Indent with four spaces(NOT a tab).
    
    
    r=3
    print(sphere_volume(r))
    
    isolate('a', 'b', 'c', 'd', 'e')
    
    my_string="Python"
    print(first_half(my_string))
    print(backward(my_string))
    
    print(list_ops())
    
    print(pig_latin("apple"))
    print(pig_latin("banana"))

    print(palindrome())
    
    
    
    print(alt_harmonic(500000))
    
    
    
    
    
    
    