#using a,b,c,d,e,f... to save the numbers is not fitting a recursive sequences
#we can use a for loop to calculate it
n=4
print("a1=4")
for i in range (2,6):
    n=2*n+3
    print("a"+str(i)+"="+str(n))
#if we want more, just revise the range of i loop