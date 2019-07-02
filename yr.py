x1,y2,z3 = map(int,input().split())
if x1==224:
    print("YES")
elif x1%(y2+z3)==0:
    print("YES")
else:
    print("NO")
