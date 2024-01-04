import random
import dis4hand
trickS=0
trickN=0
trickW=0
trickE=0
trickd=1
suit=0
#储存整手牌的信息
NSraw1=dis4hand.NSraw
NHraw1=dis4hand.NHraw
NDraw1=dis4hand.NDraw
NCraw1=dis4hand.NCraw
ESraw1=dis4hand.ESraw
EHraw1=dis4hand.EHraw
EDraw1=dis4hand.EDraw
ECraw1=dis4hand.ECraw
WSraw1=dis4hand.WSraw
WHraw1=dis4hand.WHraw
WDraw1=dis4hand.WDraw
WCraw1=dis4hand.WCraw
SSraw1=dis4hand.SSraw
SHraw1=dis4hand.SHraw
SDraw1=dis4hand.SDraw
SCraw1=dis4hand.SCraw
#调出各家在各门花色中的数值
def raw():
    global NSraw,SSraw,ESraw,WSraw,NHraw,EHraw,WHraw,SHraw,NDraw,SDraw,WDraw,EDraw,NCraw,SCraw,ECraw,WCraw
    global NSraw1,SSraw1,ESraw1,WSraw1,NHraw1,EHraw1,WHraw1,SHraw1,NDraw1,SDraw1,WDraw1,EDraw1,NCraw1,SCraw1,ECraw1,WCraw1
    NSraw=dis4hand.NSraw
    NHraw=dis4hand.NHraw
    NDraw=dis4hand.NDraw
    NCraw=dis4hand.NCraw
    ESraw=dis4hand.ESraw
    EHraw=dis4hand.EHraw
    EDraw=dis4hand.EDraw
    ECraw=dis4hand.ECraw
    WSraw=dis4hand.WSraw
    WHraw=dis4hand.WHraw
    WDraw=dis4hand.WDraw
    WCraw=dis4hand.WCraw
    SSraw=dis4hand.SSraw
    SHraw=dis4hand.SHraw
    SDraw=dis4hand.SDraw
    SCraw=dis4hand.SCraw
    '''print(NSraw,NHraw,NDraw,NCraw)
    print(ESraw,EHraw,EDraw,ECraw)
    print(SSraw,SHraw,SDraw,SCraw)
    print(WSraw,WHraw,WDraw,WCraw)'''
    global Nhand,Ehand,Whand,Shand
    Nhand=NSraw+NHraw+NDraw+NCraw
    Ehand=ESraw+EHraw+EDraw+ECraw
    Whand=WSraw+WHraw+WDraw+WCraw
    Shand=SSraw+SHraw+SDraw+SCraw
    'print(Nhand,Shand,Whand,Shand)'
'''raw()'''
#储存单手牌的数据
def refresh():
    global NSraw1,SSraw1,ESraw1,WSraw1,NHraw1,EHraw1,WHraw1,SHraw1,NDraw1,SDraw1,WDraw1,EDraw1,NCraw1,SCraw1,ECraw1,WCraw1
    global NSraw,SSraw,ESraw,WSraw,NHraw,EHraw,WHraw,SHraw,NDraw,SDraw,WDraw,EDraw,NCraw,SCraw,ECraw,WCraw
    NSraw=NSraw1.copy()
    NHraw=NHraw1.copy()
    NDraw=NDraw1.copy()
    NCraw=NCraw1.copy()
    ESraw=ESraw1.copy()
    EHraw=EHraw1.copy()
    EDraw=EDraw1.copy()
    ECraw=ECraw1.copy()
    WSraw=WSraw1.copy()
    WHraw=WHraw1.copy()
    WDraw=WDraw1.copy()
    WCraw=WCraw1.copy()
    SSraw=SSraw1.copy()
    SHraw=SHraw1.copy()
    SDraw=SDraw1.copy()
    SCraw=SCraw1.copy()
    global Nhand,Ehand,Whand,Shand
    Nhand=NSraw+NHraw+NDraw+NCraw
    Ehand=ESraw+EHraw+EDraw+ECraw
    Whand=WSraw+WHraw+WDraw+WCraw
    Shand=SSraw+SHraw+SDraw+SCraw
#出牌以及垫牌的判定：sen 是垫牌或跟牌的函数 suits是判定
def sen(x,d):
    global suit
    global r
    r=x
    'print(r)'
    if d==1:
        if 0<x<14:
            WCraw.remove(r)
            Whand.remove(r)
        if 14<=x<27:
            WDraw.remove(r)
            Whand.remove(r)
        if 27<=x<40:
            WHraw.remove(r)
            Whand.remove(r)
        if 40<=x<53:
            WSraw.remove(r)
            Whand.remove(r)
    if d==2:
        if 0<x<14:
            NCraw.remove(r)
            Nhand.remove(r)
        if 14<=x<27:
            NDraw.remove(r)
            Nhand.remove(r)
        if 27<=x<40:
            NHraw.remove(r)
            Nhand.remove(r)
        if 40<=x<53:
            NSraw.remove(r)
            Nhand.remove(r)
    if d==3:
        if 0<x<14:
            ECraw.remove(r)
            Ehand.remove(r)
        if 14<=x<27:
            EDraw.remove(r)
            Ehand.remove(r)
        if 27<=x<40:
            EHraw.remove(r)
            Ehand.remove(r)
        if 40<=x<53:
            ESraw.remove(r)
            Ehand.remove(r)
    if d==4:
        if 0<x<14:
            SCraw.remove(r)
            Shand.remove(r)
        if 14<=x<27:
            SDraw.remove(r)
            Shand.remove(r)
        if 27<=x<40:
            SHraw.remove(r)
            Shand.remove(r)
        if 40<=x<53:
            SSraw.remove(r)
            Shand.remove(r)
def suits(a):
    global suit
    global trickd
    global r1
    if trickd==1:
        if 0<a<14:
            suit=1
            WCraw.remove(r1)
            Whand.remove(r1)
        elif 14<=a<27:
            suit=2
            WDraw.remove(r1)
            Whand.remove(r1)
        elif 27<=a<40:
            suit=3
            WHraw.remove(r1)
            Whand.remove(r1)
        elif 40<=a<53:
            suit=4
            WSraw.remove(r1)
            Whand.remove(r1)
    elif trickd==2:
        if 0<a<14:
            suit=1
            NCraw.remove(r1)
            Nhand.remove(r1)
        elif 14<=a<27:
            suit=2
            NDraw.remove(r1)
            Nhand.remove(r1)
        elif 27<=a<40:
            suit=3
            NHraw.remove(r1)
            Nhand.remove(r1)
        elif 40<=a<53:
            suit=4
            NSraw.remove(r1)
            Nhand.remove(r1)
    elif trickd==3:
        if 0<a<14:
            suit=1
            ECraw.remove(r1)
            Ehand.remove(r1)
        elif 14<=a<27:
            suit=2
            EDraw.remove(r1)
            Ehand.remove(r1)
        elif 27<=a<40:
            suit=3
            EHraw.remove(r1)
            Ehand.remove(r1)
        elif 40<=a<53:
            suit=4
            ESraw.remove(r1)
            Ehand.remove(r1)
    elif trickd==4:
        if 0<a<14:
            suit=1
            SCraw.remove(r1)
            Shand.remove(r1)
        elif 14<=a<27:
            suit=2
            SDraw.remove(r1)
            Shand.remove(r1)
        elif 27<=a<40:
            suit=3
            SHraw.remove(r1)
            Shand.remove(r1)
        elif 40<=a<53:
            suit=4
            SSraw.remove(r1)
            Shand.remove(r1)
#比大小
def turn():
    global trickW,trickN,trickE,trickS,trickd
    global suit
    global trick
    a=max(trick)
    '''print(suit)'''
    b=True
    if suit==1:
        while b:
            if a>13:
                trick.remove(a)
                a=max(trick)
            if a<=13:
                b=False
    elif suit==2:
        while b:
            if 13<a<=26:
                b=False
            else:
                trick.remove(a)
                a=max(trick)
    elif suit==3:
        while b:
            if 26<a<=39:
                b=False
            else:
                trick.remove(a)
                a=max(trick)
    elif suit==4:
        while b:
            if 39<a<=52:
                b=False
            else:
                trick.remove(a)
                a=max(trick)
    '''print(a)
    print(trickd)'''
    if trickd==1:
        if a==r1:
            trickW+=1
            trickd=1
        elif a==r2:
            trickN+=1
            trickd=2
        elif a==r3:
            trickE+=1
            trickd=3
        elif a==r4:
            trickS+=1
            trickd=4
    elif trickd==2:
        if a==r4:
            trickW+=1
            trickd=1
        elif a==r1:
            trickN+=1
            trickd=2
        elif a==r2:
            trickE+=1
            trickd=3
        elif a==r3:
            trickS+=1
            trickd=4
    elif trickd==3:
        if a==r3:
            trickW+=1
            trickd=1
        elif a==r4:
            trickN+=1
            trickd=2
        elif a==r1:
            trickE+=1
            trickd=3
        elif a==r2:
            trickS+=1
            trickd=4
    elif trickd==4:
        if a==r2:
            trickW+=1
            trickd=1
        elif a==r3:
            trickN+=1
            trickd=2
        elif a==r4:
            trickE+=1
            trickd=3
        elif a==r1:
            trickS+=1
            trickd=4
def displayc():
    global r1,r2,r3,r4
    global trick
    global display
    trick=[r1,r2,r3,r4]
    display=trick.copy()
    for i in range(4):
        l=trick[i]
        if 0<l<10:
            k=l+1
            m="C"+str(k)
            display.pop(i)
            display.insert(i,m)
        if l==10:
            m="CJ"
            display.pop(i)
            display.insert(i,m)    
        if l==11:
            m="CQ"
            display.pop(i)
            display.insert(i,m)
        if l==12:
            m="CK"
            display.pop(i)
            display.insert(i,m)  
        if l==13:
            m="CA"
            display.pop(i)
            display.insert(i,m)
        if 13<l<24:
            k=l-12
            m="D"+str(k)
            display.pop(i)
            display.insert(i,m)
        if l==23:
            m="DJ"
            display.pop(i)
            display.insert(i,m)    
        if l==24:
            m="DQ"
            display.pop(i)
            display.insert(i,m)
        if l==25:
            m="DK"
            display.pop(i)
            display.insert(i,m)  
        if l==26:
            m="DA"
            display.pop(i)
            display.insert(i,m)
        if 26<l<36:
            k=l-25
            m="H"+str(k)
            display.pop(i)
            display.insert(i,m)
        if l==36:
            m="HJ"
            display.pop(i)
            display.insert(i,m)    
        if l==37:
            m="HQ"
            display.pop(i)
            display.insert(i,m)
        if l==38:
            m="HK"
            display.pop(i)
            display.insert(i,m)  
        if l==39:
            m="HA"
            display.pop(i)
            display.insert(i,m)
        if 39<l<49:
            k=l-38
            m="S"+str(k)
            display.pop(i)
            display.insert(i,m)
        if l==49:
            m="SJ"
            display.pop(i)
            display.insert(i,m)    
        if l==50:
            m="SQ"
            display.pop(i)
            display.insert(i,m)
        if l==51:
            m="SK"
            display.pop(i)
            display.insert(i,m)  
        if l==52:
            m="SA"
            display.pop(i)
            display.insert(i,m)
    '''print(display)'''
# 进入无将的打牌过程,假设南家坐庄，西家首攻
def SNTplay():
    global r1,r2,r3,r4
    global t
    global trick
    global suit 
    global trickd
    r1=0
    r2=0
    r3=0
    r4=0
    i=int(random.random()*t)
    #利用trickd辨别谁出牌。W-trickd=1 N-trickd=2 E-trickd=3 S-trickd=4
    if trickd==1:
        r1=Whand[i]
        suits(r1)
        if suit==1:
            if len(NCraw)==0:
                i=int(random.random()*t)
                r2=Nhand[i]
                sen(r2,2)
                suit=1
            elif len(NCraw)>0:
                i=int(random.random()*len(NCraw))
                r2=NCraw[i]
                sen(r2,2)
                suit=1
            if len(ECraw)==0:
                i=int(random.random()*t)
                r3=Ehand[i]
                sen(r3,3)
                suit=1
            elif len(ECraw)>0:
                i=int(random.random()*len(ECraw))
                r3=ECraw[i]
                sen(r3,3)
                suit=1
            if len(SCraw)==0:
                i=int(random.random()*t)
                r4=Shand[i]
                sen(r4,4)
                suit=1
            elif len(SCraw)>0:
                i=int(random.random()*len(SCraw))
                r4=SCraw[i]
                sen(r4,4)
                suit=1
        elif suit==2:
            if len(NDraw)==0:
                i=int(random.random()*t)
                r2=Nhand[i]
                sen(r2,2)
                suit=2
            elif len(NDraw)>0:
                i=int(random.random()*len(NDraw))
                r2=NDraw[i]
                sen(r2,2)
                suit=2
            if len(EDraw)==0:
                i=int(random.random()*t)
                r3=Ehand[i]
                sen(r3,3)
                suit=2
            elif len(EDraw)>0:
                i=int(random.random()*len(EDraw))
                r3=EDraw[i]
                sen(r3,3)
                suit=2
            if len(SDraw)==0:
                i=int(random.random()*t)
                r4=Shand[i]
                sen(r4,4)
                suit=2
            elif len(SDraw)>0:
                i=int(random.random()*len(SDraw))
                r4=SDraw[i]
                sen(r4,4)
                suit=2
        elif suit==3:
            if len(NHraw)==0:
                i=int(random.random()*t)
                r2=Nhand[i]
                sen(r2,2)
                suit=3
            elif len(NHraw)>0:
                i=int(random.random()*len(NHraw))
                r2=NHraw[i]
                sen(r2,2)
                suit=3
            if len(EHraw)==0:
                i=int(random.random()*t)
                r3=Ehand[i]
                sen(r3,3)
                suit=3
            elif len(EHraw)>0:
                i=int(random.random()*len(EHraw))
                r3=EHraw[i]
                sen(r3,3)
                suit=3
            if len(SHraw)==0:
                i=int(random.random()*t)
                r4=Shand[i]
                sen(r4,4)
                suit=3
            elif len(SHraw)>0:
                i=int(random.random()*len(SHraw))
                r4=SHraw[i]
                sen(r4,4)
                suit=3
        elif suit==4:
            if len(NSraw)==0:
                i=int(random.random()*t)
                r2=Nhand[i]
                sen(r2,2)
                suit=4
            elif len(NSraw)>0:
                i=int(random.random()*len(NSraw))
                r2=NSraw[i]
                sen(r2,2)
                suit=4
            if len(ESraw)==0:
                i=int(random.random()*t)
                r3=Ehand[i]
                sen(r3,3)
                suit=4
            elif len(ESraw)>0:
                i=int(random.random()*len(ESraw))
                r3=ESraw[i]
                sen(r3,3)
                suit=4
            if len(SSraw)==0:
                i=int(random.random()*t)
                r4=Shand[i]
                sen(r4,4)
                suit=4
            elif len(SSraw)>0:
                i=int(random.random()*len(SSraw))
                r4=SSraw[i]
                sen(r4,4)
                suit=4
    elif trickd==2:
        r1=Nhand[i]
        suits(r1)
        if suit==1:
            if len(ECraw)==0:
                i=int(random.random()*t)
                r2=Ehand[i]
                sen(r2,3)
                suit=1
            elif len(ECraw)>0:
                i=int(random.random()*len(ECraw))
                r2=ECraw[i]
                sen(r2,3)
                suit=1
            if len(SCraw)==0:
                i=int(random.random()*t)
                r3=Shand[i]
                sen(r3,4)
                suit=1
            elif len(SCraw)>0:
                i=int(random.random()*len(SCraw))
                r3=SCraw[i]
                sen(r3,4)
                suit=1
            if len(WCraw)==0:
                i=int(random.random()*t)
                r4=Whand[i]
                sen(r4,1)
                suit=1
            elif len(WCraw)>0:
                i=int(random.random()*len(WCraw))
                r4=WCraw[i]
                sen(r4,1)
                suit=1
        elif suit==2:
            if len(EDraw)==0:
                i=int(random.random()*t)
                r2=Ehand[i]
                sen(r2,3)
                suit=2
            elif len(EDraw)>0:
                i=int(random.random()*len(EDraw))
                r2=EDraw[i]
                sen(r2,3)
                suit=2
            if len(SDraw)==0:
                i=int(random.random()*t)
                r3=Shand[i]
                sen(r3,4)
                suit=2
            elif len(SDraw)>0:
                i=int(random.random()*len(SDraw))
                r3=SDraw[i]
                sen(r3,4)
                suit=2
            if len(WDraw)==0:
                i=int(random.random()*t)
                r4=Whand[i]
                sen(r4,1)
                suit=2
            elif len(WDraw)>0:
                i=int(random.random()*len(WDraw))
                r4=WDraw[i]
                sen(r4,1)
                suit=2
        elif suit==3:
            if len(EHraw)==0:
                i=int(random.random()*t)
                r2=Ehand[i]
                sen(r2,3)
                suit=3
            elif len(EHraw)>0:
                i=int(random.random()*len(EHraw))
                r2=EHraw[i]
                sen(r2,3)
                suit=3
            if len(SHraw)==0:
                i=int(random.random()*t)
                r3=Shand[i]
                sen(r3,4)
                suit=3
            elif len(SHraw)>0:
                i=int(random.random()*len(SHraw))
                r3=SHraw[i]
                sen(r3,4)
                suit=3
            if len(WHraw)==0:
                i=int(random.random()*t)
                r4=Whand[i]
                sen(r4,1)
                suit=3
            elif len(WHraw)>0:
                i=int(random.random()*len(WHraw))
                r4=WHraw[i]
                sen(r4,1)
                suit=3
        elif suit==4:
            if len(ESraw)==0:
                i=int(random.random()*t)
                r2=Ehand[i]
                sen(r2,3)
                suit=4
            elif len(ESraw)>0:
                i=int(random.random()*len(ESraw))
                r2=ESraw[i]
                sen(r2,3)
                suit=4
            if len(SSraw)==0:
                i=int(random.random()*t)
                r3=Shand[i]
                sen(r3,4)
                suit=4
            elif len(SSraw)>0:
                i=int(random.random()*len(SSraw))
                r3=SSraw[i]
                sen(r3,4)
                suit=4
            if len(WSraw)==0:
                i=int(random.random()*t)
                r4=Whand[i]
                sen(r4,1)
                suit=4
            elif len(WSraw)>0:
                i=int(random.random()*len(WSraw))
                r4=WSraw[i]
                sen(r4,1)
                suit=4
    elif trickd==3:
        r1=Ehand[i]
        suits(r1)
        if suit==1:
            if len(SCraw)==0:
                i=int(random.random()*t)
                r2=Shand[i]
                sen(r2,4)
                suit=1
            elif len(SCraw)>0:
                i=int(random.random()*len(SCraw))
                r2=SCraw[i]
                sen(r2,4)
                suit=1
            if len(WCraw)==0:
                i=int(random.random()*t)
                r3=Whand[i]
                sen(r3,1)
                suit=1
            elif len(WCraw)>0:
                i=int(random.random()*len(WCraw))
                r3=WCraw[i]
                sen(r3,1)
                suit=1
            if len(NCraw)==0:
                i=int(random.random()*t)
                r4=Nhand[i]
                sen(r4,2)
                suit=1
            elif len(NCraw)>0:
                i=int(random.random()*len(NCraw))
                r4=NCraw[i]
                sen(r4,2)
                suit=1
        elif suit==2:
            if len(SDraw)==0:
                i=int(random.random()*t)
                r2=Shand[i]
                sen(r2,4)
                suit=2
            elif len(SDraw)>0:
                i=int(random.random()*len(SDraw))
                r2=SDraw[i]
                sen(r2,4)
                suit=2
            if len(WDraw)==0:
                i=int(random.random()*t)
                r3=Whand[i]
                sen(r3,1)
                suit=2
            elif len(WDraw)>0:
                i=int(random.random()*len(WDraw))
                r3=WDraw[i]
                sen(r3,1)
                suit=2
            if len(NDraw)==0:
                i=int(random.random()*t)
                r4=Nhand[i]
                sen(r4,2)
                suit=2
            elif len(NDraw)>0:
                i=int(random.random()*len(NDraw))
                r4=NDraw[i]
                sen(r4,2)
                suit=2
        elif suit==3:
            if len(SHraw)==0:
                i=int(random.random()*t)
                r2=Shand[i]
                sen(r2,4)
                suit=3
            elif len(SHraw)>0:
                i=int(random.random()*len(SHraw))
                r2=SHraw[i]
                sen(r2,4)
                suit=3
            if len(WHraw)==0:
                i=int(random.random()*t)
                r3=Whand[i]
                sen(r3,1)
                suit=3
            elif len(WHraw)>0:
                i=int(random.random()*len(WHraw))
                r3=WHraw[i]
                sen(r3,1)
                suit=3
            if len(NHraw)==0:
                i=int(random.random()*t)
                r4=Nhand[i]
                sen(r4,2)
                suit=3
            elif len(NHraw)>0:
                i=int(random.random()*len(NHraw))
                r4=NHraw[i]
                sen(r4,2)
                suit=3
        elif suit==4:
            if len(SSraw)==0:
                i=int(random.random()*t)
                r2=Shand[i]
                sen(r2,4)
                suit=4
            elif len(SSraw)>0:
                i=int(random.random()*len(SSraw))
                r2=SSraw[i]
                sen(r2,4)
                suit=4
            if len(WSraw)==0:
                i=int(random.random()*t)
                r3=Whand[i]
                sen(r3,1)
                suit=4
            elif len(WSraw)>0:
                i=int(random.random()*len(WSraw))
                r3=WSraw[i]
                sen(r3,1)
                suit=4
            if len(NSraw)==0:
                i=int(random.random()*t)
                r4=Nhand[i]
                sen(r4,2)
                suit=4
            elif len(NSraw)>0:
                i=int(random.random()*len(NSraw))
                r4=NSraw[i]
                sen(r4,2)
                suit=4
    elif trickd==4:
        r1=Shand[i]
        suits(r1)
        if suit==1:
            if len(WCraw)==0:
                i=int(random.random()*t)
                r2=Whand[i]
                sen(r2,1)
                suit=1
            elif len(WCraw)>0:
                i=int(random.random()*len(WCraw))
                r2=WCraw[i]
                sen(r2,1)
                suit=1
            if len(NCraw)==0:
                i=int(random.random()*t)
                r3=Nhand[i]
                sen(r3,2)
                suit=1
            elif len(NCraw)>0:
                i=int(random.random()*len(NCraw))
                r3=NCraw[i]
                sen(r3,2)
                suit=1
            if len(ECraw)==0:
                i=int(random.random()*t)
                r4=Ehand[i]
                sen(r4,3)
                suit=1
            elif len(ECraw)>0:
                i=int(random.random()*len(ECraw))
                r4=ECraw[i]
                sen(r4,3)
                suit=1
        elif suit==2:
            if len(WDraw)==0:
                i=int(random.random()*t)
                r2=Whand[i]
                sen(r2,1)
                suit=2
            elif len(WDraw)>0:
                i=int(random.random()*len(WDraw))
                r2=WDraw[i]
                sen(r2,1)
                suit=2
            if len(NDraw)==0:
                i=int(random.random()*t)
                r3=Nhand[i]
                sen(r3,2)
                suit=2
            elif len(NDraw)>0:
                i=int(random.random()*len(NDraw))
                r3=NDraw[i]
                sen(r3,2)
                suit=2
            if len(EDraw)==0:
                i=int(random.random()*t)
                r4=Ehand[i]
                sen(r4,3)
                suit=2
            elif len(EDraw)>0:
                i=int(random.random()*len(EDraw))
                r4=EDraw[i]
                sen(r4,3)
                suit=2
        elif suit==3:
            if len(WHraw)==0:
                i=int(random.random()*t)
                r2=Whand[i]
                sen(r2,1)
                suit=3
            elif len(WHraw)>0:
                i=int(random.random()*len(WHraw))
                r2=WHraw[i]
                sen(r2,1)
                suit=3
            if len(NHraw)==0:
                i=int(random.random()*t)
                r3=Nhand[i]
                sen(r3,2)
                suit=3
            elif len(NHraw)>0:
                i=int(random.random()*len(NHraw))
                r3=NHraw[i]
                sen(r3,2)
                suit=3
            if len(EHraw)==0:
                i=int(random.random()*t)
                r4=Ehand[i]
                sen(r4,3)
                suit=3
            elif len(EHraw)>0:
                i=int(random.random()*len(EHraw))
                r4=EHraw[i]
                sen(r4,3)
                suit=3
        elif suit==4:
            if len(WSraw)==0:
                i=int(random.random()*t)
                r2=Whand[i]
                sen(r2,1)
                suit=4
            elif len(WSraw)>0:
                i=int(random.random()*len(WSraw))
                r2=WSraw[i]
                sen(r2,1)
                suit=4
            if len(NSraw)==0:
                i=int(random.random()*t)
                r3=Nhand[i]
                sen(r3,2)
                suit=4
            elif len(NSraw)>0:
                i=int(random.random()*len(NSraw))
                r3=NSraw[i]
                sen(r3,2)
                suit=4
            if len(ESraw)==0:
                i=int(random.random()*t)
                r4=Ehand[i]
                sen(r4,3)
                suit=4
            elif len(ESraw)>0:
                i=int(random.random()*len(ESraw))
                r4=ESraw[i]
                sen(r4,3)
                suit=4
    displayc()
    '''print(display)
    print(trick)'''

    turn()
def SNTplayi():
    global r1,r2,r3,r4
    global t
    global trick
    global suit 
    global trickd
    r1=0
    r2=0
    r3=0
    r4=0
    if trickd==1:
        for i in range(t):
            r1=Whand[i]
            sen(r1,1)
            suits(r1)
            if suit==1:
                k=len(NCraw)
                if k>0:
                    for i in range(k):
                        r2=NCraw[i]
                        sen(r2,2)
                        k=len(ECraw)
                        if k>0:
                            for i in range(k):
                                r3=ECraw[i]
                                sen(r3,3)
                                k=len(SCraw)
                                if k>0:
                                    for i in range(k):
                                        r4=SCraw[i]
                                        sen(r4,4)
                                        trick=[r1,r2,r3,r4]
                                        turn()
                                elif k==0:
                                    for i in range(t):
                                        r4=Shand[i]
                                        sen(r4,4)
                                        trick=[r1,r2,r3,r4]
                                        turn()
                        elif k==0:
                                for i in range(t):
                                    r3=Ehand[i]
                                    sen(r3,3)
                                    k=len(SCraw)
                                    if k>0:
                                        for i in range(k):
                                            r4=SCraw[i]
                                            sen(r4,4)
                                            trick=[r1,r2,r3,r4]
                                            turn()
                                    elif k==0:
                                        for i in range(t):
                                            r4=Shand[i]
                                            sen(r4,4)
                                            trick=[r1,r2,r3,r4]
                                            turn()
                elif k==0:
                    for i in range(t):
                        r2=Nhand[t]
                        sen(r2,2)
                        k=len(ECraw)
                        if k>0:
                            for i in range(k):
                                r3=ECraw[i]
                                sen(r3,3)
                                k=len(SCraw)
                                if k>0:
                                    for i in range(k):
                                        r4=SCraw[i]
                                        sen(r4,4)
                                        trick=[r1,r2,r3,r4]
                                        turn()
                                elif k==0:
                                    for i in range(t):
                                        r4=Shand[i]
                                        sen(r4,4)
                                        trick=[r1,r2,r3,r4]
                                        turn()
                        elif k==0:
                                for i in range(t):
                                    r3=Ehand[i]
                                    sen(r3,3)
                                    k=len(SCraw)
                                    if k>0:
                                        for i in range(k):
                                            r4=SCraw[i]
                                            sen(r4,4)
                                            trick=[r1,r2,r3,r4]
                                            turn()
                                    elif k==0:
                                        for i in range(t):
                                            r4=Shand[i]
                                            sen(r4,4)
                                            trick=[r1,r2,r3,r4]
                                            turn()
    elif trickd==2:
        for i in range(t):
            r1=Nhand[i]
            sen(r1,2)
            suits(r1)
            if suit==1:
                k=len(ECraw)
                if k>0:
                    for i in range(k):
                        r2=ECraw[i]
                        sen(r2,3)
                        k=len(SCraw)
                        if k>0:
                            for i in range(k):
                                r3=SCraw[i]
                                sen(r3,4)
                                k=len(WCraw)
                                if k>0:
                                    for i in range(k):
                                        r4=WCraw[i]
                                        sen(r4,1)
                                        turn()
                                elif k==0:
                                    for i in range(t):
                                        r4=Whand[i]
                                        sen(r4,1)
                                        turn()
                        elif k==0:
                                for i in range(t):
                                    r3=Shand[i]
                                    sen(r3,4)
                                    k=len(WCraw)
                                    if k>0:
                                        for i in range(k):
                                            r4=WCraw[i]
                                            sen(r4,1)
                                            turn()
                                    elif k==0:
                                        for i in range(t):
                                            r4=Whand[i]
                                            sen(r4,1)
                                            turn()
                elif k==0:
                    for i in range(t):
                        r2=Ehand[i]
                        sen(r2,3)
                        k=len(SCraw)
                        if k>0:
                            for i in range(k):
                                r3=SCraw[i]
                                sen(r3,4)
                                k=len(WCraw)
                                if k>0:
                                    for i in range(k):
                                        r4=WCraw[i]
                                        sen(r4,1)
                                        turn()
                                elif k==0:
                                    for i in range(t):
                                        r4=Whand[i]
                                        sen(r4,1)
                                        turn()
                        elif k==0:
                                for i in range(t):
                                    r3=Shand[i]
                                    sen(r3,4)
                                    k=len(WCraw)
                                    if k>0:
                                        for i in range(k):
                                            r4=WCraw[i]
                                            sen(r4,1)
                                            turn()
                                    elif k==0:
                                        for i in range(t):
                                            r4=Whand[i]
                                            sen(r4,1)
                                            turn()
    elif trickd==3:
        for i in range(t):
            r1=Ehand[i]
            sen(r1,3)
            suits(r1)
            if suit==1:
                k=len(ECraw)
                if k>0:
                    for i in range(k):
                        r2=SCraw[i]
                        sen(r2,4)
                        k=len(WCraw)
                        if k>0:
                            for i in range(k):
                                r3=WCraw[i]
                                sen(r3,1)
                                k=len(NCraw)
                                if k>0:
                                    for i in range(k):
                                        r4=NCraw[i]
                                        sen(r4,2)
                                        trick=[r1,r2,r3,r4]
                                        turn()
                                elif k==0:
                                    for i in range(t):
                                        r4=Nhand[i]
                                        sen(r4,2)
                                        trick=[r1,r2,r3,r4]
                                        turn()
                        elif k==0:
                                for i in range(t):
                                    r3=Whand[i]
                                    sen(r3,1)
                                    k=len(NCraw)
                                    if k>0:
                                        for i in range(k):
                                            r4=NCraw[i]
                                            sen(r4,2)
                                            trick=[r1,r2,r3,r4]
                                            turn()
                                    elif k==0:
                                        for i in range(t):
                                            r4=Nhand[i]
                                            sen(r4,2)
                                            trick=[r1,r2,r3,r4]
                                            turn()
                elif k==0:
                    for i in range(t):
                        r2=Shand[i]
                        sen(r2,4)
                        k=len(WCraw)
                        if k>0:
                            for i in range(k):
                                r3=WCraw[i]
                                sen(r3,1)
                                k=len(NCraw)
                                if k>0:
                                    for i in range(k):
                                        r4=NCraw[i]
                                        sen(r4,2)
                                        trick=[r1,r2,r3,r4]
                                        turn()
                                elif k==0:
                                    for i in range(t):
                                        r4=Nhand[i]
                                        sen(r4,2)
                                        trick=[r1,r2,r3,r4]
                                        turn()
                        elif k==0:
                                for i in range(t):
                                    r3=Whand[i]
                                    sen(r3,1)
                                    k=len(NCraw)
                                    if k>0:
                                        for i in range(k):
                                            r4=NCraw[i]
                                            sen(r4,2)
                                            trick=[r1,r2,r3,r4]
                                            turn()
                                    elif k==0:
                                        for i in range(t):
                                            r4=Nhand[i]
                                            sen(r4,2)
                                            trick=[r1,r2,r3,r4]
                                            turn()
    elif trickd==4:
        for i in range(t):
            r1=Shand[i]
            sen(r1,4)
            suits(r1)
            if suit==1:
                k=len(WCraw)
                if k>0:
                    for i in range(k):
                        r2=WCraw[i]
                        sen(r2,1)
                        k=len(NCraw)
                        if k>0:
                            for i in range(k):
                                r3=NCraw[i]
                                sen(r3,2)
                                k=len(ECraw)
                                if k>0:
                                    for i in range(k):
                                        r4=ECraw[i]
                                        sen(r4,3)
                                        trick=[r1,r2,r3,r4]
                                        turn()
                                elif k==0:
                                    for i in range(t):
                                        r4=Ehand[i]
                                        sen(r4,3)
                                        trick=[r1,r2,r3,r4]
                                        turn()
                        elif k==0:
                                for i in range(t):
                                    r3=Nhand[i]
                                    sen(r3,2)
                                    k=len(ECraw)
                                    if k>0:
                                        for i in range(k):
                                            r4=ECraw[i]
                                            sen(r4,3)
                                            trick=[r1,r2,r3,r4]
                                            turn()
                                    elif k==0:
                                        for i in range(t):
                                            r4=Ehand[i]
                                            sen(r4,3)
                                            trick=[r1,r2,r3,r4]
                                            turn()
                elif k==0:
                    for i in range(t):
                        r2=Whand[i]
                        sen(r2,1)
                        k=len(NCraw)
                        if k>0:
                            for i in range(k):
                                r3=NCraw[i]
                                sen(r3,2)
                                k=len(ECraw)
                                if k>0:
                                    for i in range(k):
                                        r4=ECraw[i]
                                        sen(r4,3)
                                        trick=[r1,r2,r3,r4]
                                        turn()
                                elif k==0:
                                    for i in range(t):
                                        r4=Ehand[i]
                                        sen(r4,3)
                                        trick=[r1,r2,r3,r4]
                                        turn()
                        elif k==0:
                                for i in range(t):
                                    r3=Nhand[i]
                                    sen(r3,2)
                                    k=len(ECraw)
                                    if k>0:
                                        for i in range(k):
                                            r4=ECraw[i]
                                            sen(r4,3)
                                            trick=[r1,r2,r3,r4]
                                            turn()
                                    elif k==0:
                                        for i in range(t):
                                            r4=Ehand[i]
                                            sen(r4,3)
                                            trick=[r1,r2,r3,r4]
                                            turn()
def Scomplete(w):
    raw()
    refresh()
    global t
    global trickN
    global trickS
    global trickE
    global trickW
    global trickd
    t=13
    for q in range(w):
        refresh()
        trickd=1
        t=13
        while t>0:
            SNTplay()
            t+=-1
            trickNS=trickN+trickS
            trickEW=trickE+trickW
        print("NS total tricks:",trickNS)
        print("EW total tricks:",trickEW)
        trickEW=0
        trickNS=0
        trickE=0
        trickN=0
        trickW=0
        trickS=0
bo=input("board:")
boo=int(bo)
Scomplete(boo)
