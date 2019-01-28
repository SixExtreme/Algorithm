import bisect


class ExamRoom:

    def __init__(self, N):
        """
        :type N: int
        """
        self.N = N
        self.seats = []

    def seat(self):
        """
        :rtype: int
        """
        if len(self.seats) == 0:
            self.seats.append(0)
            return 0

        _max, ret = self.seats[0], 0
        for i in range(1, len(self.seats)):
            a, b = self.seats[i - 1], self.seats[i]
            if (b - a) // 2 > _max:
                _max, ret = (b - a) // 2, (b + a) // 2

        if (self.N - 1) - self.seats[-1] > _max:
            ret = self.N - 1

        bisect.insort(self.seats, ret)
        return ret


    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        for i, s in enumerate(self.seats):
            if s == p:
                del self.seats[i]

if __name__ == '__main__':
