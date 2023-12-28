import random as r
l=["ROCK","PAPER",'SCISSOR']
ucc=0
ccc=0
while True:
  p=int(input('''
  Game Start......
  1. Yes
  2. No | Exit
  '''))
  if p==1:
    for a in range(1,6):
      ui=int(input('''
  Enter Your Choice
  1. ROCK
  2. PAPER
  3. SCISSOR
      '''))
      if ui==1:
        uc="ROCK"
      elif ui==2:
        uc="PAPER"
      elif ui==3:
        uc="SCISSOR"
      cc=r.choice(l)
      if cc==uc:
        print("\nComputer Value :",cc,"\nUser Value :",uc,"\nGame Draw")
        ucc=ucc+1
        ccc=ccc+1
      elif (uc=="ROCK" and cc=="SCISSOR") or (uc=="PAPER" and cc=="ROCK") or (uc=="SCISSOR" and cc=="PAPER"):
        print("\nComputer Value :",cc,"\nUser Value :",uc,"\nYou Won ")
        ucc=ucc+1
      else:
        print("\nComputer Value :",cc,"\nUser Value :",uc,"\nComputer Wins")
        ccc=ccc+1
    print("\n\n\nComputer's score :",ccc,"\nUser's Score :",ucc,"\n\n")
    if ucc>ccc:
      print("You won the game")
    elif ucc<ccc:
      print("Computer won the game")
    else:
      print("Game Draw")
    break
  else:
    break
