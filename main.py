import random 

level=int(input("Enter the number of your level:\n"
"1-Beginner(1-20)\n"
"2-Intermediate(1-100)\n"
"3-Hard(1-1000)\n"))

place=0
if level==1:
   place=20
elif level==2:
   place=100
elif level==3:
   place=1000
else:
   print("Invalid user input")
   exit(1)

guess_number=random.randint(1,place)
i=0
while i<5:
 user_input= int(input(f'Enter a number between 1 and {place}: '))
 if user_input==guess_number:
    print("Your guess is correct!")
    print("You won using",i+1,"out of 5 chances")
    break
 else:
    if i==4:
      print("Your guess is wrong and the game is over")
    elif user_input>place or user_input<1:
      print(f"Your input is out of the range (between 1 and {place})")
    elif user_input<guess_number-5:
      print("Your guess is too low, try again")
    elif user_input>guess_number+5:
      print("Your guess is too high, try again")
    else:
      print("Your guess is close") 
 i+=1
if user_input==guess_number:
   print("Thanks for playing!")
else:
   print("The correct answer was",guess_number,".Thanks for playing!")