trick=[1,2,3,4]
tricktotal=[]
k=200
count=0
print(tricktotal)
trick1=[1,2,3,4]
for i in range(100):
    tricktotal.append(trick)
for i in tricktotal:
    if trick1==i:
        count+=1

if count==k:
    print("a")
elif count!=k:
    print("b")