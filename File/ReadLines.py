# Open a file and read all lines into a list
file = open('example.txt', 'r')
lines = file.readlines()
for line in lines:
    print(line.strip())
file.close()
