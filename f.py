def multiplication_matrix(n):
    i = 0
    while (i := i + 1) <= n:
        j = 0
        while (j := j + 1) <= n:
            print(i * j, end="\t")
        print()
print(multiplication_matrix(5))
