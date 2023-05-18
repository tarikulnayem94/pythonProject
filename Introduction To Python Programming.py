# Introduction To Python Programming

print ("i am a software QA Engineer with 2+ experiences")


sarah, mike, bob = 10, 12, 14
print(mike)

age1 = 21
age2 = 18
print(age1+age2)


sentence = "i am a software QA Engineer with 2+ experiences"
print(sentence[7:16])
print(sentence[:-3])
print(sentence[:4])


name = "nayeem"
boyss = "%s is 27 years old"
print(boyss%name)

shoplist = ['apple', 'orange', 'water melon', 'papaya']
print(shoplist[3])


value = (12, 15)
shop = ('apple', 'grapes')

res = value+shop
print(res)

tut = ("hi")
TUT = tut*3
print(TUT)


if(5>3):
    print("true")
if(5<3):
    print("wrong")
else:
    print("false")

age = 28
if(age <= 25 and age>=18):
    print("you are young enough")
elif(age > 25):
    print("you are adult")
else:
    print("you are teenager")

for i in range(1, 7):
    print(i)

for i in range(12, 25, 3):
    print(i)

for i in range(2, 6):
    for j in range(6, 9):
        print(i+j)

c = 3
while(c<=7):
    print(c)
    if(c==5):
        break
    c= c+1

try:
    if (x > 25):
        print("you are an adult")
except:
    print("something is wrong in your code")


#function

def addition (number1, number2):
    print(number1+number2)
addition(12, 18)

sum = addition(11, 13)
print(sum)


print(abs(-23))
print(abs(12))
print(bool(-1))
print(bool(1))
print(bool(None))


someoneValue = 3
print(str(someoneValue))
print(float(someoneValue))
print(int(someoneValue))



