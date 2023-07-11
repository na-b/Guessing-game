import random 

guess_number=random.randint(1,20)
i=0
while i<5:
 user_input= int(input('Enter a number between 1 and 20: '))
 if user_input==guess_number:
    print('Your guess is correct')
    break
 else:
    print("Your guess is wrong")
 i+=1