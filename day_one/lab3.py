def increment(x):
    return x + 1


val = 10
print(increment(val))


def appendition(some_list):
    print(some_list.append('!'))


some_list = ['a', 'b']
appendition(some_list)

# QUESTION 2


def take_last_element_in_list_and_move_to_the_front(list):
    print(list)
    list[0] = list[-1]
    list.pop()
    return list


mylist = [2, 3, 4, 5, 2, 1, 5]
modified_list = take_last_element_in_list_and_move_to_the_front(mylist)

print(modified_list)


# QUESTION 3
def return_values_at_given_index(list, index1, index2, index3, index4):
    def_tuple = (list[index1], list[index2], list[index3], list[index4])

    return def_tuple


modified_list = return_values_at_given_index(mylist, 2, 3, 4, 1)
print(modified_list)


# QUESTION 4

def return_a_dictionary_of_named_parameters(param1, param2, param3):
    return {param1: "parameter one", param2: "parameter two", param3: "parameter three"}


new_dict = return_a_dictionary_of_named_parameters('any', 'many', 'emany')
print(new_dict)


# QUESTION 5

def accumulator(initial_value, tuple):
    final_value = initial_value

    for num in tuple:
        final_value += num

    return final_value


result = accumulator(0, (1, 3, 5))
print(result)


# QUESTION 6

def fibonacci_sequence_generator():

    user_choice = int(
        input("Enter any number to generate a Fibonacci sequence based on it: "))
    count, first, second = 0, 0, 1
    sequence_list = []

    if (user_choice == 0):
        print("Can't generate a sequence for zero. Please try again")
    else:

        while(count < user_choice):
            # append value to the list
            sequence_list.append(first)
            sum = first + second
            # swapping the first and second values
            first = second
            second = sum
            # incrementing the value of count
            count += 1

        print(sequence_list)


fibonacci_sequence_generator()
