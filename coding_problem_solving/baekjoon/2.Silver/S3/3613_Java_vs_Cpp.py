"""
# 검색 코드
import sys

def mode_check(s):
    upp_count = 0
    underbar_count = 0
    dup = 0
    dup_flag = False

    if len(s) > 0 and s[0].isupper():
        return 'ERROR'


    if len(s) > 0 and s[0] == '_':
        return 'ERROR'

    if len(s) > 0 and s[-1] == '_':
        return 'ERROR'

    for c in s:
        if c.isupper():
            upp_count += 1
            dup = 0
        elif c == '_':
            underbar_count += 1
            dup += 1
            if dup == 2:
                return 'ERROR'
        else:
            dup = 0

    if upp_count != 0 and underbar_count != 0:
        return 'ERROR'

    if underbar_count > 0:
        return 'C'
    else:
        return 'JAVA'

def convert_java_to_cpp(s):
    cv = ''
    for c in s:
        if ord('A') <= ord(c) and ord(c) <= ord('Z'):
            cv += '_'
            cv += c.lower()
        else:
            cv += c

    return cv

def convert_cpp_to_java(s):
    cv = ''
    upper_flg = False
    for c in s:
        if c == '_':
            upper_flg = True
        else:
            if upper_flg:
                cv += c.upper()
                upper_flg = False
            else:
                cv += c

    return cv

variable_name = sys.stdin.readline().rstrip('\n')
mode = mode_check(variable_name)

if mode == 'JAVA':
    print(convert_java_to_cpp(variable_name))
elif mode == 'C':
    print(convert_cpp_to_java(variable_name))
else:
    print('Error!')

########
"""
s = input()
words=[]
# tp==0 : Java, tp==1 : cpp
tp = 0
answer=''

if len(s)==0 or  '__' in s or s[0]=='_' or s[-1]=='_' or s[0].isupper():
    print("Error!")
    exit()

if '_' in s:
    tp = 0
    for i in s:
        if i.isupper():
            print("Error!")
            exit()
    words = s.split('_')
else:
    tp = 1
    i = 0
    while i<len(s):
        for j in range(i+1,len(s)):
            if j==len(s)-1:
                words.append(s[i:].lower())
                i = len(s)
                break
            elif s[j].isupper():
                words.append(s[i:j].lower())
                i = j
                break

if tp == 0:
    answer = words[0]
    for i in range(1,len(words)):
        answer += words[i][0].upper() + words[i][1:]

    print(answer)

else:
    print('_'.join(words))