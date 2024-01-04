import random
import dis1hand
w=0
count=0
k=input("Please enter the value of HCP you want to know (do not enter invalid number becuase that only hurts your own computer):")
k=int(k)
while w<1000:
    dis1hand.dis1hand()
    HCP=dis1hand.HCP
    count+=1
    if HCP==k:
        w+=1
R=100*w/count
print("The probability of getting an exact",k,"HCP hand:",R,"%")
