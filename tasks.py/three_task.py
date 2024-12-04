s = input("Enter string s: ")
t = input("Enter string t: ")


def is_subsequence(s, t):
    s_pointer = 0
    for char in t:
        if s_pointer < len(s) and s[s_pointer] == char:
            s_pointer += 1

    return s_pointer == len(s)

result = is_subsequence(s, t)
print(f"Is '{s}' a subsequence of '{t}'? {'True' if result else 'False'}")