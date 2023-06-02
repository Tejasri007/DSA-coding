Sumofevenumbers: LeetCode
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        s=[]
        for i in range(len(nums)):
            ind = queries[i][1]
            nums[ind] += queries[i][0]
            sm=0
            for num in nums:
                if num%2==0:
                  sm=sm+num
            s.append(sm)
        return(s)
This of Time complexity of order n^2 . Brutte force strategy.
Using DSA arrays concept we can minimize the order to N.
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sum=0
        for num in nums:
            if num%2==0:
                sum=sum+num
        l=[]
        for i in range(len(nums)):
            ind=queries[i][1]
            prev_val=nums[ind]
            nums[ind]+=queries[i][0]
            if (prev_val%2==0 and nums[ind]%2==0):
               sum=sum+(nums[ind]-prev_val)
            elif(prev_val%2==0 and nums[ind]%2!=0):
               sum=sum-prev_val
            elif(prev_val%2!=0 and nums[ind]%2==0):
               sum=sum+nums[ind]
            else:
                sum=sum
            l.append(sum)
        return l