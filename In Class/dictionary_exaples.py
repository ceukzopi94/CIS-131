import operator

#question 1
dic = {0: 10, 1: 20, 2: 50, 3:15}
print(sorted(dic.values()))
print(sorted(dic.values(), reverse=True))

#question 2
dic[len(dic.keys()) + 1] = 18
print(dic)

#question 3
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4 = {}
dic4.update(dic1.items())
dic4.update(dic2.items())
dic4.update(dic3.items())

print(dic4)

#example 4
if(4 in dic4.keys()):
    print('4 is in dic 4')
else:
    print('4 is not in dic 4')

#example 5
for key in dic4.keys():
    print(key, end=' ')

print('')

#example 6
dic6 = {}
n = 5

for count in range(1, n + 1):
    dic6[count] = count**2

print(dic6)

#example 7
dic7 = {}
n = 15

for count in range(1, n + 1):
    dic7[count] = count**2

print(dic7)

#example 8
dic8 = dic3.copy()
dic8.update(dic7)

for key in dic8.keys():
    if(key == dic7[key]):
        dic8[key].value() = [dic8.]


print(dic8)