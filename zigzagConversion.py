"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"

"""




class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #we need to take of two things just from the bginning
        # which row we are in 
        # which direction we are moving
        #first if the length of string is 1 or the row is 1 we return the string as is
        if numRows==1 or len(s)==1:
            return s
        else:
            d = 1   #keeping track of the direction. 1 denotes the down and -1 denotes the up
            i = 0   #denotes he current row
            rowList = [[] for _ in range(numRows)]
            for char in s:
                rowList[i].append(char)
                if i==0:
                    d=1 #changing direction to down when the pointer reaches the first row

                if i==numRows-1:
                    #since the last row is reached we should reverse the direction for the next iteration
                    d=-1

                #increment the value of rows according to the direction chosesn
                i+=d
            result = ""
            for i in range(numRows):
                result+="".join(rowList[i])

            return result