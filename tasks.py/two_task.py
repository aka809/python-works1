
def roman_to_int(roman):
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 
        'C': 100, 'D': 500, 'M': 1000
    }
    num = 0
    prev_value = 0
    for char in reversed(roman):
        current_value = roman_map[char]
        if current_value < prev_value:
            num -= current_value
        else:
            num += current_value
        prev_value = current_value
    return num
print(roman_to_int("MMMDXLIX"))  