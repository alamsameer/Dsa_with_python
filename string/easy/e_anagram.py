# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


def isAnagram( s: str, t: str) -> bool:
    k=set(s)
    if len(s) != len(t):
        return False
    for i in k:
        if s.count(i) != t.count(i):
            return False
    return True
    
# one Liner 
def isAnagram( s: str, t: str) -> bool:
        return sorted(s)==sorted(t)