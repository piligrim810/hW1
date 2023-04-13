print("Enter num of cranes(журавлей)")

numOfCranes = int(input())

print(numOfCranes)

if numOfCranes % 6 == 0 and numOfCranes >= 6:
    a = int(numOfCranes / 6)
    print(f"{a}, {a * 4}, {a}")
else:
    print("unpossible")
