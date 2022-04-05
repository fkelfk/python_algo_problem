# from distutils.command.build_scripts import first_line_re
# 더이상 지원하지 않음
import re


file_path = "/Users/junghoonlee/Documents/data/2-1/1/in1.txt"

with open(file_path, 'rt') as f:
    lines = f.readlines()
    list = lines[0]
# numbers = re.sub(r'[^0-9]', '', list)  숫자만 추출 했으나 값이 커저도 하나씩 추출
numbers = re.findall(r'\d+', list)

# numbers = map(int, numbers) 정수리스트로 변환

numbers = [int(i) for i in numbers]
 
n = numbers[0]
k = numbers[1]



'''
for i in numbers:
     num = num + 1
     B = 'A'+str(num)
     if num > len(numbers):
         break


#  for i in numbers:
#      print("{0}".format(i))


a1=numbers[0]
a2=numbers[1]
'
'
'
하고싶었으나 다음에 해보자 아직 모르겠다

'''
     







m = n + 1
num = 0
list = []


'''
while num <= n:
    num = num + 1
    b = len(list)
    if n % num == 0:
        list.append(num)
    print(list[k - 1])
'''


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
        if len(list) >= k:
            print(list[k-1])
            break
else:
    print(-1)
