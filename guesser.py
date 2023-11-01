import random 
numguess = 0

number = random.randint(1, 50) 
print('Guess a number between 1 and 50.')

while numguess < 6:
  guess = input("Guess a number: ")
  
  guess =  int (guess)
  numguess = numguess + 1
  
  if guess < number:
      print ("Your guess is too low.")
  
  if guess > number:
   print ("Your guess is too high.")

  if guess == number:
    print ("Congratulations. You win!.") 

if guess != number:
  number = str(number)
  print ("You Lose!")
