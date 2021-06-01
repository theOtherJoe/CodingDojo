// Predict 1
function greeting(){
    return "Hello";
    console.log("World");
}
var word = greeting();
console.log(word);

// This function sets the variable "word" equal to the function "greeting()". When console.log(word) is called, the function will log "Hello" to the console. Within the function, console.log("World") will not get executed since the return exits the function when hit. 
// -------------------------------------

// Predict 2
function add(num1, num2){
    console.log("Summing Numbers!");
    console.log("num1 is: " + num1);
    console.log("num2 is: " + num2);
    var sum = num1 + num2;
    return sum;
}
var result1 = add(3,5);
var result2 = add(4,7);
console.log(result1);
console.log(result2);

// When this block of code is executed, it will hit "var result1" first, which will output all 3 console.log statements to the console, then it sets the var sum
// equal to 3 + 5, then returns the value of sum and exits the function. Then it will hit the next line which is "var result2", which will then do the same thing as
// result1, in the end returning 11 for sum. Next it will hit console.log(result1) which will output 8 to the console, and then move on to console.log(result2) which
// will return 11 to the console. 
// -------------------------------------

// Predict 3
function highFive(num){
    for(var i=0; i<num; i++){
        if(i == 5){
            console.log("High Five!");
        }
        else{
            console.log(i);
        }
    }
}

// This function won't return or output anything because it's not actually being called. 