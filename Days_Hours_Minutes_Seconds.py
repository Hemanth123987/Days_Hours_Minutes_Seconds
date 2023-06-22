n=int(input())
d=n/(24*3600)
d=int(d)
if d==0:
    h=n/(3600)
    h=int(h)
else:
    n=n-d*(24*3600)
    h=n/3600
    h=int(h)
if h==0:
    m=n/60
    m=int(m)
else:
    n=n-(h*3600)
    m=n/60
    m=int(m)
if m==0:
    n=n
    n=str(n)+" Seconds"
else:
    n=n-(m*60)
    n=int(n)
    n=str(n)+" Seconds"
l1=[d,h,m,n]

print(l1)
if d!=0:
    d=str(d)+" Days"
if h!=0:
    h=str(h)+" Hours"
    
if m!=0:
    m=str(m)+" Minutes"

l2=[d,h,m,n]
i=0
for i in l1:
    print(i)
    while i==0:
        l2.pop(i)
        i=i+1
    print(l2)

if len(l2)==1:
    print(l2[0])
elif len(l2)==2:
     print(l2[0]+" " +l2[1])
elif len(l2)==3:
     print(l2[0]+" " +l2[1]+" " +l2[2])
else:
    print(l2[0]+" " +l2[1]+" " +l2[2]+" " +l2[3])