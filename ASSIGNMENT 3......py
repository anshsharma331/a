
x = int(input('Enter a number of your choice :'))
y = bin(x)
z = str(y)
print('Binary equivalent of the number entered:',y)







print("select an operation to perform: ")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")

operation= input()
if operation=="1":
    num1 = input("enter 1st number: ")
    num2 = input("enter 2nd number: ")
    print("The sum is " + str(int(num1) + int(num2)))
elif operation== "2":
    num1=input("enter 1st number: ")
    num2 =input("enter 2nd number: ")
    print("The sum is " + str(int(num1) - int(num2)))
elif operation== "3":
    num1=input("enter 1st number: ")
    num2 =input("enter 2nd number: ")
    print("The sum is " + str(int(num1) * int(num2)))
elif operation== "4":
    num1=input("enter 1st number: ")
    num2 =input("enter 2nd number: ")
    print("The sum is " + str(int(num1) / int(num2)))
else:
    print("Invalid Entry")





import math

#a
answer_1 = (3+4)*5
print("Answer (a):", answer_1)


#b
n = float(input("Enter Number"))
answer_2 = (n*(n-1))/2
print("Answer (b):", answer_2)


#c
radius = float(input("Enter Number"))
answer_3 = 4*math.pi*(radius**2)        
print("Answer (c):", answer_3)


#d
r = float(input("Enter Number"))
angle = float(input("Enter Angle in Radians"))
b = math.cos(angle)
c = math.sin(angle)
answer_4 = (r*(b)**2 + r*(c)**2)**(1/2)
print("Answer (d):", answer_4)


#e
y1 = float(input("Enter Number y1"))
y2 = float(input("Enter Number y2"))
x1 = float(input("Enter Number x1"))
x2 = float(input("Enter Number x2"))
answer_5 = ((y1 - y2)/(x1 - x2))
print("Answer (e):", answer_5)









for a in range(5):
 print(a)

for b in range(3,10):
 print(b)
for c in range(4,13,3):
 print(c)
for d in range(15,5,-2):
 print(d)
for e in range(5,3):
 print(e)









h= int(input("Enter no. of hydrogen atoms: "))
c = int(input("Enter the no. of carbon atoms: "))
o= int(input("Enter the no. of oxygen atoms: "))

wt_h = h*1.00794
wt_c = c*12.0107
wt_o = o*15.9994

print(wt_h + wt_c + wt_o)
