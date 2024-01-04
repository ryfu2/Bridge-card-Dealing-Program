import random
def dis1hand():
    global i
    global C
    global D
    global H
    global S
    global HCP
    global losers
    i=0
    losers=0
    C=[]
    D=[]
    H=[]
    S=[]
    HCP=0
    card=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52]
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
    global shape
    shape=1000*len(S)+100*len(H)+10*len(D)+1*len(C)
    if shape<1000:
        shape="0"+str(shape)
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
    strS=[str(i) for i in S]
    strH=[str(i) for i in H]
    strD=[str(i) for i in D]
    strC=[str(i) for i in C]
    strt=[strS,strH,strD,strC]
    for i in strt:
        o=[]
        if len(i)==1:
            if i[0]=="A":
                losers+=0
            elif i[0]=="-":
                losers+=0
            else:
                losers+=1
        elif len(i)==2:
            if i[0]=="A":
                if i[1]=="K":
                    losers+=0
                else:
                    losers+=1
            elif i[0]=="K":
                losers+=1
            else:
                losers+=2
        elif len(i)>=3:
            o=[i[0],i[1],i[2]]
            if o[0]=="A":
                if o[1]=="K":
                    if o[2]=="Q":
                        losers+=0
                    else:
                        losers+=1
                elif o[1]=="Q":
                    losers+=1
                else:
                    losers+=2
            elif o[0]=="K":
                if o[1]=="Q":
                    losers+=1
                else:
                    losers+=2
            elif o[0]=="Q":
                if o[1]=="J":
                    losers+=2
                else:
                    losers+=2.5
            else:
                losers+=3
    '''print("S:",strS)
    print("H:",strH)
    print("D:",strD)
    print("C:",strC)
    print("Shape:",shape)
    print("HCP:",HCP)
    print("LTC",losers)'''
dis1hand()


