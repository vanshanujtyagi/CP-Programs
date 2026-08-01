class Solution: 
    def mostWordsFound(self, sentences: List[str]) -> int: #leetcode default for input. sentences is a list of strings
        words=[] #empty list words
        lengths=[] #empty list lengths
        for i in sentences: #loop for each string in input sentences.
            words.append(i.split()) #split each string into a list of strings separated by spaces, and append the list into words 
          #we have found the words now in a list called words which is a list of lists of strings. each list represents the words of a single sentence.
        for i in words: #words is a list of lists of strings. check for each individual list in words
            lengths.append(len(i)) #find the length of each list in words, then append the values in lengths.
         #we have found the number of words in each sentence, the value is stored in a list called lengths.
        return max(lengths) #now, lengths is a list containing integer values. find the max value
