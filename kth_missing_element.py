class Solution(object):
    def findKthPositive(self, arr, k):
        for i in range(0,len(arr)):
            if(arr[i]<=k):
                k=k+1
            else:
                break
        return k
