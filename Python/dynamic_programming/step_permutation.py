def steps(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return steps(n-1) + steps(n-2) + steps(n-3)

def steps_2(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return steps_2(n-1) + steps_2(n-2) + steps_2(n-3)

def memoize_steps(n):
    cache = {0: 0, 1: 1, 2: 2, 3: 4}

    def steps3(num, cache):
        if num <= 0:
            return 0
        if num in cache:
            return cache[num]
        else:
            cache[num] = steps3(num-1, cache) + steps3(num-2, cache) + steps3(num-3, cache)
        return cache[num]

    return steps3(n, cache)


# print(steps(10))
# print(steps_2(30))
print(memoize_steps(100))




# if its 5,
# 3,2
# 1,1,1,1,1
# 2,2,1
# 1,2,2
# 2,3
# 3,1,1
# 1,1,3
# 1, 3, 1


# print(steps(100))

# What is the least number of ways you can get to 100 steps
#