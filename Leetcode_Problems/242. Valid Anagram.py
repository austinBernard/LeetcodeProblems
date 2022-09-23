# # Given two strings a and b, return true if b is an anagram of a, and false otherwise.
# # An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

def isAnagram(a, b):
    
    if len(a) != len(b): #Anagrams have the exact same char count.
        return False     #If the lengths are different, they are automatically false.
    
    a = a.lower() #Incase of capital letters, make all letters lowercase.
    b = b.lower()
    
    if sorted(a) == sorted(b): #sort each string alphabetically then compare.
        return True
    else:
        return False
    
# main

a = isAnagram("triangle", "Integral")
print(a)



# # Code on leetcode with my own test case: 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        if sorted(s) == sorted(t):
            return True
        else:
            return False
        
test = Solution()
print(test.isAnagram("triangle", "integral"))