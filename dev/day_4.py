import random as rd

# num_to_print = rd.randint(4,14) + rd.random()

# if num_to_print >= 0 and num_to_print <= 5:
#     print(num_to_print)
# else:
#     print(f"Error generating number.{num_to_print} is not in range")

coin_value = rd.randint(0,1)

if coin_value == 1:
    print("Heads")
else:
    print("Tails")

rd.