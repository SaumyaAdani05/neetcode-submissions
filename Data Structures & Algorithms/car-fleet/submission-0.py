class Solution:
    def carFleet(self, target, position, speed):
        cars = sorted(
            [(p, (target - p) / s) for p, s in zip(position, speed)],
            reverse=True
        )
        fleets = 0
        last_time = 0
        for _, time in cars:
            if time > last_time:
                fleets += 1
                last_time = time
        return fleets