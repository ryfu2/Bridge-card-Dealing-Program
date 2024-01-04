import random
import dis1hand
tP=0
tH=0
tS=0
tD=0
tC=0
w=0
for i in range(50000):
    dis1hand.dis1hand()
    S=dis1hand.S
    H=dis1hand.H
    D=dis1hand.D
    C=dis1hand.C
    HCP=dis1hand.HCP
    shape=dis1hand.shape
    strS=[str(i) for i in S]
    strH=[str(i) for i in H]
    strD=[str(i) for i in D]
    strC=[str(i) for i in C]
    tP+=HCP
    tH+=len(H)
    tS+=len(S)
    tD+=len(D)
    tC+=len(C)
aP=tP/50000
aH=tH/50000
aS=tS/50000
aD=tD/50000
aC=tC/50000
count=aH+aS+aD+aC
print("Statistics of a random hand:")
print("average point:",aP)
print("average spade length:",aS)
print("average heart length:",aH)
print("average diamond length:",aD)
print("average club length:",aC)
print("The layout of the last board:")
print("S:",strS)
print("H:",strH)
print("D:",strD)
print("C:",strC)
print("Shape:",shape)
print("HCP:",HCP)
