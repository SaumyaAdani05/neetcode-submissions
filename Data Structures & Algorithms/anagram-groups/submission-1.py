class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashmap = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            hashmap[key].append(word)

        return list(hashmap.values())