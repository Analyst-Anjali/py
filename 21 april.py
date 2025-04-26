ls= [23,22,45,2,45,245,35,2]
'''tp = (23,22,45,2,45,245,35,2)'''

'''store= 0
for i in ls:
    if i %2 == 0:
        store += i
print("The sum of all even number in list is", store)
print(tp)'''

'''ls1 = []    
for i in ls:
    for j in ls:
        if i!= j:
          ls1.append(i)
print(ls1)

          

ls1= set(ls)
ls2 =[]
for i in ls1:
    print(i)
    ls2.append(i)
    
print(ls2)'''    
    
#3
for i in ls:
    for j in ls:
        if i < j:
            i,j = j,i
print(ls)           
           


