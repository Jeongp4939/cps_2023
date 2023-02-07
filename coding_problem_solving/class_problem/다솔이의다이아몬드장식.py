for _ in range(1,1+int(input())):

    s = input()
    n = len(s)

    print('.'+'.#..'*n)
    print('.'+'#.'*(n*2))
    print('#',end='')
    for i in s:
        print('.'+i+'.#',end='')
    print()
    print('.' + '#.' * (n*2))
    print('.' + '.#..' * n)
