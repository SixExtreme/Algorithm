class Solution:
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        cx, cy, angle, _max_distance = 0, 0, 90, 0
        obstacles = {tuple(ob) for ob in obstacles}
        directs =((1, 0), (0, 1), (-1, 0), (0, -1))

        def turn(cmd):
            nonlocal angle
            angle = angle - 90 if cmd == -1 else angle + 90
            angle = (angle + 360) % 360

        def move(cmd):
            nonlocal cx, cy, _max_distance
            dx, dy = directs[angle // 90]
            for _ in range(0, cmd):
                nx, ny = cx + dx, cy + dy
                if (nx, ny) in obstacles:
                    break
                cx, cy = nx, ny
                _max_distance = max(_max_distance, cx * cx + cy * cy)

        for command in commands:
            if command < 0:
                turn(command)
            else:
                move(command)

        return _max_distance

if __name__ == '__main__':
    commands = [4, -1, 4, -2, 4]
    obstacles = [[2, 4]]
    print(Solution().robotSim(commands, obstacles))