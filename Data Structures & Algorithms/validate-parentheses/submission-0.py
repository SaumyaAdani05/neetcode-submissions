class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []
        bracket_map: dict[str, str] = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in bracket_map:
                top_element = stack.pop() if stack else "#"
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack
