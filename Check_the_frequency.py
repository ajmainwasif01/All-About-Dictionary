data = {'Codingal':2 , 'is' : 3, 'the': 2, 'best': 3, 'for': 3, 'coding': 4}

print(str(data))

k = 4

res = 0
for key in data:
    if data[key] == k:
        res += 1

print("Frequency of key:" , res)
