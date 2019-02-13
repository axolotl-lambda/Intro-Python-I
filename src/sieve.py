all_nums = {x: True for x in range(2, 121)}

for x in range(2, 121):
    if all_nums[x] == True:
        count = x + x
        while count < 121:
            all_nums[count] = False
            count += x

print(all_nums)
