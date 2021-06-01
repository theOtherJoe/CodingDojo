// Using the given array:
var testArr = [6,3,5,1,2,4];
var sum = 0;
var newArr = [];
// 1. Print Values and Sum
//  1.1 Print each array value and the sum so far

for(var i = 0; i < testArr.length; i++) {
    sum += testArr[i];
    console.log("Num", testArr[i] + ", " + "Sum", sum);
//  2. Value * Position
//      2.1 Multiply each value in the array by its array position
    newArr.push(i * testArr[i]);
}
console.log(newArr);