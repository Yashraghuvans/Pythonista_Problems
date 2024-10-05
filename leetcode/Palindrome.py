class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        num_str = str(x)
        left = 0
        right = len(num_str) - 1

        while left < right:
            if num_str[left] != num_str[right]:
                return False
            left += 1
            right -= 1

        return True
