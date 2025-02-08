'''count = 0
a = 0
while a%2==0:
    a = int(input("Enter number"))
    print("out ")
    count+=1
else:
    print("out of loop")'''

#Write a while loop that counts down from 10 to 1 and print each number
#when the loop finishes print  "liftoff"
'''count = 10
while count > 0:
    print(count,end=",")
    count-=1
else:
    print("lift off")'''

#WAP that keeps asking the user to input a number and add all the isers together and stop
#asing when the user enters 0 . finally print the total sum
'''collect = 0;
while True:
    print("Enter 0 for sum of all number you entered") 
    inp = int(input("Enter number = "))
    if inp > 0 or inp < 0:
        collect += inp
    elif inp == 0:
        print("Enter number is equal to 0 you are out of loop")
        print(f"sum of all entered number is {collect}")
        break
    else:
        print("invalid input")'''

#use a while loop to print all even number between 1 and 20

'''count = 1
while count < 20:
    if count%2==0:
        print(count,end="\n")
    count+=1'''


#Guess the number

'''num = 7
while True:
    uinput = int(input("Guess the number = "))
    if uinput == num:
        print("correct")
        break
    else:
        print("You guessed wrong please try again")'''

#reverse digits

'''d = int(input("Enter integer that you want to reverse"))
f = str(d)
#print(f)
#print(type(f))

count = len(f)
store = ""
while (count-1) >= 0:
    store = store + f[count-1]
    count -= 1
print(store)'''

#factorial calculator

'''n = 6
count = 1
d = 1
while count <= n:
    d *= count
    count += 1

print(d)'''

#collatz sequence
'''while True:
    uinput = int(input("enter positive integer"))
    if uinput%2 == 0:
        uinput /= 2
        print(uinput)
        if uinput == 1:
            break
    elif uinput%2 == 1:
        uinput*=3
        uinput +=1
        print(uinput)
        if uinput == 1:
            break'''

#prime number

'''n = int(input("Enter number"))
count = 1
v = 0
while count < n/2:
    if n % count == 0 and n%1==0:
        v += 1    
    count += 1

if v == 1:
    print(" It is prime number")
elif n == 2:
    print(" It is prime number")    
else:
    print("not a prime number")'''

#simulate a bank account
'''initial_balance = 1000

while True:
    print("Enter 1 for deposit balance")
    print("Enter 2 for withdraw balance")
    print("Enter 3 for check balance")
    c = int(input("Enter = "))
    if c == 1:
        print("Enter amount you want to deposit")
        a = int(input("Enter = "))
        initial_balance += a
    elif c == 2:
        print("Enter amount you want to withdraw")
        a = int(input("Enter = "))
        initial_balance -= a
    elif c == 3:
        print(f"your balance is {initial_balance}")
        print("================================================================")'''

#find the GCD ( greatest common divisor ) of two numbers using a while loop

'''import math

a = 18
b = 36
c = math.gcd(a,b)
print(c)'''

#euclid's algorithms
'''a = 36
b = 18

while b:
    a, b = b, a % b
    
print(f"The GCD of a and b is {a}")'''


#palindrome

'''a = 121
b = str(a)
print(b)
print(type(b))
c = len(b)
print(c)
d = ""
count = 1

while count <= c:
    d = d + b[c-count]
    print(d)
    count +=1

if d == b:
    print("palindrome")'''


# find the maximum
#keep asking the user for numbers until they enter -1.
#print the maximum number they entered (ignore - 1)
'''c = 0
while True:
    print("if you want exit type -1")
    num = int(input("Enter the number = "))
    if c < num:
        c = num
    elif num == (-1):
        print(f"The maximum number you entered is {c}")
        break'''

#fibonacci series

'''s1 = 0
s2 = 1
s3 = 0

digit = int(input("Enter digit you want ot need = "))
it = 0
while it < digit:
    if it<1:
        print(it,end=",")
    elif it >= 1:
        s1 = s2
        s2 = s3
        s3 = s1 + s2
        print(s3,end=",")
    it+=1'''

#decimal to binary
#method1
'''a = bin(4)
print(type(a))'''

#logic
'''a = 10
s = ""
print(bin(a)[2:])

while True:
    if a==0:
        print(s)
        break
    elif a%2==1:
        s = s + "1"
        a = a//2
    elif a%2 == 0:
        s = s + "0"
        a = a//2'''
#revere the s


#armstrong between 1 to 1000
'''count = 1
end = 1000
while count < end:
    str1 = str(count)
    strlen = len(str1)
    run = 0
    store = 0
    while run < strlen:
        store = store + (int(str1[run]) ** strlen)
        run+=1
        if count == store:
            print(count)
            break
    count+=1'''


#pattern
'''a = 4
count = 1
while count <= a:
    s = count
    while 0 < s:
        print("*",end=" ")
        s -= 1
        if s == 0:
            print("")
            break
    count+=1'''
    
    
        

        
        
    
        





        
    

    
    
        




        
        
    
    
    



    
    
    


        
    
    
    


        
        
        
        



    
