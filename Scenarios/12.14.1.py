import random
tP=0
tH=0
tS=0
tD=0
tC=0
w=0
x=0
count=0
count3=0
count4=0
count5=0
count6=0
def dis1hand():
    #给各门花色设置变量并让所有变量成为全局变量
    global i
    global C
    global D
    global H
    global S
    global HCP
    global card
    i=0
    C=[]
    D=[]
    H=[]
    S=[]
    HCP=0
    while i<13:
        b=int(random.random()*len(card))
        #判定点力
        if card[b]==13:
            HCP+=4
        if card[b]==12:
            HCP+=3
        if card[b]==11:
            HCP+=2
        if card[b]==10:
            HCP+=1
        if card[b]==26:
            HCP+=4
        if card[b]==25:
            HCP+=3
        if card[b]==24:
            HCP+=2
        if card[b]==23:
            HCP+=1
        if card[b]==39:
            HCP+=4
        if card[b]==38:
            HCP+=3
        if card[b]==37:
            HCP+=2
        if card[b]==36:
            HCP+=1
        if card[b]==52:
            HCP+=4
        if card[b]==51:
            HCP+=3
        if card[b]==50:
            HCP+=2
        if card[b]==49:
            HCP+=1
        #判定花色
        if 1<=card[b]<=13:
            C.append(card[b])
        if 13<card[b]<=26:
            D.append(card[b])
        if 26<card[b]<=39:
            H.append(card[b])
        if 39<card[b]<=52:
            S.append(card[b])
        card.pop(b)
        i+=1
    #判定牌型
    global shape
    shape=1000*len(S)+100*len(H)+10*len(D)+1*len(C)
    if shape<1000:
        shape="0"+str(shape)
    #保留原始数值方便四明手分析比较大小
    global Sraw
    global Hraw
    global Draw
    global Craw
    Sraw=S.copy()
    Hraw=H.copy()
    Draw=D.copy()
    Craw=C.copy()
    #打印
    C.sort(reverse=True)
    k=len(C)
    if k==0:
        C.append("-")
    else:
        for i in range(0,k):
            if C[i]==1:
                C.pop(i)
                C.insert(i,"2")
            if C[i]==2:
                C.pop(i)
                C.insert(i,"3")
            if C[i]==3:
                C.pop(i)
                C.insert(i,"4")
            if C[i]==4:
                C.pop(i)
                C.insert(i,"5")
            if C[i]==5:
                C.pop(i)
                C.insert(i,"6")
            if C[i]==6:
                C.pop(i)
                C.insert(i,"7")
            if C[i]==7:
                C.pop(i)
                C.insert(i,"8")
            if C[i]==8:
                C.pop(i)
                C.insert(i,"9")
            if C[i]==9:
                C.pop(i)
                C.insert(i,"10")
            if C[i]==13:
                C.pop(i)
                C.insert(i,"A")
            if C[i]==12:
                C.pop(i)
                C.insert(i,"K")
            if C[i]==11:
                C.pop(i)
                C.insert(i,"Q")
            if C[i]==10:
                C.pop(i)
                C.insert(i,"J")
    D.sort(reverse=True)
    k=len(D)
    if k==0:
        D.append("-")
    else:
        for i in range(0,k):
            if 13<D[i]<23:
                c=D[i]-12
                D.insert(i,c)
                D.pop(i+1)
            if D[i]==26:
                D.pop(i)
                D.insert(i,"A")
            if D[i]==25:
                D.pop(i)
                D.insert(i,"K")
            if D[i]==24:
                D.pop(i)
                D.insert(i,"Q")
            if D[i]==23:
                D.pop(i)
                D.insert(i,"J")
    H.sort(reverse=True)
    k=len(H)
    if k==0:
        H.append("-")
    else:
        for i in range(0,k):
            if 26<H[i]<36:
                c=H[i]-25
                H.insert(i,c)
                H.pop(i+1)
            if H[i]==39:
                H.pop(i)
                H.insert(i,"A")
            if H[i]==38:
                H.pop(i)
                H.insert(i,"K")
            if H[i]==37:
                H.pop(i)
                H.insert(i,"Q")
            if H[i]==36:
                H.pop(i)
                H.insert(i,"J")
    S.sort(reverse=True)
    k=len(S)
    if k==0:
        S.append("-")
    else:
        for i in range(0,k):
            if 39<S[i]<49:
                c=S[i]-38
                S.insert(i,c)
                S.pop(i+1)
            if S[i]==52:
                S.pop(i)
                S.insert(i,"A")
            if S[i]==51:
                S.pop(i)
                S.insert(i,"K")
            if S[i]==50:
                S.pop(i)
                S.insert(i,"Q")
            if S[i]==49:
                S.pop(i)
                S.insert(i,"J")
    'print(Sraw,Hraw,Draw,Craw)'
def oCopening():
    global w
    global HCP
    global shape
    global S,D,H,C
    global a
    global count,count3,count4,count5,count6
    if HCP==11:
        if len(S)<=1:
            a=11
            'print("set new a to 11")'
        if len(H)<=1:
            a=11
            'print("set new a to 11")'
        if len(D)<=1:
            a=11
            'print("set new a to 11")'
        if len(C)>=6:
            a=11
            'print("set new a to 11")'
    elif HCP==12:
        if shape==4333:
            a=13
            'print("set new a to 13")'
        if shape==3433:
            a=13
            'print("set new a to 13")'
        if shape==3334:
            a=13
            'print("set new a to 13")'
    if a<=HCP<=14:
        if len(S)<5:
            if len(H)<5:
                if len(C)==3:
                    if len(D)==3:
                        w+=1
                        '''tP+=HCP
                        tH+=len(H)
                        tS+=len(S)
                        tD+=len(D)
                        tC+=len(C)'''
                        count3+=1
                        '''print("S:",strS)
                        print("H:",strH)
                        print("D:",strD)
                        print("C:",strC)
                        print("Shape:",shape)
                        print("HCP:",HCP)
                        print("A valid 1C opening")
                        '''
                elif len(D)<len(C):
                    w+=1
                    '''tP+=HCP
                    tH+=len(H)
                    tS+=len(S)
                    tD+=len(D)
                    tC+=len(C)'''
                    if len(C)==3:
                        count3+=1
                    if len(C)==4:
                        count4+=1
                    if len(C)==5:
                        count5+=1
                    if len(C)>=6:
                        count6+=1
                    '''print("S:",strS)
                    print("H:",strH)
                    print("D:",strD)
                    print("C:",strC)
                    print("Shape:",shape)
                    print("HCP:",HCP)
                    print("A valid 1C opening")
                    '''
    if 15<=HCP<=17:
        if len(S)<5:
            if len(H)<5:
                if len(S)<=1:
                    if len(D)<len(C):
                        w+=1
                        '''tP+=HCP
                        tH+=len(H)
                        tS+=len(S)
                        tD+=len(D)
                        tC+=len(C)'''
                        if len(C)==3:
                            count3+=1
                        if len(C)==4:
                            count4+=1
                        if len(C)==5:
                            count5+=1
                        if len(C)>=6:
                            count6+=1
                    '''print("S:",strS)
                    print("H:",strH)
                    print("D:",strD)
                    print("C:",strC)
                    print("Shape:",shape)
                    print("HCP:",HCP)
                    print("A valid 1C opening")
                    '''
                elif len(H)<=1:
                    if len(D)<len(C):
                        w+=1
                        '''tP+=HCP
                        tH+=len(H)
                        tS+=len(S)
                        tD+=len(D)
                        tC+=len(C)'''
                        if len(C)==3:
                            count3+=1
                        if len(C)==4:
                            count4+=1
                        if len(C)==5:
                            count5+=1
                        if len(C)>=6:
                            count6+=1
                    '''print("S:",strS)
                    print("H:",strH)
                    print("D:",strD)
                    print("C:",strC)
                    print("Shape:",shape)
                    print("HCP:",HCP)
                    print("A valid 1C opening")
                    '''
                elif len(D)<=1:
                    w+=1
                    '''tP+=HCP
                    tH+=len(H)
                    tS+=len(S)
                    tD+=len(D)
                    tC+=len(C)'''
                    if len(C)==3:
                        count3+=1
                    if len(C)==4:
                        count4+=1
                    if len(C)==5:
                        count5+=1
                    if len(C)>=6:
                        count6+=1
                    '''print("S:",strS)
                    print("H:",strH)
                    print("D:",strD)
                    print("C:",strC)
                    print("Shape:",shape)
                    print("HCP:",HCP)
                    print("A valid 1C opening")
                    '''
    if 18<=HCP<=19:
        if len(S)<5:
            if len(H)<5:
                if len(C)==3:
                    if len(D)==3:
                        w+=1
                        '''tP+=HCP
                        tH+=len(H)
                        tS+=len(S)
                        tD+=len(D)
                        tC+=len(C)
                        count3+=1'''
                        '''print("S:",strS)
                        print("H:",strH)
                        print("D:",strD)
                        print("C:",strC)
                        print("Shape:",shape)
                        print("HCP:",HCP)
                        print("A valid 1C opening")
                        '''
                if len(D)<len(C):
                    w+=1
                    '''tP+=HCP
                    tH+=len(H)
                    tS+=len(S)
                    tD+=len(D)
                    tC+=len(C)'''
                    if len(C)==3:
                        count3+=1
                    if len(C)==4:
                        count4+=1
                    if len(C)==5:
                        count5+=1
                    if len(C)>=6:
                        count6+=1  
    if 20<=HCP<=21:
        if len(S)<5:
            if len(H)<5:
                if len(S)<=1:
                    if len(D)<len(C):
                        w+=1
                        '''tP+=HCP
                        tH+=len(H)
                        tS+=len(S)
                        tD+=len(D)
                        tC+=len(C)'''
                        if len(C)==3:
                            count3+=1
                        if len(C)==4:
                            count4+=1
                        if len(C)==5:
                            count5+=1
                        if len(C)>=6:
                            count6+=1
                        '''print("S:",strS)
                        print("H:",strH)
                        print("D:",strD)
                        print("C:",strC)
                        print("Shape:",shape)
                        print("HCP:",HCP)
                        print("A valid 1C opening")
                                '''
                elif len(H)<=1:
                    if len(D)<len(C):
                        w+=1
                        '''tP+=HCP
                        tH+=len(H)
                        tS+=len(S)
                        tD+=len(D)
                        tC+=len(C)'''
                        if len(C)==3:
                            count3+=1
                        if len(C)==4:
                            count4+=1
                        if len(C)==5:
                            count5+=1
                        if len(C)>=6:
                            count6+=1
                        '''print("S:",strS)
                        print("H:",strH)
                        print("D:",strD)
                        print("C:",strC)
                        print("Shape:",shape)
                        print("HCP:",HCP)
                        print("A valid 1C opening")

                    '''
                elif len(D)<=1:
                    w+=1
                    '''tP+=HCP
                    tH+=len(H)
                    tS+=len(S)
                    tD+=len(D)
                    tC+=len(C)'''
                    if len(C)==3:
                        count3+=1
                    if len(C)==4:
                        count4+=1
                    if len(C)==5:
                        count5+=1
                    if len(C)>=6:
                        count6+=1
                        '''print("S:",strS)
                        print("H:",strH)
                        print("D:",strD)
                        print("C:",strC)
                        print("Shape:",shape)
                        print("HCP:",HCP)
                        print("A valid 1C opening")'''
a=12
Ehand=[47,39,36,33,31,23,22,21,13,11,9,7,6]
ES=[47]
EH=[39,36,33,31]
ED=[23,22,21]
EC=[13,11,9,7,6]
strES=["9"]
strEH=["A","J","8","6"]
strED=["J","10","9"]
strEC=["A","Q","10","8","7"]
EHCP=12
Eshape=1435
while x<1000000:
    global card
    global NSraw,SSraw,ESraw,WSraw,NHraw,EHraw,WHraw,SHraw,NDraw,SDraw,WDraw,EDraw,NCraw,SCraw,ECraw,WCraw
    global losers
    card=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52]
    for i in Ehand:
        card.remove(i)
    dis1hand()
    a=12
    w=0
    if x<999999:
        oCopening()
        if w==1:
            x+=1
            NS=S.copy()
            NH=H.copy()
            ND=D.copy()
            NC=C.copy()
            NHCP=HCP
            dis1hand()
            SS=S.copy()
            SH=H.copy()
            SD=D.copy()
            SC=C.copy()
            SHCP=HCP
            dis1hand()
            if len(H)>=3:
                count+=1
            WS=S.copy()
            WH=H.copy()
            WD=D.copy()
            WC=C.copy()
            WHCP=HCP
    elif x==999999:
        card=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52]
        for i in Ehand:
            card.remove(i)
        dis1hand()
        oCopening()
        if w==1:
            x+=1
            NS=S.copy()
            NH=H.copy()
            ND=D.copy()
            NC=C.copy()
            NHCP=HCP
            Nshape=shape
            strNS=[str(i) for i in S]
            strNH=[str(i) for i in H]
            strND=[str(i) for i in D]
            strNC=[str(i) for i in C]
            dis1hand()
            SS=S.copy()
            SH=H.copy()
            SD=D.copy()
            SC=C.copy()
            SHCP=HCP
            strSS=[str(i) for i in S]
            strSH=[str(i) for i in H]
            strSD=[str(i) for i in D]
            strSC=[str(i) for i in C]
            Sshape=shape
            dis1hand()
            if len(H)>=3:
                count+=1
            WS=S.copy()
            WH=H.copy()
            WD=D.copy()
            WC=C.copy()
            WHCP=HCP
            Wshape=shape
            strWS=[str(i) for i in S]
            strWH=[str(i) for i in H]
            strWD=[str(i) for i in D]
            strWC=[str(i) for i in C]
r=count/x*100
print("The probability of getting a fit:",r,"%")
print("The layout of the last board:")
print("North:")
print("S:",strNS)
print("H:",strNH)
print("D:",strND)
print("C:",strNC)
print("Shape:",Nshape)
print("HCP:",NHCP)
'print("LTC",losersN)'
print("East:")
print("S:",strES)
print("H:",strEH)
print("D:",strED)
print("C:",strEC)
print("Shape:",Eshape)
print("HCP:",EHCP)
'print("LTC",losersE)'
print("South:")
print("S:",strSS)
print("H:",strSH)
print("D:",strSD)
print("C:",strSC)
print("Shape:",Sshape)
print("HCP:",SHCP)
'print("LTC",losersS)'
print("West:")
print("S:",strWS)
print("H:",strWH)
print("D:",strWD)
print("C:",strWC)
print("Shape:",Wshape)
print("HCP:",WHCP)
'print("LTC",losersW)'