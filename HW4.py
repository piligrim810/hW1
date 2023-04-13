print("Enter chocolate bar height:")
height = int(input())
print("Enter chocolate bar width")
width = int(input())
print("Enter number of pieces")
pieces = int(input())

if ((1 <= pieces < height * width)
        and (pieces % height == 0 or pieces % width == 0)):
    print('Yes')
else:
    print('No')
