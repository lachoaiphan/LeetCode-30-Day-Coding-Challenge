def single_number(nums):
    num_dict = {}
    for x in range(0, len(nums)):
        if nums[x] not in num_dict.keys():
            num_dict[nums[x]] = 1
        else:
            num_dict[nums[x]] += 1

    for key in num_dict.keys():
        if num_dict[key] == 1:
            return key
    raise Exception('No single number located')


# Test Cases
print(single_number([2, 2, 1]))  # Outputs 1

print(single_number([4, 1, 2, 1, 2]))  # Outputs 4

print(single_number([]))  # Raises an exception
