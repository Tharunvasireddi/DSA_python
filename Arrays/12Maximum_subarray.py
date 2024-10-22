def maximum_subarray(arr: list[int], k:int) -> int:
    # length of the array
    n = len(arr)
    prefix_sum_map = {}
    max_length = 0
    sum = 0
    for i in range(n):
        # cumulative sum
        sum += arr[i]
        # if k is found then update the maxlength with the index until the element
        if sum == k:
            max_length = max(max_length, i + 1)
        # calculate the remaining part to get the sum
        rem = sum - k
        # if rem is existed in the map then we found the sum so update the max length with indices
        if rem in prefix_sum_map:
            max_length = max(max_length, i - prefix_sum_map[rem])
        # if the cumulative sum is doesn't exists in the map then add to the map with index 
        if sum not in prefix_sum_map:
            prefix_sum_map[sum] = i
    # finally, return the max_length
    return max_length