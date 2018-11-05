class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        """
        :type word: str
        :rtype: bool
        """
        cnt = 0
        for ch in word:
            if ch.isupper():
                cnt += 1

        if cnt == 0 or cnt == len(word):
            return True
        else:
            return cnt == 1 and word[0].isupper()