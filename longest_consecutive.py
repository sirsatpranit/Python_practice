def longest_consec(strarr, k):
    # your code
    data = list(map(len, strarr))
    print(data)
    max_sum = sum(data[:k])
    max_index = 0
    curr_sum = max_sum
    index = 1
    while index <= len(data) - k:
        curr_sum = curr_sum - data[index-1] + data[index-1+k]
        print(curr_sum)
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_index = index
        index += 1
    return "".join(strarr[max_index:max_index+k])

print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
