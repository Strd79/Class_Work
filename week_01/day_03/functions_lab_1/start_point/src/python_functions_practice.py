def return_10():
    return 10

def add(num_1, num_2):
    return num_1 + num_2

add(1,2) 

def subtract(num_1, num_2):
    return num_1 - num_2

subtract(10,5)

def multiply(num_1, num_2):
    return num_1 * num_2

multiply(4,2)

def divide(num_1, num_2):
    return num_1 / num_2

divide(10,2)

string = "A string of length 21"

def length_of_string(test_string):
    return len(test_string)

length_of_string(string)

string_1 = "Mary had a little lamb, "
string_2 = "its fleece was white as snow"

def join_string(str_a, str_b):
    return str_a + str_b

join_string(string_1, string_2)

def add_string_as_number(str_a, str_b):
    return int(str_a) + int(str_b)

add_string_as_number("1", "2")

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def number_to_full_month_name(index):
    return months[index-1]

number_to_full_month_name(1)  
number_to_full_month_name(3)
number_to_full_month_name(9)

def number_to_short_month_name(index):
    return months[index-1][0:3]

number_to_short_month_name(1)
number_to_short_month_name(4)
number_to_short_month_name(10)

def volume_of_cube(side_length):
    return side_length**3

volume_of_cube(5)

string_2 = "Hello Cam and David"

def reverse_string(string):
    return string[::-1]

reverse_string(string_2)