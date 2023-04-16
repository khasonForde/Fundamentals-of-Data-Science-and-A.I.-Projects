import random
##ASK USER NAME
username = print("Hi, my name is speed.")
print()
username = input("What is your name: ").title()
print()
##ASK FIRST QUESTION - FAVOURITE ITEM
#Lowercase user answer
user_sport = input(f"Nice to  meet you {username}! What is your favourite sport: ").lower()
print()
#Get random chatbot answer
sport_list = ["soccer", "football", "basketball", "tennis", "rugby"]
speed_sport = random.choice(sport_list)
#Compare user answer to chatbot answer
if user_sport in sport_list:
  print("thats my favourite sport too! We should watch a game/match sometime!")
  print()
if user_sport not in sport_list:
  if user_sport[0] == "b":
    print(f"Thats good, but I prefer {speed_sport}.")
  else:
    print(f"Thats good, but I prefer {speed_sport}.")
    print()
##SECOND QUESTION - COUNTABLE ITEM
#Lowercase user answer
user_has_pets = input("Do you have any pets: ").lower()
print()
#Get random chatbot answer
pet_list = ["dogs", "cats", "guinea pigs", "birds", "fishes"]
speed_pet = random.choice(pet_list)
speed_number_of_pets = random.randint(1,7)
#Compare user answer to chatbot answer
if speed_number_of_pets == 1 and speed_pet[-1] == "s":
  speed_pet = speed_pet[:-1]
if "yes" in user_has_pets or "y" in user_has_pets:
  print(f"AHHHH! I also have pets! I have {speed_number_of_pets} {speed_pet}")
  print()
  user_pet = input("What pets do you have: ")
  print()
  if pet_list[0] in user_pet:
    print("I love dogs! My aunt is actually a vet")
    print()
  elif pet_list[1] in user_pet:
    print("I love cats! My aunt is actually a vet.")
    print()
  elif pet_list[2] in user_pet:
    print("I love guinea pigs! My aunt is actually a vet.")
    print()
  elif pet_list[3] in user_pet:
    print("I love birds! My aunt is actually a vet.")
    print()
  elif pet_list[4] in user_pet:
    print("I love fishes! My aunt is actually a vet.")
    print()
##ASK THIRD QUESTION - RATING OR NUMBER
#Lowercase user answer
user_hobby = input("What is your favorite hobby: ")
print()
user_level = float(input(f"I see! On a scale of 1 to 10, how good would you say you are at {user_hobby}: "))
print()
#Get random chatbot answer
speed_level = random.randint(1,10)
#Compare user answer to chatbot answer
if speed_level > user_level:
  print(f"Nice! You're better at {user_hobby} than me.")
  print()
elif speed_level < user_level:
  print(f"Ahhh you're not bad at {user_hobby}, but I'm better!")
  print()
elif speed_level == user_level:
  print(f"We're pretty much the same level at {user_hobby}.")
  print()
##SAY GOODBYE
print(f"It was nice chatting with you, {username}. Goodbye!")
