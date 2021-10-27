from decimal import Decimal

# QUESTION 5
# Write down the types of the following expressions:
# Expression	Type	Verified Type
# 5
# 5000 * 50000000
# 'j'
# 1j
# (l,)
# [1]
# None

num_1 = 5
num_2 = 5000 * 50000000
num_3 = 'j'
num_4 = 1j
num_5 = (1, )
num_6 = [1]
num_7 = None


print(type(num_1))
print(type(num_2))
print(type(num_3))
print(type(num_4))
print(type(num_5))
print(type(num_6))
print(type(num_7))


# QUESTION 6

result_1 = 0.1 + 0.1 + 0.1
result_2 = Decimal(".1") + Decimal(".1") + Decimal(".1")

print(result_1)
print(result_2)


# QUESTION 7
# fibonacci sequence
limit = 20
count, first, second = 0, 0, 1

while (count <= limit):
    print(first)
    # calculate the next value
    sum = first + second
    # swap the values of first and second
    first = second
    second = sum
    count += 1


# QUESTION 8
mood = "Charlie"

print(mood.isnumeric)
print(mood.isprintable)
print(mood.count)
print(mood.format_map)
print(mood.strip)
print(mood.upper)

print(mood[-1])

for letter in mood:
    if (letter == mood[-1]):
        print(letter, end="")
    else:
        print(letter+":", end="")


# QUESTION 9
count = 0

user_prompt = input(
    "Enter any 10 numbers between 1 and 8 separated by a comma: \n")
numbers_list = user_prompt.split(",")

print(numbers_list)

for num in numbers_list:
    if (int(num) == 5):
        count += 1

print("You entered the number '5'", count, "times")


# QUESTION 10
another_list = [1, 4, 9, 16, 25]

# using list comprehension to filter out all odd numbers
new_list = [num for num in another_list if num % 2 == 0]

print(another_list)
print(new_list)
