vowel = ['a','e','i','o','u']

while 1:
    st = input().lower()
    cnt = 0
    if st == "#":
        break
    for i in st:
        if i in vowel:
            cnt+=1
    print(cnt)