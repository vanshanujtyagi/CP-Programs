import math #import math module as we will need isqrt() function

class Solution:
    def checkPerfectNumber(self, num: int) -> bool: #leetcode default for num=int(input())
        if num == 1: # if input num is 1
            return False #input num 1 can never be a perfect number

        summ = 1 #default sum is 1, as number 1 is always included in the sum of a perfect number

        for i in range(2, math.isqrt(num) + 1): #we do not want to include 1 as it is present in our sum above, isqrt(num) finds the integer sqrt
            if num % i == 0: #if i is the divisor of num
                other = num // i #the other divisor of num, in pair with i ie. i*other=num
              
                if other == i: #if the other number is i
                    summ += i #sum=sum+1, so that the number and divisor both cant be added twice
                else: #else i and other are not same
                    summ += i + other #then both divisors shall be added to the sum

        return summ == num #print whether sum is equal to the input number
#if the loop; for i in range(2, math.isqrt(num) + 1): ; would have started with 1, then the other divisor would have the number itself and in the sum of perfect number, the number itself must not be added.
