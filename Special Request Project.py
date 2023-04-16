##GETTING USER INPUT
recipient_name = input("Enter the recipient's name: ").title()
recipient_city = input("Enter the recipient's city: ").title()
mutual_friend_name = input("Enter mutual friend (optional:press enter if no mutual friend): ").title()
friendliness_level = int(input("Enter your letter's friendliness level from 0 (never taked to) to 4 (close friend/family): "))
print()
##CHOOSING THE LETTER TONE
#Choose subject line based on friendliness level
subject_lines = ["Killian Mbappe Transfer Offer", "Offer for Killian Mbappe", "Requesting Killian Mbappe", "Killian Mbappe Availablity", f"200 Millian to get Mbappe out of {recipient_city}"]
subject = subject_lines[friendliness_level]
#Choose greeting based on friendliness level
greetings = [f"Good day {recipient_name},",f"Hello {recipient_name},",f"Dear {recipient_name},",f"Hey {recipient_name},",f"How has it been {recipient_name},"]
greeting = greetings[friendliness_level]
#Choose introduction based on friendliness level
introductions = ["I am the manager of Real Madrid Club de Futbol and", "I make transfer decisions Real Madrid Club de Futbol and", "I purchase the soccer players for Real Madrid and", "I bring players to Real Madrid and","We need more world class players and"]
introduction = introductions[friendliness_level]
#Choose feeling about transfer based friendliness level
feelings = ["The entirety of Real Madrid is in great spirits and eager to","Real Madrid Club de Futbol would be absolutely thrilled to","Real Madrid Club de Futbol is excited to","Real Madrid watering at the mouth to","Real Madrid desire (more than anything) to"]
feeling = feelings[friendliness_level]
#Choose closing based on friendliness level
closings = ["Respectfully,\nFlorentino Peres\nReal Madrid Club de Futbol","Best wishes and regards,\nFlorentino Peres\nReal Madrid Club de Futbol","Best,\nFlorentino Peres\nReal Madrid Club de Futbol","Sincerely,","Your friend in great sport of football,\nFlorentino Peres\nReal Madrid Club de Futbol"]
closing = closings[friendliness_level]
##MENTIONING MUTUAL FRIEND
transfer_pitch = ""
if mutual_friend_name  != "" and friendliness_level > 3:
  transfer_pitch = f"We are associates with {mutual_friend_name}. They have spoken greatly of you interms of general difficulty with negotiations. They also said that you would be willing to sell Kylian if an offer over 150 million was sent to you. We are officially making that offer of 150 million"
goal = "Our goal is to acquire the services of Kylian for a fee no higher than 225 million. We are in need of a talented forward so we would be willing to trade the services of one of our own contracted players."
##PRINTING THE LETTER
print("Letter:")
print()
print("-" * 80)
#Heading
print(f"Recipient Name: {recipient_name}")
print(f"Recipient City: {recipient_city}")
print("-" * 80)
print(f"Subject: {subject}")
print("-" * 80)
print(greeting)
print()
#Body
print(introduction + "we are writing to you to officially enquire about the availabity of your star forward, Kylian Mbappe." + goal + feeling + "acquire the services of the top scorer at this year's world cup." + transfer_pitch)
print()
#closing
print(closing)
print("-" * 80)