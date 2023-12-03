
number_dict = {"one" : "1","two" : "2","three" :"3","four" : "4","five" : "5","six" : "6","seven" : "7","eight" : "8","nine" : "9"}
nums_as_words =["one", "two", "three","four", "five", "six", "seven", "eight", "nine"]

important_string="rgxjrsldrfmzq25szhbldzqhrhbjpkbjlsevenseven"


print("left: "+str(left_num)+"\nright: "+str(right_num))


def find_index_num_as_word_left(string_to_search):
    min_index = find_any_index(string_to_search)
    for x in nums_as_words:
        temp_index = string_to_search.find(x)
        if temp_index != -1 and temp_index < min_index:
            min_index = temp_index
            
    return min_index

def find_index_num_as_word_right(string_to_search):
    max_index = find_any_index(string_to_search)
    for x in nums_as_words:
        temp_index = string_to_search.rfind(x)
        if temp_index != -1 and temp_index > max_index:
            max_index = temp_index
            
    return max_index
        
def find_any_index(string_to_search):
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
    
    return [indices[0], indices[-1]]