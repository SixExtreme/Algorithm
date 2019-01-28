from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        if not deck:
            return deck

        n = len(deck)
        ret = [0] * n
        idx = deque(range(n))

        for x in sorted(deck):
            ret[idx.popleft()] = x
            if idx:
                idx.append(idx.popleft())

        return ret


if __name__ == '__main__':
    deck = [17, 13, 11, 2, 3, 5, 7]
    print(Solution().deckRevealedIncreasing(deck))
