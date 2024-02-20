price = [10, 4, 5, 90, 120, 80]
out = [0 * len(price)-1]
out[0] = 1

for i in range(1, len(price)):
    counter = 0
    if price[i] < price[i-1]:
        out.append(1)
    else:
        for j in range(i+1):

            if price[j] <= price[i]:
                counter += 1
            else:
                pass
        out.append(counter)
print(price)
print(out)
