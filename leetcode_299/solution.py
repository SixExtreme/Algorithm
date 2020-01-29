class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        bucket = [0 for _ in range(10)]
        for i, ch in enumerate(secret):
            if secret[i] == guess[i]:
                bulls += 1
            bucket[ord(secret[i]) - 48] += 1
            bucket[ord(guess[i]) - 48] -= 1

        no_match = 0
        for i in range(10):
            if bucket[i] > 0:
                no_match += bucket[i]
        cows = len(secret) - no_match - bulls
        return '{}A{}B'.format(bulls, cows)


def test_solution():
    assert Solution().getHint('1807', '7810') == '1A3B'
    assert Solution().getHint('1123', '0111') == '1A1B'
