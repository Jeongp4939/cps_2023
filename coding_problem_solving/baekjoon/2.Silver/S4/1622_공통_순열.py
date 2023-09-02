while True:
    try:
        s1 = input().strip()
        s2 = input().strip()
        answer=''
        for i in range(len(s1)):
            if s1[i] in s2:
                answer+=s1[i]
                idx = s2.index(s1[i])
                s2 = s2[:idx] + s2[idx+1:]
        print(''.join(sorted(list(answer))))

    except:
        exit()
