import random
from datetime import date

# QUESTION THREE
name = "my name"
age = 100
personality = name + " " + str(age)

print(name)
print(age)
print(personality)


# QUESTION FOUR
# GUESSIN' GAME
rand_num = random.randint(0, 10)
user_input = int(input("Enter any number between 0 and 10: "))

while(rand_num != user_input):
    print("Sorry! Try again")
    user_input = int(input("Enter any number between 0 and 10: "))


if rand_num == user_input:
    print("You got it correct")

print(rand_num, user_input)


# QUESTION FIVE
some_list = [1, 4, 9, 16, 25]
some_tuple = (1, 4, 9, 16, 25)


for num in some_list:
    if (num % 2 == 0):
        print(num)

print("---------")

for anothernum in some_tuple:
    if (anothernum % 2 == 0):
        print(anothernum)


# QUESTION SIX
user_age = int(input("Enter your age: "))
counter = 0
accumulated_age = 0

while (counter <= user_age):
    accumulated_age += counter
    counter = counter + 1


print(accumulated_age, "years, son")


# QUESTION SEVEN

num_of_months = accumulated_age * 12
num_of_days = num_of_months * 30
num_of_hours = num_of_days * 24

print(num_of_months, "months")
print(num_of_days, "days")
print(num_of_hours, "hours")
