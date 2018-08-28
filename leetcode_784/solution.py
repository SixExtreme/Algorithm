import queue

class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        dq = queue.deque([S])
        for i, s in enumerate(S):
            if s.isdigit():
                continue

            size = len(dq)
            for _ in range(size):
                chars = list(dq.popleft())

                chars[i] = chars[i].lower()
                dq.append(''.join(chars))

                chars[i] = chars[i].upper()
                dq.append(''.join(chars))

        return list(dq)



if __name__ == '__main__':
    S = 'a1b2'
    print(Solution().letterCasePermutation(S))





