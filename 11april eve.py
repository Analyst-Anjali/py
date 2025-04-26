num= 22
if num> 50:
   print("number is greater than 50")

else:
   print("number is less than 50")

num1= 20
num2= 40

if num1>num2:
   print("num1 is greater than num2")
else:
    print("num2 is greater than num1")
    
num =int(input("Enter number ="))

if num%3==0 and num%5==0:
   print("number is divisible by 3 and 5")
else:
    print("number is not divisible by 3 and 5")


#write a program to check if a given username and password are both correct
#username must be "admin"
#password must be "12345"
    
username= input("enter username=")
password= input("enter password=")

if password== "12345" and username== "admin":
   print("username and password is correct")
else:
    print("username and password is not correct")
                
   
num = int(input("Enter number ="))
if num%2==0 and num>0:
   print("number is greater than 0 and even")

elif num%2!=0 and num>0:
    print("number is positive but not even")
elif num%2==0 and num<0:
     print("number is even but negative")
else:
     print("number is not positive nor negative")
                   
