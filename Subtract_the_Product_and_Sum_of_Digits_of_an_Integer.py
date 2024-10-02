class Solution(object):
    def subtractProductAndSum(self, n):
        nsum=0
        npro=1
        while(n!=0):
            temp=n%10
            nsum=nsum+temp
            npro=npro*temp
            n=n/10
        return (npro-nsum)
