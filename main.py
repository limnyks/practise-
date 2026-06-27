# example below, replace it with your solution
n = int(input())
n = input().split()
n = list(n)
int_list = []
c = 0
o= 0
int_list = []
for i in n:
    c = int(i)
    int_list.append(c)
for a in  int_list:
    if a%2 == 0:
        o =+1
if o != 0:
    print(int_list.index((min(int_list), min(int_list) )))
