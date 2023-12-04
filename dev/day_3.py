# Day 3

# # Read height form console
# height = int(input("Enter height: "))

# # check whether person is taller than 120 cm
# if height > 120:
#     # Read age form console
#     age = int(input("Enter age: "))
#     # check if age is less than 5
#     if age < 5:
#         print("You pay a 100$ for bring that crying goop here!")
#     # check if age is >5 and <12
#     elif age >= 5  and age <= 12:
#         print("Alright! We're nice to nice kids! so you pay nothing")
#     # check if age is less than 18
#     elif age < 18:
#         print("Entitled Teenager Alert: Pay 50$! ")
#     # everyone above 18 pays full price 
#     else:
#         print("You're old enough, so pay 10$")

# else:
#     print("Short person disount - A visit to the hospital!! :D")

# 33    
# body_mass_index =10
# print(f"Your BMI is {body_mass_index}, ")
# if body_mass_index < 18.5:
#     print("you are underweight.")
# elif body_mass_index > 18.5 and body_mass_index < 25:
#     print("you have a normal weight.")
# elif body_mass_index >= 25 and body_mass_index < 30:
#     print("you are slightly overweight.")
# elif body_mass_index >= 30 and body_mass_index < 35:
#     print("you are obese.")
# elif body_mass_index >= 35:
#     print("you are clinically obese.")
# else:
#     print("invalid code")

# 34
""" # Which year do you want to check?
year = int(input("Year: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

if year % 4 == 0:
  if year % 100 !=0:
      print("Leap year")
  elif year % 100 == 0 and year % 400 == 0:
      print("Leap year")
  else:
    print("Not leap year")
else:
  print("Not leap year") """

# # 36
# print("Thank you for choosing Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L \n") # 
# add_pepperoni = input("Do you want pepperoni? Y or N \n") # 
# extra_cheese = input("Do you want extra cheese? Y or N \n") # 
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇
# price = 0

# if size == "L":
#     price = 25
#     if add_pepperoni == "Y":
#         price += 3
# elif size == "M":
#     price = 20
#     if add_pepperoni == "Y":
#         price += 3
# elif size == "S":
#     price = 15
#     if add_pepperoni == "Y":
#         price += 2

# if extra_cheese == "Y":
#     price += 1

# print(f"Your final bill is: ${price}.")

# 38

print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

string_to_check_1 = "TRUE"
string_to_check_2 = "LOVE"
true_score = 0
love_score = 0
combined_name = name1 + name2
combined_name = combined_name.lower()

for character in string_to_check_1.lower():
    count = combined_name.count(character)
    # print(f"{character} occurs {count} times")
    true_score += count

for character in string_to_check_2.lower():
    count = combined_name.count(character)
    # print(f"{character} occurs {count} times")
    love_score += count

score = true_score * 10 + love_score

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
   print(f"Your score is {score}, you are alright together.")
else:
   print(f"Your score is {score}.")
  