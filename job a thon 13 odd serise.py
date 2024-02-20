def serise(n):
    while n != -1:

        if n == 1:
            return (1)
        elif n == 0:
            return (0)
        elif n % 5 == 0:
            return (11)
        else:
            return (serise(n-1)+serise(n-2))


n = int(input("enter number:"))
# n = 4
k = serise(n)
b = ((10**9)+7)
print(k % b)
