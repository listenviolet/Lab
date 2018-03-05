class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if not s:
            return 0
        longestlength = 1
        substr = ""
        for item in s:
            if item not in substr:
                substr += item
            else:
                if len(substr) > longestlength:
                    longestlength = len(substr)
             
                #将重复字符加入substr
                substr += item
                # 应该从substr中第一次出现重复字符的下一个字符开始继续判断
                substr = substr[substr.index(item) + 1:]
        
        if len(substr) > longestlength:
            longestlength = len(substr)
        return longestlength
        