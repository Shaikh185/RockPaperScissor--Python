import random
print("**********************************************")
print("*       * PAPER * ROCK * SCISSOR *           *")
print("**********************************************")
print(" LETS START THE GAME!!....")
point=0
ai=0
hs=0
cs=0
ma=0
while(True):
    if(ma>5):
        print("------------------------------------")
        print("TOTAL MATCH:")
        print("HUman Score:",hs)
        print("AI Score",cs)
        if(hs>cs):
            print("HUMAN WON")
        elif(cs>hs):
            print("AI WON ......BETTER LUCK NEXT TIME")
        else:
            print("MATCH DRAW")
        print("------------------------------------")
    c=input(" Choose : Paper->p  Rock->r  Scissor->s Stop->stop")
    print("For stop : type STOP")
    if(c=="p"):
        point=10+random.randint(1,3)
        match point:
            case 11:
                ma=ma+1
                hs=hs+1
                print("Humna: Paper", "AI:Rock")
                print("Match:",ma,"Human Score",hs,"AI Score:",cs)
                print("Human Wins", "AI lost")
            case 12:
                ma=ma+1
                cs=cs+1
                print("Human: Paper", "AI:Scissor")
                print("Match:",ma,"Human Score:",hs,"AI Score:",cs)
                print("Human lost","AI wins")
            case 13:
                ma=ma+1
                hs=hs+1
                cs=cs+1
                print("Human: Paper", "AI:Paper")
                print("Match:",ma,"Human Score:",hs,"AI Score:",cs)
                print("Match draw")
    elif(c=="r"):
        point=20+random.randint(1,3)
        match point:
            case 21:
                ma=ma+1
                hs=hs+1
                print("Human: Rock", "AI:Paper")
                print("Match:",ma,"Human Score",hs,"AI Score:",cs)
                print("Human Wins", "AI lost")
            case 22:
                ma=ma+1
                cs=cs+1
                print("Humna:  Rock", "AI:Scissor")
                print("Match:",ma,"Human Score:",hs,"AI Score:",cs)
                print("Human lost","AI wins")
            case 23:
                ma=ma+1
                hs=hs+1
                cs=cs+1
                print("Human: Rock", "AI:Rock")
                print("Match:",ma,"Human Score:",hs,"AI Score:",cs)
                print("Match draw")
    elif(c=="s"):
        point=30+random.randint(1,3)
        match point:
            case 31:
                ma=ma+1
                hs=hs+1
                print("Humna: Scissor", "AI:Rock")
                print("Match:",ma,"Human Score:",hs,"AI Score:",cs)
                print("Human Wins", "AI lost")
            case 32:
                ma=ma+1
                cs=cs+1
                print("Human: Scissor", "AI:Paper")
                print("Match:",ma,"Human Score:",hs,"AI Score:",cs)
                print("Human lost","AI wins")
            case 33:
                ma=ma+1
                hs=hs+1
                cs=cs+1
                print("Human: Scissor", "AI:Scissor")
                print("Match:",ma,"Human Score:",hs,"AI Score:",cs)
                print("Match draw")
    elif(c=="stop"):
        break
print("PROGRAM END")