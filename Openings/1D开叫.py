import random
import dis1hand
tP=0
tH=0
tS=0
tD=0
tC=0
w=0
count=0
count3=0
count4=0
count5=0
count6=0
a=12
while w<10000:
    dis1hand.dis1hand()
    a=12
    count+=1
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
    if HCP==11:
        if len(S)<=1:
            a=11
            'print("set new a to 11")'
        if len(H)<=1:
            a=11
            'print("set new a to 11")'
        if len(C)<=1:
            a=11
            'print("set new a to 11")'
        if len(D)>=6:
            a=11
            'print("set new a to 11")'
    elif HCP==12:
        if shape==3343:
            a=13
            'print("set new a to 13")'
    if a<=HCP<=14:
        if len(S)<5:
            if len(H)<5:
                if len(C)==6:
                    if len(D)>=5:
                        w+=1
                        tP+=HCP
                        tH+=len(H)
                        tS+=len(S)
                        tD+=len(D)
                        tC+=len(C)
                    if len(D)==5:
                        count5+=1
                    if len(D)>=6:
                        count6+=1
                        '''print("S:",strS)
                        print("H:",strH)
                        print("D:",strD)
                        print("C:",strC)
                        print("Shape:",shape)
                        print("HCP:",HCP)
                        print("A valid 1D opening")'''
                if len(D)==len(C):
                    if len(D)>=4:
                        w+=1
                        tP+=HCP
                        tH+=len(H)
                        tS+=len(S)
                        tD+=len(D)
                        tC+=len(C)
                        if len(D)==3:
                            count3+=1
                        if len(D)==4:
                            count4+=1
                        if len(D)==5:
                            count5+=1
                        if len(D)>=6:
                            count6+=1
                        '''print("S:",strS)
                        print("H:",strH)
                        print("D:",strD)
                        print("C:",strC)
                        print("Shape:",shape)
                        print("HCP:",HCP)
                        print("A valid 1D opening")'''
                if len(D)>len(C):
                    w+=1
                    tP+=HCP
                    tH+=len(H)
                    tS+=len(S)
                    tD+=len(D)
                    tC+=len(C)
                    if len(D)==3:
                        count3+=1
                    if len(D)==4:
                        count4+=1
                    if len(D)==5:
                        count5+=1
                    if len(D)>=6:
                        count6+=1
                    '''print("S:",strS)
                    print("H:",strH)
                    print("D:",strD)
                    print("C:",strC)
                    print("Shape:",shape)
                    print("HCP:",HCP)
                    print("A valid 1D opening")'''
    if 15<=HCP<=17:
        if len(S)<5:
            if len(H)<5:
                if len(S)<=1:
                    if len(D)>=len(C):
                        w+=1
                        tP+=HCP
                        tH+=len(H)
                        tS+=len(S)
                        tD+=len(D)
                        tC+=len(C)
                        if len(D)==3:
                            count3+=1
                        if len(D)==4:
                            count4+=1
                        if len(D)==5:
                            count5+=1
                        if len(D)>=6:
                            count6+=1
                        '''print("S:",strS)
                        print("H:",strH)
                        print("D:",strD)
                        print("C:",strC)
                        print("Shape:",shape)
                        print("HCP:",HCP)
                        print("A valid 1D opening")'''
                elif len(H)<=1:
                    if len(D)>=len(C):
                        w+=1
                        tP+=HCP
                        tH+=len(H)
                        tS+=len(S)
                        tD+=len(D)
                        tC+=len(C)
                        if len(D)==3:
                            count3+=1
                        if len(D)==4:
                            count4+=1
                        if len(D)==5:
                            count5+=1
                        if len(D)>=6:
                            count6+=1
                        '''print("S:",strS)
                        print("H:",strH)
                        print("D:",strD)
                        print("C:",strC)
                        print("Shape:",shape)
                        print("HCP:",HCP)
                        print("A valid 1D opening")'''
                elif len(C)==1:
                    w+=1
                    tP+=HCP
                    tH+=len(H)
                    tS+=len(S)
                    tD+=len(D)
                    tC+=len(C)
                    if len(D)==3:
                        count3+=1
                    if len(D)==4:
                        count4+=1
                    if len(D)==5:
                        count5+=1
                    if len(D)>=6:
                        count6+=1
                    '''print("S:",strS)
                    print("H:",strH)
                    print("D:",strD)
                    print("C:",strC)
                    print("Shape:",shape)
                    print("HCP:",HCP)
                    print("A valid 1D opening")'''
    if 18<=HCP<=19:
        if len(S)<5:
            if len(H)<5:
                if len(D)==len(C):
                    if len(D)>=4:
                        w+=1
                        tP+=HCP
                        tH+=len(H)
                        tS+=len(S)
                        tD+=len(D)
                        tC+=len(C)
                        if len(D)==3:
                            count3+=1
                        if len(D)==4:
                            count4+=1
                        if len(D)==5:
                            count5+=1
                        if len(D)>=6:
                            count6+=1  
                        '''print("S:",strS)
                        print("H:",strH)
                        print("D:",strD)
                        print("C:",strC)
                        print("Shape:",shape)
                        print("HCP:",HCP)
                        print("A valid 1D opening")'''
                if len(D)>len(C):
                    w+=1
                    tP+=HCP
                    tH+=len(H)
                    tS+=len(S)
                    tD+=len(D)
                    tC+=len(C)
                    if len(D)==3:
                        count3+=1
                    if len(D)==4:
                        count4+=1
                    if len(D)==5:
                        count5+=1
                    if len(D)>=6:
                        count6+=1 
                    '''print("S:",strS)
                    print("H:",strH)
                    print("D:",strD)
                    print("C:",strC)
                    print("Shape:",shape)
                    print("HCP:",HCP)
                    print("A valid 1D opening")'''
    if 20<=HCP<=21:
        if len(S)<5:
            if len(H)<5:
                if len(S)<=1:
                    if len(D)>=len(C):
                        w+=1
                        tP+=HCP
                        tH+=len(H)
                        tS+=len(S)
                        tD+=len(D)
                        tC+=len(C)
                        if len(D)==3:
                            count3+=1
                        if len(D)==4:
                            count4+=1
                        if len(D)==5:
                            count5+=1
                        if len(D)>=6:
                            count6+=1  
                        '''print("S:",strS)
                        print("H:",strH)
                        print("D:",strD)
                        print("C:",strC)
                        print("Shape:",shape)
                        print("HCP:",HCP)
                        print("A valid 1D opening")'''
                elif len(H)<=1:
                    if len(D)>=len(C):
                        w+=1
                        tP+=HCP
                        tH+=len(H)
                        tS+=len(S)
                        tD+=len(D)
                        tC+=len(C)
                        if len(D)==3:
                            count3+=1
                        if len(D)==4:
                            count4+=1
                        if len(D)==5:
                            count5+=1
                        if len(D)>=6:
                            count6+=1
                        '''print("S:",strS)
                        print("H:",strH)
                        print("D:",strD)
                        print("C:",strC)
                        print("Shape:",shape)
                        print("HCP:",HCP)
                        print("A valid 1D opening")'''
                elif len(D)<=1:
                    w+=1
                    tP+=HCP
                    tH+=len(H)
                    tS+=len(S)
                    tD+=len(D)
                    tC+=len(C)
                    if len(D)==3:
                        count3+=1
                    if len(D)==4:
                        count4+=1
                    if len(D)==5:
                        count5+=1
                    if len(D)>=6:
                        count6+=1 
                    '''print("S:",strS)
                    print("H:",strH)
                    print("D:",strD)
                    print("C:",strC)
                    print("Shape:",shape)
                    print("HCP:",HCP)
                    print("A valid 1D opening")'''

aP=tP/w
aH=tH/w
aS=tS/w
aD=tD/w
aC=tC/w
aC3=100*count3/w
aC4=100*count4/w
aC5=100*count5/w
aC6=100*count6/w
oR=100*w/count
count=aH+aS+aD+aC
print("Statistics of a natural 1D opening(3+D ignore 12P 4333):")
print("The probability of a 1D opening:",oR,"%")
print("Average HCP:",aP)
print("Average spade length:",aS)
print("Average heart length:",aH)
print("Average diamond length:",aD)
print("Average club length:",aC)
print("The probability of getting 3 diamonds:",aC3,"%")
print("The probability of getting 4 diamonds:",aC4,"%")
print("The probability of getting 5 diamonds:",aC5,"%")
print("The probability of getting more than 5 diamonds:",aC6,"%")
print("The layout of the last board:")
print("S:",strS)
print("H:",strH)
print("D:",strD)
print("C:",strC)
print("Shape:",shape)
print("HCP:",HCP)
