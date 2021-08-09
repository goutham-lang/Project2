lst = []
lst1=[]
lst2=[]
lst3=[]
n=int(input("Enter the no.of elements in list 1: "))
k=int(input("Enter the no.of elements in list 2: "))
print("Enter the elements of list1")
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
print("Enter the elements of list2")
for i in range(0,k):
    ele=int(input())
    lst2.append(ele)
print("List1= "+str(lst))
for number in lst:
    if number>0: lst1.append(number)
print(lst1)
print("List2 =  "+str(lst2))
for number in lst2:
    if number>0: lst3.append(number)
print(lst3)

