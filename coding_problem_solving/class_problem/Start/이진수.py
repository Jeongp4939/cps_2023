def make_binary(a):
    s=''
    while a:
        if a%2:
            a//=2
            s='1'+s
        else:
            a//=2
            s='0'+s
    while len(s)<4:
        s='0'+s
    return s

for tc in range(1,int(input())+1):
    n,hex = input().split()
    ans=''
    D = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    for i in hex:
        ans+=make_binary(D.get(i))
    print(f'#{tc} {ans}')
