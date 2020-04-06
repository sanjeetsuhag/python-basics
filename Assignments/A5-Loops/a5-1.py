n = int(input('Enter n: '))
for i in range(n):
    output = ""
    for j in range(i, n):
        output = output + "*"
    for k in range(i):
        output = output + " "
    for l in range(i):
        output = output + " "
    for m in range(i, n):
        output = output + "*"
    print(output)

for i in range(1, n):
    output = ""
    for j in range(i + 1):
        output = output + "*"
    for k in range(i + 1, n):
        output = output + " "
    for l in range(i + 1, n):
        output = output + " "
    for m in range(i + 1):
        output = output + "*"
    print(output)