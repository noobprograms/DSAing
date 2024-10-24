/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
    var values = 
                 [   ["M",1000],
                 ["CM",900],["D",500],["CD",400],["C",100],
                    ["XC",90],["L",50],["XL",40],["X",10],
                    ["IX",9],["V",5],["IV",4],["I",1],
                 ]
    var result = "";
    for(let i of values){
        if(Math.floor(num/i[1])){
            let countm = Math.floor(num/i[1]);
            result+=i[0].repeat(countm);
            num = num%i[1]
        }

    }
    return result;

};