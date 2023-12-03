inputFile = open("/home/leo/Documents/AdventOfCode/2023/Day1Input.txt", "r")

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

sum = 0
all_digits = ""
number_as_string = ""
first_last_digit = ""

for line in inputFile:
    for x in line:
        if x.isdigit():
            all_digits += x
        else:
            number_as_string += x
            if number_as_string in number_dict:
                all_digits += number_dict[number_as_string]
                number_as_string = ""
    number_as_string = ""
    
    first_last_digit = all_digits[0] + all_digits[-1]
    print(first_last_digit)
    sum += int(first_last_digit)
    first_last_digit = ""
    all_digits = ""

print(sum)

