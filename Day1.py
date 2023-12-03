INPUT_FILE= open("Day1Input.txt", "r")  #input file from Advent of Code

DIGITS_DICT = {"one" : "1",             #for translating digits written as words, or as
               "two" : "2",             #i call them "literal digits" into normal digits
               "three" :"3",
               "four" : "4",
               "five" : "5",
               "six" : "6",
               "seven" : "7",
               "eight" : "8",
               "nine" : "9"
               }

def get_first_literal_digit(string_to_search):          #finding the first(most left) occurance of a literal digit and return both
    min_index = index_find_any_match(string_to_search)  #index and the literal digit
    if min_index == -1:                                 #if no literal digit is found return -1
        return[-1]
    literal_digit = "null"
    for x in list(DIGITS_DICT.keys()):                  #iterate through the literal digits (list(DIGITS_DICT.keys()) = "one, "two"...)
        temp_index = string_to_search.find(x)           #to find the first occurance
        if temp_index != -1 and temp_index <= min_index:
            min_index = temp_index
            literal_digit = x                           #here the literal digit gets saved together with the index
    
    return [min_index, DIGITS_DICT[literal_digit]]      #return a list with the index and the value

def get_last_literal_digit(string_to_search):          #same here with the last occurance
    max_index = index_find_any_match(string_to_search)
    if max_index == -1:
        return[-1]
    literal_digit= "null"
    for x in list(DIGITS_DICT.keys()):
        temp_index = string_to_search.rfind(x)
        if temp_index != -1 and temp_index >= max_index:
            max_index = temp_index
            literal_digit = x
            
    return [max_index, DIGITS_DICT[literal_digit]]
        
def index_find_any_match(string_to_search):
    count = 0
    any_index = -1
    while any_index == -1 and count < 9:
        any_index = string_to_search.find(list(DIGITS_DICT.keys())[count])
        count += 1
    
    return any_index

def index_digit_left_right(string_to_search):
    indices = []
    for index, value in enumerate(string_to_search):
        if value.isdigit():
            indices.append(index)
    indices.sort()
    if indices == []:
        return [-1]
    return [indices[0], indices[-1]]

def get_left_right(string_results, char_results, input_string):
    if string_results[0][0] == -1:
        return input_string[char_results[0]] + input_string[char_results[1]]
    if char_results[0] == -1:
        return DIGITS_DICT[string_results[0][1]] + DIGITS_DICT[string_results[1][1]]
    if string_results[0][0] < char_results[0]:
        left = DIGITS_DICT[string_results[0][1]]
    else:
        left = input_string[char_results[0]]
    if string_results[1][0] > char_results[1]:
        right = DIGITS_DICT[string_results[1][1]]
    else:
        right = input_string[char_results[1]]
    return left + right


sum = 0
for line in INPUT_FILE:
    sum += int(get_left_right([left_index_literal_digit(line),right_index_literal_digit(line)],index_digit_left_right(line),line))

print(sum)

