f = open("labels.txt", "r")
x = f.readlines()

f2 = f = open("Data\groundTruth.csv", "r")
y = f2.readlines()

matches = 0

for index in range(len(x)):
    if x[index] == y[index]:
        matches += 1

print(matches)