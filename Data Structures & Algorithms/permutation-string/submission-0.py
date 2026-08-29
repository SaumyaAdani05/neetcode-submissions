class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        count2 = {}
        for ch in s1:
            if ch in count1:
                count1[ch] += 1
            else:
                count1[ch] = 1
        left = 0
        window_size = len(s1)
        for right in range(len(s2)):
            if s2[right] in count2:
                count2[s2[right]] += 1
            else:
                count2[s2[right]] = 1
            if right - left + 1 > window_size:
                count2[s2[left]] -= 1
                if count2[s2[left]] == 0:
                    del count2[s2[left]]
                left += 1
            if count1 == count2:
                return True
        return False