# Methods that check whether a word contains all unique letters.


def bit_array(word):
    '''
    Using Bit Array of 128 for ASCII characters and checking if item already exixts
    '''
    word = clean_string(word)
    a = [None] * 128
    for i in word:
        ascii = ord(i)
        if a[ascii] is None:
            a[ascii] = 1
        else:
            return False, f"{i} is repeated in "
    return True

def is_unique(word):
    '''
    Using dictionaries O(n) time complexity
    '''
    word = clean_string(word)
    print(word)
    a_dict = {}
    for i in word:
        if i not in a_dict:
            a_dict[i] = 1
        else:
            return False, f"{i} is repeating"
    return True

def is_unique_without_datastructures(word):
    """
    Using array traversal O(n^2) time complexity
    """
    word = clean_string(word)
    print(word)
    word_length = len(word)
    for i in range(word_length):
        for j in range(i+1, word_length):
            if word[i] == word[j]:
                return False, f"{word[i]} is repeating"
    return True

def clean_string(word):
    a = word
    a = a.lower()
    a = "".join(a.split(" "))
    return a

# Testing the methods out

print("\n\nIn first method")
print(bit_array("Shinoy"))
print(bit_array("Mohammed"))
print(bit_array("Python is awesome"))

print("\nIn second method")
print(is_unique("Shinoy"))
print(is_unique("Mohammed"))
print(is_unique("Python is awesome"))


print("\n\nIn third method")
print(is_unique_without_datastructures("Shinoy"))
print(is_unique_without_datastructures("Mohammed"))
print(is_unique_without_datastructures("Python is awesome"))

