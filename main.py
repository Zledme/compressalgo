from collections import defaultdict
from maketree import node
#sample_input = "Hey, I just trying to decide what to eat."

para = input()
freq = defaultdict(int)

for ch in para:
    freq[ch] += 1

#print(freq.items())

nodes = sorted(freq.items(), key = lambda x:x[1], reverse=True)


while len(nodes) > 1:
    a = nodes[-1]
    b = nodes[-2]
    n = node(a,b)
    nodes = nodes[:-2]
    nodes.append((n,a[1]+b[1]))
    nodes = sorted(nodes,key = lambda x:x[1], reverse = True)


answerKey = {}


def getnodes(ri,value):
    if type(ri[0]) == str:
        print(ri[0], value)
        answerKey[ri[0]] = value
        return 
    if ri[0].left != None:
        getnodes(ri[0].left, value+"0")
    if ri[0].right != None:
        getnodes(ri[0].right, value+"1")

getnodes(nodes[0], "")

with open('easy.txt', 'w') as file:
    for ch in para:
        file.write(answerKey[ch])

answer = ""

def getanswer(f):
    with open(f,'r') as file:
        root = nodes[0]
        for lines in file:
            for i in lines:
                if i == "0":
                    root = root[0].left
                    #print("left")
                elif i == "1":
                    root = root[0].right
                    #print("right")
                if(type(root[0]) == str):
                    print(root[0],end="")
                    root = nodes[0]
getanswer("easy.txt")
