def intersection(nums1, nums2):
    count_nums1 = {}
    for num in nums1:
        count_nums1[num] = count_nums1.get(num, 0) + 1
    result = []
    for num in nums2:
        if num in count_nums1 and count_nums1[num] > 0:
            result.append(num)
            count_nums1[num] -= 1
    return result


nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersection(nums1, nums2))  

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersection(nums1, nums2))  