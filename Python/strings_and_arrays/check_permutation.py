# To check If one string is a permutation of the other

def permutation_check_dict(word1, word2):
    word1_dict = {}
    word2_dict = {}

    for i in word1:
        if i in word1_dict:
            word1_dict[i] = word1_dict[i] + 1
        else:
            word1_dict[i] = 1

    for i in word2:
        if i in word2_dict:
            word2_dict[i] = word2_dict[i] + 1
        else:
            word2_dict[i] = 1

    if word1_dict == word2_dict:
        return True
    else:
        return False

def permutation_check_sort(word1, word2):
    """
    In this method the two words are sorted and then checked for equality.
    Takes O(log n) time each for sorting and then O(1) time for sorting
    """

    word1 = sorted(word1)
    word2 = sorted(word2)

    if word1 == word2:
        return True
    else:
        return False

a = "something"
b = "thingsome"

c = "dad"
d = "add"

e = "some thing"
f = "thingsome"

print(permutation_check_dict(a,b))
print(permutation_check_dict(c,d))
print(permutation_check_dict(e,f))

print(permutation_check_dict(a,c))

print(permutation_check_sort(a,b))
print(permutation_check_sort(c,d))
print(permutation_check_sort(e,f))

print(permutation_check_sort(a,c))

