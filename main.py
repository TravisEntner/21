import random
print("This is 21, how you play is, i will give you 2 random numbers, your goal is to get as close to 21 as posible without going over, also your total must be higher than mine, but you wont know what my numbers are. I will generate new numbers for myself untill I have more than 17.")
firstNum = random.randint(1,10)
secondNum = random.randint(1,10)
myFirst = random.randint(1,10)
mySecond = random.randint(1,10)
myTotal = myFirst + mySecond
print("Your first number is, " + str(firstNum) + " and your second number is, " + str(secondNum))

usertotal = firstNum + secondNum
print("Your total is " + str(usertotal))
if(usertotal == 21):
  print("You got a blackjack you win")
elif(usertotal > 21):
  print("Your numbers are over 21 you lost")
while(myTotal < 17):
  myNew = random.randint(1,10)
  myTotal = myTotal + myNew
if(myTotal > 21):
  print("my total is over 21 you win")
ask = input("Would you like a new card(If you want a new card I will give you a new number to add to the total) or you can tap out and you neither win nor loose.  yes, no, or tap out, please do not use caps: ")
for n in range(21):
  if(ask == "tap out"):
    print("Thanks for playing")
  if(ask == "yes"):
    newNum = random.randint(1,10)
    usertotal = usertotal + newNum
    print("your new total is " + str(usertotal))
  if(ask == "yes" and usertotal > 21):
    print("Oh no you lost your total is over 21.")
  if(ask =="yes" and usertotal < 21):
    ask = input("Would you like a new card(If you want a new card I will give you a new number to add to the total)  yes or no, please do not use caps: ")
  if(ask == "no" and usertotal > 21):
    print("Oh no you lost your total was bigger than")
  if(ask == "no" and myTotal > usertotal):
    print("Oh no You lost,because my total was bigger than yours, my total was " + str(myTotal))
  if(ask == "no" and usertotal > myTotal and usertotal <= 21 or usertotal == 21):
    print("You win, my total was " + str(myTotal))
  if(ask == "tap out"):
    break
  if(usertotal > 21 or usertotal == 21):
    break
  if(ask == "no"):
    break