import random

#Ask to chooses a random number from 1 to 100.
def main ():
  
  number = random.randint(1, 100)
  guesses = 0

  while True: 
    user_input = input("Guess a number from 1 to 100: ")

#If the person inputs a number out of the range, it will output an invalid response.
    if not user_input.isdigit():
      print("Invalid number. Please enter a valid number.")
      continue

#Store the interger into user_num
    user_num = int(user_input)

    if user_num < 1 or user_num > 100:
      print("Invalid number. Please enter a valid number.")
      continue

#Increases the guess count.
    guesses += 1

#Gives out the proper responses to the guesses until guessed correctly.
    if user_num < number:
      print("Too low! Guess again.")
    elif user_num > number:
      print("Too high! Guess again.")
    else:
      print("Congratulations! You guessed the number " + str(number) + " in " + str(guesses) +         " guesses.")
      break
      
if __name__ == "__main__":
  main()
