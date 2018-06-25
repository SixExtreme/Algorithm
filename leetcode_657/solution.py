class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x, y = 0, 0
        for step in moves:
            if step is 'L':
                x -= 1
            if step is 'R':
                x += 1
            if step is 'U':
                y += 1
            if step is 'D':
                y -= 1
        return (x, y) == (0, 0)