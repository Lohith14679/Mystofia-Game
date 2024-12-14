import random as r
import csv
import time
def load():
    time.sleep(0.75)
def saved():
    global name
    global classch
    global vilch
    global yhp
    global vhp
    global yum
    global vum
    global item
    f1=open("MystofiaData","r",newline="")
    data=csv.reader(f1)
    name=input("Enter name:")
    passwd=input("Enter password:")
    while True:
        for i in data:
            if i[0]==name:
                if i[1]==passwd:
                    classch=int(i[2])
                    vilch=int(i[3])
                    yhp=int(i[4])
                    vhp=int(i[5])
                    yum=int(i[6])
                    vum=int(i[7])
                    hhp=int(i[8])
                    hp=int(i[9])
                    load()
                    return "Finished" 
        return "Unfinished"
    f1.close()
def save():
    global classch
    global vilch
    global yhp
    global vhp
    global yum
    global vum
    global hhp
    global hp
    f2=open("MystofiaData","a+",newline="")
    csvwriter=csv.writer(f2)
    name=input("Enter name:")
    passwd=input("Enter password:")
    csvwriter.writerow([name,passwd,classch,vilch,yhp,vhp,yum,vum,hhp,hp])
    load()
    print("Game saved")
def kni():
    global yum
    global yhp
    global vhp
    print('''Attacks
1.Sword slash
2.Divine blade
3.Knight's pride''')
    if yum>=3:
        print("4.Ultimate move-Excaliber!!!!!!!!")
    if yum>=5:
        print("5.Ultimate move-God's Slash!!!!!!!!!!!!")
    while True:
      en=int(input("Enter your attack:"))
      load()
      if en==1:
        print("You used Sword slash")
        load()
        print("Opponent loses 450 HP")
        vhp=vhp-450
        break
      elif en==2:
        print("You used Divine blade")
        load()
        print("Opponent loses 475 HP")
        vhp=vhp-475
        break
      elif en==3:
        print("You used Knight's pride")
        load()
        print("You gained 300 HP")
        yhp=yhp+300
        break
      elif en==4 and yum>=3:
        print("You used Ultimate move-Excaliber!!!!!!!!")
        load()
        print("OPponent loses 775 HP")
        vhp=vhp-775
        yum=yum-3
        break
      elif en==5 and yum>=5:
        print("You used Ultimate move-God's Slash!!!!!!!!!!")
        load()
        print("Opponent loses 1550 HP")
        vhp=vhp-1550
        yum=yum-5
        break
      else:
        load()
        print("Enter valid choice")
def ber():
    global yum
    global yhp
    global vhp
    print('''Attacks
1.Rage
2.Stomp
3.Roar''')
    if yum>=3:
        print("4.Ultimate move-Raging dash!!!!!!!!!!")
    if yum>=5:
        print("5.Ultimate move-Maddness!!!!!!!!!!!!")
    while True:
      en=int(input("Enter your attack:"))
      load()
      if en==1:
        print("You used Rage")
        load()
        print("Opponent loses 400 HP")
        vhp=vhp-400
        break
      elif en==2:
        print("You used Stomp")
        load()
        print("OPponent loses 475 HP")
        vhp=vhp-475
        break
      elif en==3:
        print("You used Roar")
        load()
        print("Opponent loses 300 HP")
        vhp=vhp-300
        break
      elif en==4 and yum>=3:
        print("You used Ultimate move-Raging dash!!!!!!!!!!")
        load()
        print("Opponent loses 800 HP")
        vhp=vhp-800
        yum=yum-3
        break
      elif en==5 and yum>=5:
        print("You used Ultimate move-Maddness!!!!!!!!!!!!")
        load()
        print("Opponent loses 1700 HP")
        vhp=vhp-1700
        yum=yum-5
        break
      else:
        load()
        print("Enter vaild choice")
def ass():
    global yum
    global yhp
    global vhp
    print('''Attacks
1.Kill
2.Silence
3.Poison''')
    if yum>=3:
        print("4.Ultimate move-Execution!!!!!!!!!!")
    if yum>=5:
        print("5.Ultimate move-Countdown to Death!!!!!!!!!!!!!!")
    while True:
      en=int(input("Enter your attack:"))
      load()
      if en==1:
        print("You used Kill")
        load()
        print("Opponent loses 400 HP")
        vhp=vhp-400
        break
      elif en==2:
        print("You used Silence")
        load()
        print("Opponent loses 480 HP")
        vhp=vhp-480
        break
      elif en==3:
        print("You used Poison")
        load()
        print("Opponent loses 465 HP") 
        vhp=vhp-465
        break
      elif en==4 and yum>=3:
        print("You used Ultimate move-Execution!!!!!!!!!!")
        load()
        print("Opponent loses 750 HP")
        vhp=vhp-750
        yum=yum-3
        break
      elif en==5 and yum>=5:
        print("You used Ultimate move-Countdown to Death!!!!!!!!!!!!!!!")
        load()
        print("Opponent loses 1750 HP")
        vhp=vhp-1750
        yum=yum-5
        break
      else:
          load()
          print("Enter valid choice")
def arc():
    global yum
    global yhp
    global vhp
    print('''Attacks
1.Fire arrow
2.Ice irrow
3.Explosive arrow ''')
    if yum>=3:
        print("4.Ultimate Move-Thousand arrows!!!!!!!!!!")
    if yum>=5:
        print("5.Ultimate Move-One million arrows!!!!!!!!!!!")
    while True:
        en=int(input("Enter your attack:"))
        load()
        if en==1:
          print("You used Fire arrow")
          load()
          print("Opponent loses 475 HP")
          vhp=vhp-475
          break
        elif en==2:
          print("You used Ice arrow")
          load()
          print("Opponent loses 460 HP")
          vhp=vhp-460
          break
        elif en==3:
          print("You used Explosive arrow")
          load()
          print("Opponent loses 480 HP")
          vhp=vhp-450
          break
        elif en==4 and yum>=3:
          print("You used Ultimate Move-Thousand arrows!!!!!!!!!!")
          load()
          print("Opponent loses 875 HP")      
          vhp=vhp-875
          yum=yum-3
          break
        elif en==5 and yum>=5:
          print("You used Ultimate Move-One million arrows!!!!!!!!!!!")
          load()
          print("Opponent loses 1750 HP")      
          vhp=vhp-1750
          yum=yum-5
          break
        else:
            load()
            print("Enter valid choice")  
def cas():
    global yum
    global yhp
    global vhp
    print('''Attacks
1.Explosion
2.Heal
3.Curse''')
    if yum>=3:
        print("4.Ultimaye move-Elemental strike!!!!!!!!!!")
    if yum>=5:
        print("5.Ultimate move-Black hole!!!!!!!!!!!!!!")
    while True:
      en=int(input("Enter your attack:"))
      load()
      if en==1:
        print("You used Explosion")
        load()
        print("Opponent loses 445 HP")
        vhp=vhp-445
        break
      elif en==2:
        print("You used Heal")
        load()
        print("You recovered 380 HP")
        yhp=yhp+380
        break
      elif en==3:
        print("You used Curse")
        load()
        print("Opponent loses 375 HP")
        vhp=vhp-375
        break
      elif en==4 and yum>=3:
        print("You used Ultimaye move-Elemental strike!!!!!!!!!!")
        load()
        print("Opponent loses 890 HP")
        vhp=vhp-890
        yum=yum-3
        break
      elif en==5 and yum>=5:
          print("You used Ultimate move-Black hole!!!!!!!!!!!!!!")
          load()
          print("Opponent loses 1825 HP")
          vhp=vhp-1825
          yum=yum-5
          break
      else:
          load()
          print("Enter valid choice") 
def vam():
    global vum
    global yhp
    global vhp
    a=r.randint(1,5)
    if vum>=5:
        print("Ultimate Move-Bloody Moon!!!!!!!!!!!")
        load()
        print("You lose 1700 HP")
        yhp=yhp-1700
        vum=vum-5
    elif a==3 and vum>=3:
        print("Ultimate Move-Endless Night!!!!!!!")
        load()
        print("You lose 750 HP")
        yhp=yhp-750
        vum=vum-3
    else:
        l=['Blood suck','Death scream','Bloody claws']
        n=r.randint(0,2)
        print("Opponent used",l[n])
        load()
        if n==0:
          print("You lose 250 HP")
          print("Opponent gains 250 HP")
          yhp=yhp-250
          vhp=vhp+250
        elif n==1:       
          print("You lose 350 HP")
          yhp=yhp-350
        elif n==2:
          print("You lose 400 HP")  
          yhp=yhp-400
def gho():
    global vum
    global yhp
    global vhp
    a=r.randint(1,5)
    if vum>=5:
        print("Ultimate Move-Kraken!!!!!!!!!!!")
        load()
        print("You lose 1800 HP")
        yhp=yhp-1800
        vum=vum-5
    elif a==3 and vum>=3:        
        print("Ultimate Move-Ghost ship!!!!!!!")
        load()
        print("You lose 800 HP")
        yhp=yhp-800
        vum=vum-3       
    else:
      l=["Curse slash","Gunshot","Walk the plank"]
      n=r.randint(0,2)
      print("Opponent used:",l[n])
      load()
      if n==0:
        print("You lose 375 HP")  
        yhp=yhp-375
      elif n==1:
        print("You lose 450 HP")
        yhp=yhp-450
      elif n==2:
        print("You lose 350 HP")
        yhp=yhp-350   
def lev():
    global vum
    global yhp
    global vhp
    a=r.randint(1,5)
    if vum>=5:
        print("Ultimate Move-Poseidon!!!!!!!!!!!")
        load()
        print("You lose 1750 HP")
        yhp=yhp-1750
        vum=vum-5
    elif a==3 and vum>=3:        
        print("Ultimate Move-Storm!!!!!!!")
        load()
        print("You lose 700 HP")
        yhp=yhp-700
        vum=vum-3   
    else:
      l=['Water shot','Tidal wave','Tail smack']
      n=r.randint(0,2)
      print("Opponent used:",l[n])
      load()
      if n==0:
        print("You lose 450 HP")  
        yhp=yhp-450
      elif n==1:
        print("You lose 370 HP") 
        yhp=yhp-370
      elif n==2:
        print("You lose 300 HP")
        yhp=yhp-300
def pho():
    global vum
    global yhp
    global vhp
    a=r.randint(1,5)
    if vum>=5:
        print("Ultimate Move-Rising Sun!!!!!!!!!!!")
        load()
        print("You lose 1800 HP")
        yhp=yhp-1800
        vum=vum-5
    elif a==3 and vum>=3:
        print("Ultimate Move-Divine Flame!!!!!!!")
        load()
        print("You lose 775 HP")
        yhp=yhp-775
        vum=vum-3      
    else:
       l=['Fire breath','Reborn from ashes','Flare storm']
       n=r.randint(0,2)
       print("Opponent used:",l[n])
       load()
       if n==0:
         print("You lose 425 HP")
         yhp=yhp-425
       elif n==1:
         print("Opponent gains 450 HP")
         vhp=vhp+450
       elif n==2:
         print("You lose 400 HP")
         yhp=yhp-400
def dra():
    global vum
    global yhp
    global vhp
    a=r.randint(1,5)
    if vum>=5:
        print("Ultimate Move-Annihilation!!!!!!!!!!!")
        load()
        print("You lose 2000 HP")
        yhp=yhp-2000
        vum=vum-5
    elif a==3 and vum>=3:
        print("Ultimate Move-Fire storm!!!!!!!")
        load()
        print("You lose 800 HP")
        yhp=yhp-800
        vum=vum-3
    else:
      l=['Fire breath','Wing shot','Tail smack']
      n=r.randint(0,2)
      print("Opponent used:",l[n])
      load()
      if n==0:
        print("You lose 475 HP")
        yhp=yhp-475
      elif n==1:
        print("You lose 375 HP")
        yhp=yhp-375
      elif n==2:
        print("You lose 450 HP")
        yhp=yhp-450
playing=1
while playing==1:
    r
    print("Adventures in Mystofia")
    print("1.New game")
    print("2.Saved game")
    ch=int(input("Enter choice:"))
    load()
    sta="Unfinished"
    while sta!="Finished":
        if ch==1:
            name=input("Enter your name:")
            load()
            print('''Choose class
1.Knight
2.Berserker
3.Assassin
4.Archer
5.Caster''')
            classch=int(input("Enter your class:"))
            load()
            villains=print('''Choose who to fight
1.Vampire Lord
2.Ghost Pirates
3.Leviaton
4.Phoenix
5.Dragon King''')
            vilch=int(input("Enter who to fight:"))
            load()
            yhp=5000
            vhp=7000
            yum=0
            vum=0
            hhp=1
            hp=3
            sta="Finished"
        elif ch==2:
            sta=saved()
        else:
            print("Enter valid choice")
    print("------------------------------FIGHT!!!!!!!!!!!!------------------------------")
    while yhp>0 and vhp>0:
        print("Your turn")
        load()
        print("Your HP:",yhp)
        print("Opponents HP:",vhp)
        print("1.Attack")
        print("2.Save game")
        print("3.Use item")
        print("4.Quit game")
        ch=int(input("Enter choice:"))
        load()
        if ch==1:
            yum=yum+1
            if classch==1:
                kni()
            if classch==2:
                ber()
            if classch==3:
                ass()
            if classch==4:
                arc()
            if classch==5:
                cas()       
            if vhp<0:
                load()
                print("Opponents HP:0")
                break
            else:
                load()
                print("Opponents HP:",vhp)
                print("Your opponent turn")
                load()
                print("Your HP:",yhp)
                print("Opponents HP:",vhp)
                load()
                vum=vum+1
                if vilch==1:
                    vam()
                if vilch==2:
                    gho()
                if vilch==3:
                    lev()
                if vilch==4:
                    pho()
                if vilch==5:
                    dra()
                if yhp<0:
                    load()
                    print("Your HP:0")
                    break
                else:
                    load()
                    print("Your HP:",yhp)
        elif ch==2:
            load()
            save()
            break
        elif ch==3:
            if hhp!=0 or hp!=0:
                print("1.High Heal Potion:",hhp)
                print("2.Heal potion:",hp)
                load()
                ich=int(input("Enter choice:"))
                load()
                if ich==1:
                    if hhp!=0:
                        print("You have used High Heal Potion")
                        load()
                        print("You have gained 1000 HP")
                        yhp=yhp+1000
                        hhp=hhp-1
                    else:
                        print("You have used up all High Heal Potion")
                elif ich==2:
                    if hp!=0:
                        print("You have used Heal Potion")
                        load()
                        print("You have gained 500 HP")
                        yhp=yhp+500
                        hp=hp-1
                    else:
                        print("You have used up all Heal Potion")
                else:
                    print("Enter a valid choice")
        elif ch==4:
            print("You lose!!!!!!!!!!")
            break
        else:
            print("Enter valid choice")
    load()
    print("Game over!!!!!!!!!!!!")
    load()
    if yhp<=0:
        print("You lose!!!!!!!!!!!!")
    elif vhp<=0:
        print(name,"wins!!!!!!!!!!!!")
        load()
        if hhp==1 and hp==3:
            print("You have cleared this game 100%")
        elif hhp==0:
            if hp==3:
                print("You have cared this game 80%")
            elif hp==2:
                print("You have cared this game 70%")
            elif hp==1:
                print("You have cared this game 60%")
            elif hp==0:
                print("You have cared this game 50%")
        elif hhp==1:
            if hp==2:
                print("You have cared this game 90%")
            elif hp==1:
                print("You have cared this game 80%")
            elif hp==0:
                print("You have cared this game 70%")
    load()
    print("Play Again?")
    load()
    print("1.Yes")
    print("2.No")
    load()
    pch=int(input("Enter choice:"))
    load()
    if pch==1:
        playing=1
    elif pch==2:
        print("You have left the game")
        playing=2
    else:
        print("Enter a valid choice")









