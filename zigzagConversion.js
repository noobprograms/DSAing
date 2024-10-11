/*
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

*/
/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
    //if the num of rows is 1 or the string only has one character then simply return the string
    if(numRows==1 ||s.length==1){
        return s;
    }
    //lets crate the matrix first
    var rowsList = [];
    for(let i=0;i<numRows;i++){
        rowsList.push([]);
    }
    //now the matrix for addition is ready
    //let create two variables one to keep account of the nth row we are in and the other for direction.
    rowNumber = 0;
    direction = 1;  //1 denotes that we have to move down and -1 denotes we have to move up
    //lets loop over the string to parse its chars
    for(let char of s){
        rowsList[rowNumber].push(char);  //push the character in the respective list
        if(rowNumber==0){   //being in zero row number means we have to move down
            direction = 1
        }
        if(rowNumber ==numRows-1){ //being in the last row means we have to move up
            direction = -1;

        }
        //now lets update the rowNumber according to the direction 
        rowNumber +=direction

    }
    //in the end join all the lists and concatenate into a single string
    var result = ""
    for(let i=0;i<numRows;i++){
        result+=rowsList[i].join("")
    }
    return result

    
};