"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.



Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).


Note:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are english lowercase letters.
"""

def alienDictionary(order, dictionary):
    hash_order = {}
    for i in range(len(order)): #O(n)
        hash_order[order[i]] = i  #O(1)
    print(hash_order)

    #dictionary = dictionary.split() #O(n)

    for i in range(0, len(dictionary)-1):
        flag = True
        a = dictionary[i]
        b = dictionary[i+1]
        for j in range(0, len(a)):
            if(hash_order[a[i]] < hash_order[b[i]]):
                break
            elif(hash_order[a[i]]>hash_order[b[i]]):
                flag = False
            if j== len(a)-1:
                if len(a) >  len(b):
                    flag = False
        if(~flag):
            break
    if(flag):
        print("Ordered")
    else:
        print("Unordered")

if 0:
    words = ["word","world","row"]
    order = "worldabcefghijkmnpqstuvxyz"
elif 1:
    words = ["apple","app"]
    order = "abcdefghijklmnopqrstuvwxyz"

alienDictionary(order, words)



                
        



