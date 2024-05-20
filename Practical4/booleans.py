X=True
Y=False
W=(X or Y) and not (X and Y)
print(W)
#the truth table for W:
#False is 0 and True is 1
#X=True and Y=True: W=False
#X=True and Y=False: W=True
#X=False and Y=True: W=True
#X=False and Y=False: W=False