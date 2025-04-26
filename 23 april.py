#palindrome in list
ls = [5,4,3,2,1]

reverselist = ls [::-1]

if ls == reverselist:
   print("list is palindrome")
else:
    print("list is not palindrome")

#flatten in a list
'''ls = [[2,4],[34,56]]

flat_list =[]

l =len(ls)

for i in range(l):
    for j in range(len(ls[i])):
        flat_list.append(ls[i][j])
        
print(flat_list)'''

    
#remove the all the element from the list which is divisible by 3
ls = [5,4,6,3,8,9]
store_list =[]

for i in ls:
    if i%3 !=0:
        store_list.append(i)

print(store_list)
print(ls)

#write a function that takes a list and return a new list with element doubles

ls = [3,4,3,45]
s= []
for i in ls:
    s.append(i+i)

print(s)


#take input from user to create a list
'''ls = []
inp = int(input("Enter specific range of list"))
for i in range(inp):
    l= int(input(f"Enter{i}index number"))
    ls.append(l)
print(ls)'''    

