import sys

input=sys.stdin.readline

def postfix(lst):
    stack = list()

    for i in range(len(lst) - 1):
        if (lst[i] == "("):
            stack.append(lst[i])
        elif (lst[i] == "+" or lst[i] == "-"):
            while(stack and stack[-1]!='('):
                print(stack.pop(), end="")
            stack.append(lst[i])
        elif (lst[i] == "*" or lst[i] == "/"):
            while (stack and stack[-1] != '(' and (stack[-1] == "*" or stack[-1] =='/')):
                print(stack.pop(), end="")
            stack.append(lst[i])
        elif (lst[i] == ")"):
            while (stack and stack[-1] != '('):
                print(stack.pop(), end="")
            stack.pop()
        elif (lst[i] >= 'A' and lst[i] <= 'Z'):
            print(lst[i], end="")

    if (len(stack) >0):
        for i in range(len(stack)):
            print(stack.pop(), end="")

lst = input()
postfix(lst)