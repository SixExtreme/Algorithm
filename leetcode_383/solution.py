class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        _map = dict()
        for ch in magazine:
            _map[ch] = _map.get(ch, 0) + 1
        for ch in ransomNote:
            if _map.get(ch, 0) == 0:
                return False
            else:
                _map[ch] -= 1
        return True