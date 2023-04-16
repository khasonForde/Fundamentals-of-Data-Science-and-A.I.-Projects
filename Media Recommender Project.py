import random
import inquirer
Song_List = ["Myself by Yeat", "Fashion Habits by Ken Carson", "Money Trees by Kendrick Lamar","Kevin's Heart by J.Cole", "Sunshine by Steve Lacy", "Everlong by Foo Fighters", "Suave by Alkaline", "Without Money by Vybz Kartel"]
print("Warning: all songs suggested have non-explicit lyrics!")
Genre_Question = [inquirer.List("Genre Chosen", message = "What is your preferred genre?", choices = ["Trap", "Rap", "Rock", "Dancehall"])]
Genre = inquirer.prompt(Genre_Question)
if "Trap" in Genre["Genre Chosen"] :
  Artist_Question = [inquirer.List("Artist Chosen", message = "Who is your preferred Trap Artist?", choices = ["Yeat", "Ken Carson"] )]
  Artist = inquirer.prompt(Artist_Question)
  if "Yeat" == Artist["Artist Chosen"] : 
    print(f"You should try {Song_List[0]} if you haven't heard it already.")
  elif "Ken Carson" == Artist["Artist Chosen"]: 
    print(f"You should try {Song_List[1]} if you haven't heard it already.")
elif "Rap" == Genre["Genre Chosen"] :
  Artist_Question = [inquirer.List("Artist Chosen", message = "Who is your preferred Trap Artist?", choices = ["Kendrick Lamar", "J.Cole"] )]
  Artist = inquirer.prompt(Artist_Question)
  if "Kendrick Lamar" == Artist["Artist Chosen"] :
    print(f"You should listen to {Song_List[2]} if you haven't heard it as yet.")
  elif "J.Cole" == Artist["Artist Chosen"] : 
    print(f"You should listen to {Song_List[3]} if you haven't heard it as yet.")
elif "Rock" == Genre["Genre Chosen"] :
  Artist_Question = [inquirer.List("Artist Chosen", message = "Who is your preferred Rock Artist?", choices = ["Steve Lacy", "Foo Fighters"] )]
  Artist = inquirer.prompt(Artist_Question)
  if "Steve Lacy" == Artist["Artist Chosen"] :
    print(f"You should listen to {Song_List[4]} if you haven't heard it as yet.")
  elif "Foo Fighters" == Artist["Artist Chosen"] :
    print(f"You should listen to {Song_List[5]} if you haven't heard it as yet.")
elif "Dancehall" == Genre["Genre Chosen"] :
  Artist_Question = [inquirer.List("Artist Chosen", message = "Who is your preferred Dancehall Artist?", choices = ["Alkaline", "Vybz Kartel"] )]
  Artist = inquirer.prompt(Artist_Question)
  if "Alkaline" == Artist["Artist Chosen"] :
    print(f"You should listen to {Song_List[6]} if you haven't heard it as yet.")
  elif "Vybz Kartel" == Artist["Artist Chosen"] :
    print(f"You should listen to {Song_List[7]} if you haven't heard it as yet.")
else:
  print(f"Here is a possibly new song for you to listen to: {random.choice(Song_List)}")
  
  

