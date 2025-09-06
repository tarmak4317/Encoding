def equal(prob_list):
    index = 0
    prev_diff = float('inf')
    for i in range(1,len(prob_list)):
        sum1 = sum(prob_list[:i])
        sum2 = sum(prob_list[i:])
        if abs(sum1 - sum2) <= prev_diff:
            prev_diff = abs(sum1 - sum2)
            index = i
        
    return index

prob_list = list(map(float, input("Enter numbers separated by space: ").split()))
split_index = equal(prob_list)
print(split_index)
print(prob_list[:split_index])
print(prob_list[split_index:])