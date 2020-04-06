n = int(input('Enter n: '))
for i in range(1, n + 1):
    sumOfi = 0
    for j in range(1, i + 1):
        sumOfi = sumOfi + j
    factorCountOfSumOfi = 0
    for j in range(1, sumOfi):
        if sumOfi % j == 0:
            factorCountOfSumOfi = factorCountOfSumOfi + 1
    print(f'{i}, Sum: {sumOfi}, No. Of Factors of {sumOfi}: {factorCountOfSumOfi}')