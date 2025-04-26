password =input("enter password")
count= 0  
    
if len(password) >= 8:    
 for i in password:
   if i=="@" or i== "#":
    print("password is strong")
    count+= 1
    break
if count == 0:
   print("password is moderate")
   
elif len(password)<6:
    print("password is weak")
    
elif len(password)>= 6:
     print("password is moderate")
else:
    print("invalid click")
'''    


ch ="2"

if ord(ch)<= 65 and ord(ch)<=90:
   print("character is capital alphabet")
elif ord(ch)>= 97 and ord(ch)<= 123:
    print("character is small alphabet")
else:
    print("invalid input")
    print(ord(ch))
'''
p = 1223
c= p
store = 0

while p!=0:
     rem= p%10
     store = (store + rem)*10
     p//10
     print(store/10)

if(c == (store//10)):
    print("palindrome")
else:
    print("not a palindrome")
'''    

    
    
