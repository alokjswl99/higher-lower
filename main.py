from art import logo, vs
from game_data import data
import random
from replit import clear
print(logo)
game_on=True
current_score=0
B=random.choice(data)

def get_random_account(data,A):
  B=random.choice(data)
  while A==B:
    B=random.choice(data)
  return B

def check_answer(guess, A, B):
  if A['follower_count']>B['follower_count']:
    return guess=='a'
  else: return guess=='b'

while game_on:
  A=B
  B=get_random_account(data,A)
  print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
  print(vs)
  print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")
  choice=input("Who has more followers? Type 'A' or 'B':").lower()
  answer_check=check_answer(choice, A, B)
  clear()
  print(logo)
  if answer_check:
    current_score+=1
    print(f"You are right. Current score: {current_score}")
  else:
    print(f"Sorry, that's wrong. Final score:{current_score}")
    game_on=False
