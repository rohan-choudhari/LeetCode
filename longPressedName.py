"""
Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.



Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
Example 3:

Input: name = "leelee", typed = "lleeelee"
Output: true
Example 4:

Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.
"""

import pdb
class Solution:
    def isLongPressed(self, name, typed):

        #pdb.set_trace()
        let = typed[0]
        while typed:
            if name[0] == typed[0]:
                del name[0]
                let = typed.pop(0)
            elif typed[0] == let:
                let = typed.pop(0)
            else:
                print(False)
                return
        print(True)

leetCode = Solution()
if 0: 
    name="alex"
    typed = "aaleex"
elif 1: 
    name = "saeed"
    typed = "ssaaedd"
elif 0:
    name = "leelee"
    typed = "lleeelee"
elif 0:
    name = "laiden" 
    typed = "laiden"

name = list(name)
typed = list(typed)
leetCode.isLongPressed(name, typed)
