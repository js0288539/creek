# Think Python 2e
# Exercise 8.5

# (Version of code that only works with lowercase letters)
#def rotate_word(s,x):
#    rotate_string = ""
#    lower_alpha = "abcdefghijklmnopqrstuvwxyz"
#    upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#
#    for c in s:
#        c_element = ord(c) - ord('a')
#        rot_element = c_element + x
#        if rot_element >= 26:
#            rot_element = rot_element - 26
#        rotate_string = rotate_string + lower_alpha[rot_element]
#
#    return rotate_string

def rotate_word(s,x):
    rotate_string = ""
    lower_alpha = "abcdefghijklmnopqrstuvwxyz"
    upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for c in s:
        if c.islower():
            c_element = ord(c) - ord('a')
            rot_element = c_element + x
            if rot_element >= 26:
                rot_element = rot_element - 26
            rotate_string = rotate_string + lower_alpha[rot_element]
        else:
            c_element = ord(c) - ord('A')
            rot_element = c_element + x
            if rot_element >= 26:
                rot_element = rot_element - 26
            rotate_string = rotate_string + upper_alpha[rot_element]

    return rotate_string
