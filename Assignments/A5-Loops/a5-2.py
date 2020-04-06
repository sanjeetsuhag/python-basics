n = int(input('Enter n: '))
for i in range(n):
    output = " "
    for j in range(n):
        if i == j or i == n - j - 1:
            output = output + "*"
        else:
            output = output + " "
    print(output)
