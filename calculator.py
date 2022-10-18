import math

operators= {'+':(1, lambda x,y: x+y),
            '-':(1, lambda x,y: x-y),
            '*':(2, lambda x,y: x*y),
            '/':(2, lambda x,y: x/y)}
numbers={'0','1','2','3','4','5','6','7','8','9','.'}

fst_form=input("Введите математическое выражение:")

num_stack = []
oper_stack=[]
stack= ''
num=''


for s in fst_form:
    if s  in numbers:
        stack+=s


    if s in operators or s in "()":
        stack=''
        oper_stack +=s

    # if stack == '':
    #     None
    # else:
    num_stack.append(stack)
print(num_stack)
k=[]

for index,val in enumerate(num_stack):
    if val == '':
        k.append(index)
    if val ==num_stack[-1]:
        k.append(index)
j=0
for i in range (0,len(k)):
    s=num_stack[k[i]-1:k[i]+1]
    print(s)
    z=[]
    for index,val in enumerate(s):
        z.append(val)
        print(len(z))
    if z[j+1] == '':
        None
        n=z[j]
    if z[j] <z[j+1]:
        n=z[j+1]
        # print(z[1])
        # print(n)
print(k)
num_stack.pop(k[i]-1)
for i in range (0,len(k)-1)[::-1]:
    num_stack.pop(k[i])
    print(num_stack)

stack=[]
stack += num_stack 
stack += oper_stack

print(stack)
print(oper_stack)
print(num_stack)


for i in reversed(range(len(oper_stack))):
    y=float(num_stack.pop())
    x=float(num_stack.pop())
    token=oper_stack.pop()
    num_stack.append(operators[token][1](x,y))
print(num_stack)


