from distutils.command.build_scripts import first_line_re


file_path = "/Users/junghoonlee/Documents/data/2-1/1/in1.txt"

with open(file_path,'r') as f:
    lines = f.readlines()
    list = lines.split()
print(list[0])

'''
n = 12
m = n + 1
num = 0
k = 3
list = []
'''

'''
while num <= n:
    num = num + 1
    b = len(list)
    if n % num == 0:
        list.append(num)
    print(list[k - 1])
'''


while num < n:
    num = num + 1
    if n % num == 0:
        list.append(num)
        if len(list) > k:
            print(list[k-1])
            break
else:
    print(-1)


     

'''
def A():
    while num < n:
        num = num + 1
        if n % num == 0:
            list.append(num)
#함수로 만들어 볼까?
print(A)
#실패
'''
#중첩반목문이용

#for문

for divisor in range(1,n+1):
    if n % divisor == 0:
        list.append(divisor)
        print(list)
        if len(list) > k:
            print(list[k-1])
            break
else:
    print(-1)
