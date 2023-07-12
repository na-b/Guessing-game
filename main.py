import random 

guess_number=random.randint(1,20)
i=0
while i<5:
 user_input= int(input('Enter a number between 1 and 20: '))
 if user_input==guess_number:
    print("Your guess is correct!")
    print("You won using",i+1,"out of 5 chances")
    break
 else:
    if i==4:
      print("Your guess is wrong and the game is over")
    elif user_input<guess_number-5:
      print("Your guess is too low, try again")
    elif user_input>guess_number+5:
      print("Your guess is too high, try again")
    else:
      print("Your guess is close")
   
 i+=1
print("Thanks for playing!")