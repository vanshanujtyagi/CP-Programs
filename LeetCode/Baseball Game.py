class Solution:
    def calPoints(self, operations: List[str]) -> int: #leetcode default for operations=list(input().split())
        score = [] #empty list to store scores

        for i in operations:
            if i not in ['+', 'D', 'C']: #if operator is not in ['+', 'D', 'C'] then, in this question, its a integer.
                score.append(int(i)) #if its the integer append it in the score. The default format iw string, so first convert into int before storing
            elif i == '+': #if the operator is +
                score.append(score[-1] + score[-2]) #append the sum of last and last second integers of score
            elif i == 'D': #if the operator is D
                score.append(2 * score[-1]) #append the double of the last int in score
            elif i == 'C': #if the operator is C
                score.pop() # .pop() by default removes the last item of the given list

        return sum(score) # sum() function adds all the elements of a list/tuple.
