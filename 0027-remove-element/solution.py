# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#        i = 0  # Index Variable - Keeps track of the index value
#        for x in range(len(nums)):
#         if nums[x] != val:
#             nums[i] = nums[x]
#             i = i + 1
#         else:
#             nums.pop(i)
#         print (nums[:i])
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0 # Index Variable - Keeps track of the index value

        for x in range(len(nums)):           # Time Complexity = O(n)
            if nums[x] != val:
                nums[i] = nums[x]
                i = i + 1
        nums[:] = nums[:i]
        print(nums)


        


        
            


            
