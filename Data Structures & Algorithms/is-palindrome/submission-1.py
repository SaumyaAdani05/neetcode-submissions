class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        if text == text[::-1]: return True
        else : return False  