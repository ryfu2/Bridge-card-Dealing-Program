import random
import dis1hand
while True:
    count=0
    w=0
    m=input("Please enter the lower bound of HCP (close interval):")
    n=input("Please enter the upper bound of HCP (close interval):")
    m=int(m)
    n=int(n)
    x=n-m
    while w<1000:
        dis1hand.dis1hand()
        HCP=dis1hand.HCP
        count+=1
        if m<=HCP<=n:
            w+=1
    R=100*w/count
    print("The probability of getting HCP in the range of [",m,",",n,"] is:",R,"%")
