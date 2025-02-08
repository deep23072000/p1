#check eligibility
'''age = int(input("Enter your age = "))
country = input("Enter your country name = ")

if age >= 18:
    if country == 'india' or country == 'India' or country == 'INDIA':
        print("You are eligible to cast vote")
    else:
        print(" Your age is greater than 18 but you are not citizen of india thats why you are not eligible to cast vote")
else:
    print("You are not eligible to cast a vote")'''

#leap year question

'''year = int(input("Enter year that you want to check = "))
if year%4==0:
    if year%100 != 0:
        print(year," is leap year ")
    elif year%400==0:
        print(year," is a leap year ")
    else:
        print(year,"Not a leap year")
else:
    print(year,"Not a leap year")'''

#Grade calculation
'''mark = int(input("Enter your marks = "))
if mark >= 90:
    print("Excellent")
elif mark >= 70 and mark < 90:
    print("Good")
elif mark >= 50 and mark < 70:
    print("Average")
elif mark < 50:
    print("Fail")
else:
    print(" invalid input ")'''

#Number Range Check
'''num = int(input(" Enter check number = "))
if num>=10 and num<=20:
    print(" Your number lies between 10 and 20 range")
elif num > 50 :
    print(" Number is gretaer than 50 ")
else:
    print(" Invalid input " )'''

#Weekend checker
'''day = input(" Enter day ")
if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    print("Not a weekend")
elif day == "Satuarday" or day == "Sunday":
    print( " weekend " )
else:
    print("Invalid input")'''

#Multiple of number
'''num = int(input("Enter number"))
if num%3 == 0 and num%5 ==0:
    print(num," is a multipe of 3 and 5 ")
else:
    print(num , " Not a multiple of 3 and 5")'''

#valid triangle
'''angle_1 = int(input(" Enter angle one = "))
angle_2 = int(input(" Enter angle two = "))
angle_3 = int(input(" Enter angle three = "))

if  angle_1 > 0 and angle_2 > 0 and angle_3 >0:
    if angle_1 + angle_2 + angle_3 == 180:
        print(" It is a triangle ")
    else:
        print("it is not a triangle")
else:
    print("angle should not be negatiove or equal to zero")'''

#login authentication
#WAP to validate a username and password-
#condition 1 - Username must be admin
#condition 2 - Password must be at least 8 charaters long and contain either "@" or "#"

'''username = input("Enter Username")
password = input("Enter Password")

if username == "admin" and len(password) == 8 and "@" in password or "#" in password:
    print("login successfull")
else:
    print("username and password does not match")'''


#number type checker

'''num = int(input("enter number = "))
if num > 0 and num%2==0:
    print("Number is positive and even ")
elif num < 0 and num%2==1:
    print(" number is negative and odd")
elif num == 0:
    print(" number is equal to zero ")
else:
    print("conditon not true")'''

#discount eligibility

'''amount = int(input("Enter your puchase = "))

if amount > 500:
    print(" Enter 1 if you are member ")
    print(" Enter 2 if you are not member ")
    val = int(input(" Type = "))
    if val == 1:
        print(" You got 15 % discount on purchase  ")
        print(" Your final price after applying discount is ",amount - ((amount/100)*15))
    elif val == 2:
        print(" You got 10 % discount on purchase ")
        print(" Your final price after applying discount is ",amount - ((amount/100)*10))
    else:
        print("invalid selection")
else:
    print("Your final price is " , amount)'''

#traffic light system

'''print("Enter 1 for red")
print("Enter 2 for yellow")
print("Enter 3 for green")
val = int(input(" Enter option = "))

if val == 1:
    print("stop")
elif val == 2:
    print("get ready")
elif val == 1:
    print("go")
else:
    print("invalid input")'''

#temperature checker

'''temperature = int(input("Enter temperature"))

if temperature < 0:
    print("Freezing")
elif temperature >= 0 and temperature <=15:
    print("cold")
elif temperature >= 16 and temperature <=30:
    print("warn")
elif temperature >30:
    print("hot")
else:
    print("invalid input")'''


#divisibility tst
#WAP to check if a number is :
#divisible by 2 or 3
#not divisible by both

'''num = int(input("Enter test number"))
if (num % 2==0 or num%3==0) and (not(num%2==0 and num%3==0)):
    print("done")
else:
    print("not done")'''

#even odd prime
'''num = int(input("Enter test number "))
if num %2==0:
    if num >1 and num/2 '''


a = 45
print(f"num is {a}")



        
    



    


