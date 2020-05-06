def permute(data, i, length):
    if i==length:
        print("".join(data))
    else:
        for j in range(i, length):
            #swap
            data[i], data[j] = data[j], data[i]
            permute(data, i+1, length)
            data[i], data[j] = data[j], data[i]

def find_all_permutation(data, i):
    ### Backtracking Algorithm
    if i == len(data):
        print("".join(data))
    else:
        for j in range(i, len(data)):
            data[i], data[j] = data[j], data[i]
            find_all_permutation(data, i+1)
            data[i], data[j] = data[j], data[i]


def find_all_permutation_2(data, i):
    """Printing the elements"""
    if len(data) == i:
        print("".join(data))
    else:
        for j in range(i, len(data)):
            data[i], data[j] = data[j], data[i]
            find_all_permutation_2(data, i + 1)
            data[i], data[j] = data[j], data[i]

list_of_stuff = []
def find_all_permutation_3(data, i):
    """
    If you need a list of elements
    :param data:
    :param i:
    :return:
    """
    if len(data) == i:
        list_of_stuff.append("".join(data))
    else:
        for j in range(i, len(data)):
            data[i], data[j] = data[j], data[i]
            find_all_permutation_3(data, i + 1)
            data[i], data[j] = data[j], data[i]


string = "abcd"
n = len(string)
data = list(string)
find_all_permutation_3(data, 0)
print(list_of_stuff)


def permutations(string, step = 0):

    # if we've gotten to the end, print the permutation
    if step == len(string):
        print ("".join(string))

    # everything to the right of step has not been swapped yet
    for i in range(step, len(string)):

        # copy the string (store as array)
        string_copy = [character for character in string]

        # swap the current index with the step
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]

        # recurse on the portion of the string that has not been swapped yet (now it's index will begin with step + 1)
        permutations(string_copy, step + 1)



