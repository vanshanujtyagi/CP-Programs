class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int: #accounts is a list of list
        richest=0 #initially richest=0
        for i in accounts: #check for each list in the accounts list. i is a list.
            current_wealth=sum(i) #current_wealth is the sum of all elements of list i. ie the wealth of a customer.
            richest=(max(richest,current_wealth))  #richest is the maximum between richest (initial 0) and current_wealth. 
        return richest #print richest
