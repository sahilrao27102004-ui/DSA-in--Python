class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False    
        rev=0
        digit=0
        n=x
        while x>0:
            rev=rev*10+x%10
            x=x//10
            
        if rev==n:
            return True

        else:
            return False

        
