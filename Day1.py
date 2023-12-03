inputFile = open("Day1Input.txt", "r")

number_dict = {"one" : "1",
               "two" : "2",
               "three" :"3",
               "four" : "4",
               "five" : "5",
               "six" : "6",
               "seven" : "7",
               "eight" : "8",
               "nine" : "9"
               }

nums_as_words =["one", "two", "three","four", "five", "six", "seven", "eight", "nine"]

def find_index_num_as_word_left(string_to_search):
    min_index = find_any_index(string_to_search)
    num_as_word = "null"
    for x in nums_as_words:
        temp_index = string_to_search.find(x)
        if temp_index != -1 and temp_index <= min_index:
            min_index = temp_index
            num_as_word = x
    
    return [min_index, num_as_word]

def find_index_num_as_word_right(string_to_search):
    max_index = find_any_index(string_to_search)
    num_as_word = "null"
    for x in nums_as_words:
        temp_index = string_to_search.rfind(x)
        if temp_index != -1 and temp_index >= max_index:
            max_index = temp_index
            num_as_word = x
            
    return [max_index, num_as_word]
        
def find_any_index(string_to_search):
    count = 0
    any_index = -1
    while any_index == -1 and count < 9:
        any_index = string_to_search.find(nums_as_words[count])
        count += 1
    
    return any_index

def smallest_biggest_num_as_char(string_to_search):
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
        return number_dict[string_results[0][1]] + number_dict[string_results[1][1]]
    if string_results[0][0] < char_results[0]:
        left = number_dict[string_results[0][1]]
    else:
        left = input_string[char_results[0]]
    if string_results[1][0] > char_results[1]:
        right = number_dict[string_results[1][1]]
    else:
        right = input_string[char_results[1]]
    return left + right


sum = 0
for line in inputFile:
    sum += int(get_left_right([find_index_num_as_word_left(line),find_index_num_as_word_right(line)],smallest_biggest_num_as_char(line),line))

print(sum)

