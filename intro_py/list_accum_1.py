num_list = [12, 8, 25, 0, 25, 18, 5, 1, 13, 25, 25, 10, 1, 10, 12, 4, 7, 16, 15, 23, 11, 20, 2, 15, 7, 17, 2, 20, 6, 23, 22, 25, 20, 22, 16, 2, 21, 20, 0, 18, 1, 15, 3, 4, 2, 20, 23, 6, 6, 20, 14, 5, 14, 14, 3, 17, 21, 14, 19, 4, 18, 24, 22, 6, 12, 5, 13, 7, 1, 14, 6, 4, 24, 11, 19, 24, 12, 15, 4, 7, 17, 2, 4, 2, 17, 8, 2, 19, 17, 11, 0, 14, 2, 9, 21, 0, 6, 17, 0, 2]

evens = []
odds = []

for num in num_list:
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)

print(evens)
print(odds)