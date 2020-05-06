def compute_substring_old(string_to_compute):
    """
    Returns an array of substrings
    """
    if string_to_compute is None or len(string_to_compute) is 0:
        return ""
    if len(string_to_compute) == 1:
        return string_to_compute

    # list to store substrings
    sub_strings = []

    # sliding window
    start = 0
    end = 1
    counter = 1
    while end <= len(string_to_compute):
        counter += 1
        while end <= len(string_to_compute):
            substring = string_to_compute[start:end]
            start += 1
            end += 1
            sub_strings.append(substring)
        start = 0
        end = counter
    return sub_strings


def compute_substring(string_to_compute, length):
    """
    Returns an array of substrings given a length
    """
    if string_to_compute is None or len(string_to_compute) < length:
        return ""

    # list to store substrings
    sub_strings = []

    # sliding window
    start = 0
    end = length
    while end <= len(string_to_compute):
        sub_strings.append(string_to_compute[start:end])
        start += 1
        end += 1
    return sub_strings


strings_to_store = []


def compute_string_recursively(string_to_compute):
    if len(string_to_compute) is 0:
        return ""
    if len(string_to_compute) is 1:
        return string_to_compute
    return compute_string_recursively(string_to_compute[0:-1]), compute_string_recursively(string_to_compute[1:])


# print(compute_string_recursively("abc"))


# print(compute_substring(""))
# print(compute_substring("a"))
# print(compute_substring("abcd"))
# print(compute_substring("qwetyuiopasdfghjkl"))
# print(compute_substring(None))

# print(compute_substring("abcdefgh", 5))
# print(compute_substring("abcdefgh", 10))


def fibonacci_recursion(n):
    """
    Return the n fibonacci numbers
    """
    if n is 0:
        return 0
    if n is 1:
        return 1
    return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)


def memoize(n):
    cache = {0: 0, 1: 1}

    for i in range(n + 1):
        if n in cache:
            return cache[n]
        else:
            cache[n] = cache[n - 1] + cache[n - 2]

    list_to_return = []
    for i in cache:
        list_to_return.append(i)


def fibonaaci_memoize(n):

    cache = {0: 0, 1: 1}

    def memoize_2(num, cache):
        """
        Return the n fibonacci numbers
        """
        if num == 0:
            return num
        if num == 1:
            return num
        if num not in cache:
            cache[num] = memoize_2(num - 1, cache) + memoize_2(num - 2, cache)
        return cache[num]
    memoize_2(n, cache)
    list_to_return = []
    for i in cache:
        list_to_return.append(cache[i])
    return list_to_return

print(fibonaaci_memoize(10))

# print(fibonacci_recursion(100))


















