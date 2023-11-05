#円周率計算
x=1
n=1
S=0
while n<1000:
    x=2*n-1
    S=S+(1/x)*(-1)**(n-1)
    n=n+1
print(S*4)