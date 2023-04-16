import random 
import os
import time
from stringcolor import cs
player_names = []
categories = ["Naruto Shippuden","Bleach","One Piece","Dragon Ball Z" ]
vowel_list = ["a", "e", "i", "o","u"]
countdown = [3,2,1,"Go"]
score = [0,0]
time_limit = 10

print(cs("LIGHTNING ROUND\n","blue"))

time.sleep(2)

print(cs("You have 10 seconds to answer each question from 4 Animes. If you answer incorrectly, your turn will be over.","blue"))

time.sleep(3)

for i in range(2):
  player_name = input(f"\nPlayer {i+1}, please enter your name: ")
  print(cs(f"\nWelcome to Anime Lightning Round {player_name}!","blue"))
  time.sleep(2)
  player_names.append(player_name)
  
os.system("clear")

random.shuffle(player_names)
  
for i in range(len(player_names)):
  print(cs(f"{player_names[i]}, get ready!","blue"))
  time.sleep(3)
  os.system("clear")
  
  for h in range(len(countdown)):
    print(cs(countdown[h],"blue"))
    print()
    time.sleep(2)
    
  os.system("clear")
  random.shuffle(categories)
  
  for j in range(len(categories)):
    
    random_vowel = random.choice(vowel_list)
    
    print(cs(f"First name of a character in {categories[j]} whose name contains the vowel {random_vowel}.\n","blue"))
    
    start = time.time()
    answer = input(cs("Enter character: ","blue"))
    end = time.time()
    
    timer = end - start
    
    os.system("clear")

    if random_vowel in answer:
      
      if timer <= time_limit:
        print(cs("Nice! you scored 10 points!\n","green"))
        time.sleep(3)
        score[i] += 10
        print(cs(f"Current Score: {score[i]}","blue"))
        time.sleep(3)
        os.system("clear")
        
      else:
        print(cs(f"You did not answer with in the {time_limit} second time limit.\n","maroon"))
        time.sleep(3)
        print(cs(f"Current Score: {score[i]}","blue"))
        time.sleep(3)
        os.system("clear")
        continue
        
    else:
      print(cs(f"That character's name does contain the vowel {random_vowel}.\n","maroon"))
      time.sleep(3)
      print(cs(f"Your final score is {score[i]}","blue"))
      time.sleep(3)
      os.system("clear")
      break

if score[0] > score[1]:
  print(cs(f"{player_names[0]} is the winner!","blue"))
  time.sleep(2)
elif score[0] < score[1]:
  print(cs(f"{player_names[1]} is the winner!","blue"))
  time.sleep(2)
else:
  print(cs("The final scores were tied!", "blue"))
  time.sleep(2)
  
os.system("clear")

print(cs(f'''Final Score:

{player_name[0]}: {score[0]}

{player_name[1]}: {score[1]} ''',"blue"))
