"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""

class Solution:
    def lengthLastWord(self, str_words):
        x = str_words.split()
        print(len(x[-1]))

str_words = "a dog ran with the fox and lost"
obj = Solution();
obj.lengthLastWord(str_words)


