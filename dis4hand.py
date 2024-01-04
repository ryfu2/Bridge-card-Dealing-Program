#调用随机函数
import random
def dis1hand():
    #给各门花色设置变量并让所有变量成为全局变量
    global i
    global C
    global D
    global H
    global S
    global HCP
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
def dis4hand():
    global card
    global NSraw,SSraw,ESraw,WSraw,NHraw,EHraw,WHraw,SHraw,NDraw,SDraw,WDraw,EDraw,NCraw,SCraw,ECraw,WCraw
    card=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52]
    dis1hand()
    NS=S.copy()
    NH=H.copy()
    ND=D.copy()
    NC=C.copy()
    NSraw=Sraw.copy()
    NHraw=Hraw.copy()
    NDraw=Draw.copy()
    NCraw=Craw.copy()
    NHCP=HCP
    Nshape=shape
    strNS=[str(i) for i in S]
    strNH=[str(i) for i in H]
    strND=[str(i) for i in D]
    strNC=[str(i) for i in C]
    print("North:")
    print("S:",strNS)
    print("H:",strNH)
    print("D:",strND)
    print("C:",strNC)
    print("Shape:",Nshape)
    print("HCP:",NHCP)
    print(NSraw,NHraw,NDraw,NCraw)
    dis1hand()
    ES=S.copy()
    EH=H.copy()
    ED=D.copy()
    EC=C.copy()
    ESraw=Sraw.copy()
    EHraw=Hraw.copy()
    EDraw=Draw.copy()
    ECraw=Craw.copy()
    EHCP=HCP
    Eshape=shape
    strES=[str(i) for i in S]
    strEH=[str(i) for i in H]
    strED=[str(i) for i in D]
    strEC=[str(i) for i in C]
    print("East:")
    print("S:",strES)
    print("H:",strEH)
    print("D:",strED)
    print("C:",strEC)
    print("Shape:",Eshape)
    print("HCP:",EHCP)
    print(ESraw,EHraw,EDraw,ECraw)
    dis1hand()
    SS=S.copy()
    SH=H.copy()
    SD=D.copy()
    SC=C.copy()
    SSraw=Sraw.copy()
    SHraw=Hraw.copy()
    SDraw=Draw.copy()
    SCraw=Craw.copy()
    SHCP=HCP
    Sshape=shape
    strSS=[str(i) for i in S]
    strSH=[str(i) for i in H]
    strSD=[str(i) for i in D]
    strSC=[str(i) for i in C]
    print("South:")
    print("S:",strSS)
    print("H:",strSH)
    print("D:",strSD)
    print("C:",strSC)
    print("Shape:",Sshape)
    print("HCP:",SHCP)
    print(SSraw,SHraw,SDraw,SCraw)
    dis1hand()
    WS=S.copy()
    WH=H.copy()
    WD=D.copy()
    WC=C.copy()
    WSraw=Sraw.copy()
    WHraw=Hraw.copy()
    WDraw=Draw.copy()
    WCraw=Craw.copy()
    WHCP=HCP
    Wshape=shape
    strWS=[str(i) for i in S]
    strWH=[str(i) for i in H]
    strWD=[str(i) for i in D]
    strWC=[str(i) for i in C]
    print("West:")
    print("S:",strWS)
    print("H:",strWH)
    print("D:",strWD)
    print("C:",strWC)
    print("Shape:",Wshape)
    print("HCP:",WHCP)
    '''print(WSraw,WHraw,WDraw,WCraw)
    tHCP=NHCP+EHCP+WHCP+SHCP
    tH=NH+EH+WH+SH
    tS=NS+ES+WS+SS
    tD=ND+ED+WD+SD
    tC=NC+EC+WC+SC
    print("totalHCP",tHCP)
    print(len(tH),len(tS),len(tD),len(tC))'''
dis4hand()
