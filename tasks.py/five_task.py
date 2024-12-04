input_strings = input("Enter a list of strings separated by commas: ").split(',')
def longest_common_prefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    for string in strs[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
input_strings = [s.strip() for s in input_strings]
result = longest_common_prefix(input_strings)
print(f"The longest common prefix is: '{result}'")