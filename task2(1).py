def character_occurance(input_str):
    """
    :param input_str: string characters
    :return: True or False based on certain conditions
    """
    a_occurred = False
    b_occurred = False
    for element in input_str:
        if element == 'a':
            if b_occurred:
                return False
            else:
                a_occurred = True
        elif element == 'b':
            b_occurred = True

    result = a_occurred or b_occurred
    return result



# Test cases
test_cases = ["aaaaaaa", "aaabbbb", "aaaaba", "bbb", "bbbbaaaa","aba","cba","cab","","ca"]

for s in test_cases:
    result = character_occurance(s)
    print(f"String: '{s}' -> Result: {result}")