file = open('sums.txt', 'r')
for i in file:
    print(int(i.split()[0]) + int(i.split()[1]))
file.close()
