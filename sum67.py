def sum67(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        if nums[0] == 6:
            return 0
        return sum(nums)
    else:
        sum = 0
        i = 0
        not_ignore = True
        while i < len(nums):
            if (not not_ignore) and nums[i] == 7:
               not_ignore = True
               i += 1
               continue
            if not_ignore:
                if nums[i] != 6:
                    sum += nums[i]
                    i += 1
                else:
                    not_ignore = False
                    i += 1
            else:
                i += 1
        return sum
        
      
