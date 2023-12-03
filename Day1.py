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
    min_index = get_any_literal_digit(string_to_search)  #index and the literal digit
    if min_index == -1:                                 #if no literal digit is found return -1
        return[-1,"null"]
    literal_digit = "null"
    for x in list(DIGITS_DICT.keys()):                  #iterate through the literal digits (list(DIGITS_DICT.keys()) = "one, "two"...)
        temp_index = string_to_search.find(x)           #to find the first occurance
        if temp_index != -1 and temp_index <= min_index:
            min_index = temp_index
            literal_digit = x                           #here the literal digit gets saved together with the index
    
    return [min_index, DIGITS_DICT[literal_digit]]      #return a list with the index and the value

def get_last_literal_digit(string_to_search):           #same here with the last occurance
    max_index = get_any_literal_digit(string_to_search)
    if max_index == -1:
        return[-1,"null"]
    literal_digit= "null"
    for x in list(DIGITS_DICT.keys()):
        temp_index = string_to_search.rfind(x)
        if temp_index != -1 and temp_index >= max_index:
            max_index = temp_index
            literal_digit = x
            
    return [max_index, DIGITS_DICT[literal_digit]]
        
def get_any_literal_digit(string_to_search):             #function to find any occurance of a literal digit and return its index
    count = 0
    any_index = -1
    while any_index == -1 and count < 9:
        any_index = string_to_search.find(list(DIGITS_DICT.keys())[count])
        count += 1
    
    return any_index

def get_first_last_normal_digit(string_to_search):      #returns the index and value of the first and the last occurance of a normal digit("1","2","3"...)
    indices = []
    for index, value in enumerate(string_to_search):
        if value.isdigit():
            indices.append(index)
    indices.sort()
    if indices == []:
        return [[-1],[-1]]                                     #if nothing is found return -1
    return [[indices[0],string_to_search[indices[0]]],[indices[-1],string_to_search[indices[-1]]]]

def get_line_result(literal_digits, normal_digits):
    if literal_digits[0][0] == -1:
        return int(normal_digits[0][1] + normal_digits[1][1])   #when no literal digits are present return the first and last normal digit
    if normal_digits[0][0] == -1:
        return int(literal_digits[0][1] + literal_digits[1][1])  #same thing just the opposite
    if literal_digits[0][0] < normal_digits[0][0]:               #comparing indices of the occurances of the literal and normal digits
        first = literal_digits[0][1]
    else:
        first = normal_digits[0][1]
    if literal_digits[1][0] > normal_digits[1][0]:              #comparing indices of the occurances of the literal and normal digits
        last = literal_digits[1][1]
    else:
        last = normal_digits[1][1]
    return int(first + last)


sum = 0
for line in INPUT_FILE:
    sum += get_line_result([get_first_literal_digit(line),get_last_literal_digit(line)],get_first_last_normal_digit(line))

print(sum)

