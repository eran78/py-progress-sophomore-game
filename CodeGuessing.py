import random

def introduction(): 
 print("HACKING A PIN-CODE")
 print("Hello there! If you are new to this game, type 'yes', if not, type 'no'")


 x = input()

 if x == "yes":
   print("All right! Then you have some catching up to do... In this game, you have 10 tries to guess the code the computer has chosen. If you've guessed a digit correctly with the correct position, the computer will type 'G'. If the digit is correct, but not in the correct position, the computer will type a 'C'. If the digit is incorrect, the computer will type an 'F'. If the code is completely correct, you win. But be aware that in some of the codes, the same digit may appear more than once. That's it! You're all ready. Good luck!")
 else:
   print("All right! You know how to play it... so, good luck!")

introduction()

def main():
  

 #List of codes

  codes = [
   "1231", 
   "9997", 
   "8829", 
   "6765", 
   "9114", 
   "5673", 
   "0103", 
   "4370", 
   "8301",
   "1022"
  ]

  global chosenCode
  global answer

  chosenCode = random.choice(codes)

  answerstyped = 0

  while answerstyped < 10:

    answerstyped = answerstyped + 1


    #List of eastereggs
    ee1 = "1955"
    ee2 = "1980"
    ee3 = "2003"
    ee4 = "2310"
    ee5 = "0908"
    ee6 = "3009"
    ee7 = "1972"
    ee8 = "1968"

    print("This is try " + str(answerstyped) + ".")
    answer = input()

    if answer.isdigit == False:
      print("Only use numbers.")
      answerstyped = answerstyped - 1
      continue

    feedback = ['F'] * 4
    digits = [chosenCode.count(str(i)) for i in range(10)]
    count_digits = [i for i in digits]
   

    if answer == chosenCode:
      #try nr. 1
      if answer == chosenCode and answerstyped == 1:
        print("Congratulations! You've guessed the code correctly within " + str(answerstyped) + " try.")
        break
      #multiple tries
      if answer == chosenCode and answerstyped > 1:
        print("Congratulations! You've guessed the code correctly within " + str(answerstyped) + " tries.")
        break

    else:
      for i, digit in enumerate(answer):
        index = int(digit)
        if count_digits[index] > 0 and chosenCode[i] == digit:
          count_digits[index] -= 1
          feedback[i] = 'G'
        elif count_digits[index] > 0:
          count_digits[index] -= 1
          feedback[i] = 'C'
       
    if answer != chosenCode and answer == ee1 or answer == ee2 or answer == ee3 or answer == ee4 or answer == ee5 or answer == ee6 or answer == ee7 or answer == ee8:
     
      if answer == ee1:
        print("You've found the birth year of bnt")
      if answer == ee2:
        print("You've found the birth year of lgg")
      if answer == ee3:
        print("You've found the birth year of Eran, the game developer")
      if answer == ee4:
        print("You've found the birthday of Eran, the game developer")
      if answer == ee5:
        print("You've found the birthday of Judit, the game developer's best female friend")
      if answer == ee6:
        print("You've found the birthday of Tijmen, the game developer's best male friend")
      if answer == ee7:
        print("You've found the birth year of Liat, the game developer's mother")
      if answer == ee8:
        print("You've found the birth year of Rani, the game developer's father")

      answerstyped = answerstyped - 1

    else:
      print(*feedback)
      print("Incorrect, try again.")

  answerstyped = answerstyped - 1

main()


def restart_game():

  

  while True:
    if answer != chosenCode:
      print("Incorrect. You have no tries left. The correct code was " + chosenCode + ". Do you want to start over?")
    elif answer == chosenCode:
      print("Do you want to start over?")
      
    restart_game = input()

    while restart_game.lower() != "yes" or restart_game.lower() != "no":
      if restart_game.lower() == "yes":
        print("Great! Now try to beat the computer once more...")
        main()
        break

      else:
        print("That's fine. See you again soon!")
        print("Created by E. R. Hyman")
        print("Voorburg, ZH, The Netherlands")
        print("Copyright, 2019")
        print("All rights reserved")
        exit()

restart_game()