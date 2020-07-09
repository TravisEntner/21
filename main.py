import random
print("This is 21, how you play is, i will give you 2 random numbers, your goal is to get as close to 21 as posible without going over, also your total must be higher than mine, but you wont know what my numbers are")
firstNum = random.randint(1,12)
secondNum = random.randint(1,12)
myFirst = random.randint(1,12)
mySecond = random.randint(1,12)
myTotal = myFirst + mySecond
print("Your first number is, " + str(firstNum) + " and your second number is, " + str(secondNum))

usertotal = firstNum + secondNum
print("Your total is " + str(usertotal))
if(usertotal == 21):
  print("You got a blackjack you win")


ask = input("Are you happy with you numbers?(If you are not happy with your total I will give you a new number to add to the total)  yes or no, please do not use caps: ")

while(ask == "no"):
  newNum = random.randint(1,12)
  usertotal = usertotal + newNum
  print("your new total is " + usertotal)
  askAgain = input("Are you happy with you numbers?(If you are not happy with your total I will give you a new number to add to the total)  yes or no, please do not use caps: ")
  if(ask == yes and usertotal > 21):
    print("you lose your total is over 21")
  elif(ask == "yes" and usertotal > myTotal):
      print("Your total was bigger than mine, you win, my number is " + str(myTotal) )
  elif(ask == "yes" and usertotal < myTotal):
      print("My number was bigger than yours I win, my number was " + str(myTotal))

if(ask == yes):
  elif(ask == "yes" and usertotal > 21):
    print("you lose your total is over 21")
  elif(ask == "yes" and usertotal > myTotal):
    print("Your total was bigger than mine, you win, my number is " + str(myTotal) )
  elif(ask == "yes" and usertotal < myTotal):
    print("My number was bigger than yours I win, my number was " + str(myTotal))




