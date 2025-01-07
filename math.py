import time
import random
import math
score = 0
def question(qno):
    if qno == 0:
        num1 = random.randint(0,9999)
        num2 = random.randint(0,9999)
        result = num1 + num2
        answer = input(str(num1)+'+'+str(num2)+': ')
        if answer == result:
            return(1)
        else:
            return(0)
    if qno == 1:
        num1 = random.randint(0,9999)
        num2 = random.randint(0,9999)
        result = num1 - num2
        answer = input(str(num1)+'-'+str(num2)+': ')
        if answer == result:
            return(1)
        else:
            return(0)
    if qno == 2:
        num1 = random.randint(0,9999)
        num2 = random.randint(0,9999)
        result = num1 * num2
        answer = input(str(num1)+'*'+str(num2)+': ')
        if answer == result:
            return(1)
        else:
            return(0)
    if qno == 3:
        num1 = random.randint(0,9999)
        num2 = random.randint(0,9999)
        result = num1 / num2
        answer = input(str(num1)+'/'+str(num2)+': ')
        if answer == result:
            return(1)
        else:
            return(0)
    if qno == 4:
        num1 = random.randint(0,9999)
        result = num1 * num1
        answer = input(str(num1)+'^2: ')
        if answer == result:
            return(1)
        else:
            return(0)
    if qno == 5:
        num1 = random.randint(0,9999)
        num2 = random.randint(0,9999)
        result = math.sqrt(num1)
        answer = input(str(num1)+'sqrt: ')
        if answer == result:
            return(1)
        else:
            return(0)

print('5')
time.sleep(1)
print('4')
time.sleep(1)
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)
print('go')
time1 = time.time()
while score <= 10:
    score = score + question(random.randint(0,5))
    
