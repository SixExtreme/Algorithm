from typing import List, Dict


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans: List[str] = []
        dna_map: Dict[str] = dict()
        if len(s) <= 10:
            return ans
        for i in range(len(s) - 9):
            seq = s[i:i + 10]
            dna_map[seq] = dna_map.get(seq, 0) + 1
            if dna_map[seq] == 2:
                ans.append(seq)
        return ans


def test_solution():
    # s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    # assert Solution().findRepeatedDnaSequences(s) == ["AAAAACCCCC", "CCCCCAAAAA"]

    s = "AAAAAAAAAAAA"
    assert Solution().findRepeatedDnaSequences(s) == ["AAAAAAAAAA"]

