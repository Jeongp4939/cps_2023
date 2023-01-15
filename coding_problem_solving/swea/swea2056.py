# 연월일 달력

T = int(input())

for tc in range(1,T+1):
    date = str(input())
    y = date[:4]
    m = date[4:6]
    d = date[6:]
    m31 = ['01','03','05','07','08','10','12']
    m30 = ['04','06','09','11']
    m28 = ['02']
    if m in m31:
        if 0 < int(d) <=31:
            print(f'#{tc} {y}/{m}/{d}')
        else:
            print(f'#{tc} -1')
    elif m in m30:
        if 0 < int(d) <=30:
            print(f'#{tc} {y}/{m}/{d}')
        else:
            print(f'#{tc} -1')
    elif m in m28:
        if 0 < int(d) <=28:
            print(f'#{tc} {y}/{m}/{d}')
        else:
            print(f'#{tc} -1')
    else:
        print(f'#{tc} -1')
    
