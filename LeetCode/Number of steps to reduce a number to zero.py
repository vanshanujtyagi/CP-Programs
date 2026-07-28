class Solution: #leetcode default
    def numberOfSteps(self, num: int) -> int: #leetcode default for num=int(input())
        steps = 0 

        while num != 0: #runs and stops if num becomes 0.
            if num % 2 == 0: #check for even
                num = num // 2
            else: #automatically odd
                num = num - 1

            steps = steps + 1

        return steps #leetcode default for print(steps)
