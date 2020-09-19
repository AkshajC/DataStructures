s = "sdax ixs xcool "
# x = 0
# for letter in s:
#    if letter == "x":
#        x += 1
# s = s.replace("x", "")
# s = s + x * "x"
# print(s)
x = 0


def push_back(string, character):
    global x
    if character in string:
        for letter in string:
            if letter == character:
                x += 1
                string = string.replace(character,"", 1)
                push_back(string, character)
    else:
        print(x)
        return (string + x * character)


push_back(s, "")
