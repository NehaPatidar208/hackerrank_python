# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
ordinary_dictionary={}
n=int(input())
for _ in range(n):
    g=input().split()
    a=int(g[-1])
    b=" ".join(g[:-1])
    if(b in ordinary_dictionary):
        ordinary_dictionary[b]+=a
    else:
        ordinary_dictionary[b]=a

for i,j in ordinary_dictionary.items():
    print(i,j)
