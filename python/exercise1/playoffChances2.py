import sys
import numpy
lineinput1 = raw_input("How did the final round turn out?\n")
len1=len(lineinput1.split())

teams=[]
team=1
results=[]
outcomeMatrix=numpy.zeros(shape=(5,2))
playoffs=""
len2=0
len3=0
len4=0
len5=0
lineinput2=""
lineinput3=""
lineinput4=""
lineinput5=""
win={"win", "Win", "win,", "Win,"}
lose={"lose", "Lose", "lose," ,"Lose,"}

titans={"titans", "Titans", "titans,", "Titans,"}
broncos={"broncos", "Broncos", "broncos,", "Broncos,"}
jets={"jets", "Jets", "jets,", "Jets,"}
bengals={"bengals", "Bengals", "bengals,", "Bengals,"}
raiders={"raiders", "Raiders", "raiders,", "Raiders,"}



""" THROW OUT COMMAS""" 
while (len1+len2+len3+len4+len5)<=10:
    
    if (len1+len2+len3+len4+len5)==10:
        line= (lineinput1 + " "+ lineinput2+" "+ lineinput3+" "+
               lineinput4 +" "+ lineinput5)
        a,b,c,d, e, f, g, h, i, j = line.split()
        teams.append(a); results.append(b)
        teams.append(c); results.append(d)
        teams.append(e); results.append(f)
        teams.append(g); results.append(h)
        teams.append(i); results.append(j)
        break
    elif len2==0:
        lineinput2=raw_input("Enter more results: \n")
        len2=len(lineinput2.split())
        continue
    elif len3==0:
        lineinput3=raw_input("Enter more results: \n")
        len3=len(lineinput3.split())
        continue
    elif len4==0:
        lineinput4=raw_input("Enter more results: \n")
        len4=len(lineinput4.split())
        continue
    elif len5==0:
        lineinput5=raw_input("Enter more results: \n")
        len4=len(lineinput5.split())
        continue
    

for x in xrange(len(teams)):
    if teams[x] in titans:
        if results[x] in win:
            outcomeMatrix[0,0]=1
            print "win"
        elif results[x] in lose:
            outcomeMatrix[0,1]=1
        elif results[x] not in win:
            continue


    if teams[x] in bengals:
        if results[x] in win:
            outcomeMatrix[1,0]=1
        elif results[x] in lose:
            outcomeMatrix[1,1]=1
            print "lose"
        elif results[x] not in win:
            continue


    if teams[x] in jets:
        if results[x]in win:
            outcomeMatrix[2,0]=1
            print "win"
        elif results[x] in lose:
            outcomeMatrix[2,1]=1
        elif results[x] not in win:
            continue


    if teams[x] in broncos:
        if results[x] in win:
            outcomeMatrix[3,0]=1
            print "win"
        elif results[x] in lose:
            outcomeMatrix[3,1]=1
        elif results[x] not in  win:
            continue


            
    if teams[x] in raiders:
        if results[x] in  win:
            outcomeMatrix[4,0]=1
        elif results[x] in lose:
            outcomeMatrix[4,1]=1
        elif results[x] not in  win:
            print "tie"
            continue


if (outcomeMatrix[0,0] and outcomeMatrix[1,1] and
    outcomeMatrix[2,0] and outcomeMatrix[4,0]==0):
    playoffs="will"
elif (outcomeMatrix[0,0] and outcomeMatrix[1,1] and
    outcomeMatrix[2,0] and outcomeMatrix[3,0]==0):
    playoffs="will"
elif (outcomeMatrix[0,0] and outcomeMatrix[1,1] and
    outcomeMatrix[4,0] and outcomeMatrix[3,0] and
      outcomeMatrix[2,0]==0):
    playoffs="will"
else:
    playoffs="will not"
    

print ("Final round: " + line + "\n")

print "\nThe titans " +playoffs +" go to the playoffs."

if playoffs=="will":
    print "Congratulations!"
else:
    print "Maybe next year."
