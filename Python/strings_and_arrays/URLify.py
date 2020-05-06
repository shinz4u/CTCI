def URLify(word, total_space):
    print(len(word))
    spaces = 0
    for i in range(total_space):
        if word[i] == " ":
            spaces += 1

    tot_chars_required = total_space + (spaces * 3)

    for i in range(total_space-1, -1, -1):
        if word[i] is " ":
            word[tot_chars_required] = "%20"
        else:
            word[tot_chars_required-1] = word[i]
            tot_chars_required -= 1




name = "Mohammed Shinoy Kavarodi          "
space = 24

# URLify(name, space)

name[0] = "q"
print(name)