'''
944. Delete Columns to Make Sorted

You are given an array of n strings strs, all of the same length.
The strings can be arranged such that there is one on each line, 
making a grid. For example, strs = ["abc", "bce", "cae"] can be arranged as:

abc
bce
cae

You want to delete the columns that are not sorted lexicographically. 
In the above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') 
are sorted while column 1 ('b', 'c', 'a') is not, so you would delete column 1.

Return the number of columns that you will delete.

Example 1:
Input: strs = ["cba","daf","ghi"]
Output: 1
Explanation: The grid looks as follows:
  cba
  daf
  ghi
Columns 0 and 2 are sorted, but column 1 is not, so you only need to delete 1 column.

Example 2:
Input: strs = ["a","b"]
Output: 0
Explanation: The grid looks as follows:
  a
  b
Column 0 is the only column and is sorted, so you will not delete any columns.

Example 3:
Input: strs = ["zyx","wvu","tsr"]
Output: 3
Explanation: The grid looks as follows:
  zyx
  wvu
  tsr
All 3 columns are not sorted, so you will delete all 3.
 
Constraints:
n == strs.length
1 <= n <= 100
1 <= strs[i].length <= 1000
strs[i] consists of lowercase English letters.
'''

# Code

''' 
Possible cases:
# e = e (no issue)
# a < b (no issue)
# c > a (unsorted)

What we need is to check if the value in the previous cell is greater than the next 
and deleting it. We create a dictionary that all columns set to zero, which means that 
no columun deleted. And then we loop over all strings and check if we encounter with the 3rd 
case, if we do encounter then we set that columns value to 1. At end we return sum of all values.'''

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        col_l = len(strs[0])
        row_l = len(strs)

        dic = {i: 0 for i in range(col_l)}
        for i in range(1, row_l):
            for j in range(col_l):
                if strs[i][j] < strs[i-1][j]:
                    dic[j] = 1
        print(dic)
        return sum(dic.values())
        
# For any kind of discussion I put my contacts here:
# farhad.szd@gmail.com
# +994557367002 (WhatsApp)
# @farhad_zada_ (instagram)
