# # make foods list
# foods_list = ["kebab", "chicken", "pizza", "sandwich", "cheese burgur"]
# print(foods_list)

# # add new food to the list
# foods_list.append("pasta")
# print(foods_list)

# # remove 3rd food of list
# foods_list.remove(foods_list[2])
# print(foods_list)

# print("====================================================")

# [================ Factorial ================]

number = int(input("Enter your number: "))
factorial = number

for i in range(1, number):
  factorial *= (number - i)

print(factorial)