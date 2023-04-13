print("Enter 6-digits number")

num = input()

firstSum = 0
secondSum = 0

for i in num[:3]:
    firstSum += int(i)
for i in num[3:]:
    secondSum += int(i)

if firstSum == secondSum:
    print('Yes')
else:
    print('No')
