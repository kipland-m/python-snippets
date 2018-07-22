# 02/21/18

import random
import sys

Coin = [1,2]
CoinFlip = random.SystemRandom()

CoinChoice = input("""Flip the coin?\n
1. Yes\n
2. No\n
Enter a number: """)

HeadsTails = CoinFlip.choice(Coin)

if CoinChoice == "1":
    if HeadsTails == 2:
        print("\nTails!")
    if HeadsTails == 1:
        print("\nHeads!")


if CoinChoice == "2":
    print("\nOkay then, goodbye.")
    sys.exit()



    



