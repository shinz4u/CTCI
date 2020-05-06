

# a = {1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 8, 9, 10}
a = {1,2,3,4}

# {1} {2} {3} {4} {1,2} {1,3} {1,4} {2,3} {2,4} {3,4} {1,2,3} {2,3,4} {1,3,4} {1,2,4} {1,2,3,4}

print(a)
a = list(a)
print(a)
some_list = []
def powerset(a):
    if len(a) is 0:
        return []
    elif len(a) is 1:
        return [[a[0]], []]
    elif len(a) is 2:
        return [[], [a[0]], [a[1]], [a[0]], a[1]]
    else:
        a = powerset(a[:-1])
        to_add = []
        for i in a:
            a[n]

        some_list.append(powerset(a[1:]))


def basic(a):
    for i in a:
        for j in a:
            pass
powerset(a)

print(some_list)




a = {1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 8, 9, 10}