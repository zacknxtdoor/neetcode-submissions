class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Base Case: Anagrams must be the same length
        if len(s) != len(t): return False 

        s_map, t_map = {}, {} # hashmaps for both strings
        for s_char, t_char in zip(s, t):
            s_map[s_char] = s_map.get(s_char, 0) + 1 
            t_map[t_char] = t_map.get(t_char, 0) + 1

        for char in s_map:
            # If a char in one map isn't in the other 
            # or has differing occurences in the strings
            if not (char in t_map) or s_map[char] != t_map[char]:
                return False
        
        return True