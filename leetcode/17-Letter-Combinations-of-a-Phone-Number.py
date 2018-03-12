class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        if digits == '':
            return []
        self.DigitDict=[' ','1', "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = ['']
        for d in digits:
            res = self.letterCombBT(int(d),res)
        return res

    def letterCombBT(self, digit, oldStrList):
        return [dstr+i for i in self.DigitDict[digit] for dstr in oldStrList]

        #就是用递归或者dfs，比如给‘234’吧，先看2，那现在应该是[‘a’,’b’,’c’]， 
        #再加上3呢，在这个[‘a’,’b’,’c’]的基础上，
        #[‘a’,’b’,’c’]每一个的后面分别加上‘d’,’e’,’f’：
        #也就是 [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf”]， 
        #然后再加4的’g”h”i’，以此类推。