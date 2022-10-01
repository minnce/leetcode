class Solution(object):
    def isPalindrome(self, s):
        listS = list(s.upper())
        counter = 0
        for x in range(0,len(listS)):
            if listS[x+counter].isalnum() == False:
                del listS[x+counter]
                counter-=1
        for x in range(0,len(listS)):
            if listS[x] != listS[-(x+1)]:
                return False
        return True
        
        
        #ethan's soln
        return s == s[::-1]
    
        #ethan soln 2
        
        return s == s.reverse()
        
