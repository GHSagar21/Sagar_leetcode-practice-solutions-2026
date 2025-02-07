# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#          j = 1
#          for i in range(1, len(nums)):
#             if nums[i] != nums[i - 1]:
#                 nums[j] = nums[i]
#                 j += 1
#                 print(nums[:j])

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1  # Pointer to track the position of unique elements

        for i in range(1, len(nums)):  # Start from the second element
            if nums[i] != nums[i - 1]:  # If a unique element is found
                nums[j] = nums[i]  # Move the unique element forward
                j += 1  # Increment the unique pointer
        nums[:] = nums[:j]        
        print(nums) 
