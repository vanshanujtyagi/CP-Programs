class Solution:
    def subtractProductAndSum(self, n: int) -> int: #leetcode default to access int value in variable n
        length = len(str(n)) #finds the number of digits in integer by converting it to string and then counting characters
        ones = n % 10 #returns the last digit. for eg. 279%10 is 9
        summ = 0
        product = 1

        for i in range(length - 1): 
            n = n // 10 #returns for eg. 279//10 is 27
            summ = summ + (n % 10) #n%10 gives again the last digit. for eg n is 27, so n%10 gives 7, thus the second last digit
            product = product * (n % 10)

        return (product * ones) - (summ + ones) #default leetcode function to print((product*ones)-(summ+ones))
