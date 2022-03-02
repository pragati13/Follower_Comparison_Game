import art
import game_data
import random
import os

rand_cmpa = random.randint(0,49)
rand_cmpb = random.randint(0,49)
final_score = 0
print(art.logo)

def questionairre(rand_cmpa,rand_cmpb):
  if rand_cmpa != rand_cmpb:
    print("Compare A: " + game_data.data[rand_cmpa]['name'] + ", a " + game_data.data[rand_cmpa]['description'] + ", from " + game_data.data[rand_cmpa]['country'])
    print(art.vs)
    print("Against B: " + game_data.data[rand_cmpb]['name'] + ", a " + game_data.data[rand_cmpb]['description'] + ", from " + game_data.data[rand_cmpb]['country'])
    comparison(rand_cmpa, rand_cmpb)
  else:
    rand_cmpb = random.randint(0,49)
    questionairre(rand_cmpa,rand_cmpb)
  
def comparison(rand_cmpa,rand_cmpb):
  answer = input("Who has more followers? Type 'A' or 'B': ").lower()
  global final_score
  if answer == "a" or answer == "b":
    if game_data.data[rand_cmpa]['follower_count'] > game_data.data[rand_cmpb]['follower_count']:
      highest = "a"
    elif(game_data.data[rand_cmpa]['follower_count'] < game_data.data[rand_cmpb]['follower_count']):
      highest = "b"
    if(answer == highest):
      os.system('clear')
      final_score = final_score + 1
      print(art.logo)
      print(f"You're right! Current score: {final_score}.")
      rand_cmpc = random.randint(0,49)
      questionairre(rand_cmpb,rand_cmpc)
    else:
      os.system('clear')
      print(art.logo)
      print(f"Sorry, that's wrong. Final score: {final_score}")
      exit(0)
  else:
     print("Please select proper option...")

questionairre(rand_cmpa,rand_cmpb)