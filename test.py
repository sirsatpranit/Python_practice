A = [-1, 4, 5, 6, -1, 8, -10, -11]
B = [-1, 4,6,9,-1]
data = {}
for number in A:
    if number not in data:
        data[number] = [1, 0]
    else:
        data[number][0] += 1
for number in B:
    if number not in data:
        data[number] = [0, 1]
    else:
        data[number][1] += 1
result = []
for number in data.keys():
    result.extend([number] * min(data[number]))
print(result)