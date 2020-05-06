# Tower of Hanoi

def hanoi1(n, source, helper, target):
    if n > 0:
        # move tower of size n - 1 to helper:
        hanoi1(n - 1, source, target, helper)
        # move disk from source peg to target peg
        if source:
            target.append(source.pop())
        # move tower of size n-1 from helper to target
        hanoi1(n - 1, helper, source, target)


def hanoi2(n, source, target, helper):
    if n <= 0:
        if source:
            target.append(source.pop())
    else:
        # move tower of size n - 1 to helper:
        hanoi2(n - 1, source, helper, target)
        # move disk from source peg to target peg
        if source:
            target.append(source.pop())
        # move tower of size n-1 from helper to target
        hanoi2(n - 1, helper, target, source)


source = [3, 2, 1]
target = []
helper = []
hanoi2(len(source), source, helper, target)

print(source, helper, target)