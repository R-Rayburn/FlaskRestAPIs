### Variables
a = 5
b = 10
my_variable = 56
my_10_variable = 10

string_var = 'hello'
double_string = "python recognizes double and single as string"

#print(my_variable)
#print(string_var)
#print('hello, world!')
#print(123)

### Methods

def my_print_method(my_parameter):
    print(my_parameter)

#my_print_method('buzz')

def my_multiply_method(num_one, num_two):
    return num_one * num_two

result = my_multiply_method(3,7)
my_print_method(result)
my_print_method(my_multiply_method(4,6))

