// 1. Biggie Size - Given an array, write a function that changes all positive numbers in the array to the string "big".  Example:
// makeItBig([-1,3,5,-5]) returns that same array, changed to [-1, "big", "big", -5].
function biggieSize(arr) {
    for(var j = 0; j < arr.length; j++) {
        if(arr[j] > 0) {
            arr[j] = "big";
        }
    }
    return arr;
}
console.log(biggieSize([]));

// 2. Print Low, Return High - Create a function that takes in an array of numbers.  The function should print the lowest value in
// the array, and return the highest value in the array.
function printLowReturnHigh(arr) {
    var highest_num = arr[0];
    var lowest_num = arr[arr.length -1];
    for(var j = 0; j < arr.length; j++) {
        if(arr[j] > highest_num) {
            highest_num = arr[j];
        }
        if(arr[j] < lowest_num) {
            lowest_num = arr[j];
        }
    }
    console.log(`This is the lowest number: ${lowest_num}`);
    return highest_num;
}
console.log(printLowReturnHigh([]));

// 3. Print One, Return Another - Build a function that takes in an array of numbers.  The function should print the second-to-last
// value in the array, and return the first odd value in the array.
function printOneReturnAnother(arr) {
    for(var j = 0; j < arr.length; j++) {
        if(arr[j] % 2 !== 0) {
            var first_odd = arr[j];
        }
    }
    console.log(`This is the second to last number in the array: ${arr[arr.length -2]}`);
    return first_odd;
}
console.log(printOneReturnAnother([]));

// 4. Double Vision - Given an array (similar to saying 'takes in an array'), create a function that returns a new array where each
// value in the original array has been doubled.  Calling double([1,2,3]) should return [2,4,6] without changing the original array.
function doubleVision(arr) {
    for(var j = 0; j < arr.length; j++) {
        arr[j] = arr[j] * 2;
    }
    return arr;
}
console.log(doubleVision([12,4,8,6]));

// 5. Count Positives - Given an array of numbers, create a function to replace the last value with the number of positive values
// found in the array.  Example, countPositives([-1,1,1,1]) changes the original array to [-1,1,1,3] and returns it.
function countThePositives(arr) {
    var count = 0;
    for(var j = 0; j < arr.length; j++) {
        if(arr[j] > 0) {
            count++;
        }
        arr[arr.length - 1] = count;
    }
    return arr;
}
console.log(countThePositives([]));

// 6. Evens and Odds - Create a function that accepts an array.  Every time that array has three odd values in a row, print "That's
// odd!".  Every time the array has three evens in a row, print "Even more so!".
function evensAndOdds(arr) {
    var odd_count = 0;
    var even_count = 0;
    for(var j = 0; j < arr.length; j++) {
        if(arr[j] % 2 !== 0) {
            odd_count++;
            even_count = 0;
            console.log(`There is ${odd_count} odd number(s) in a row so far!`);
            if(odd_count == 3) {
                console.log("That's odd!");
                odd_count = 0;
            }
        }
        if(arr[j] % 2 == 0) {
            even_count++;
            odd_count = 0;
            console.log(`There is ${even_count} even number(s) in a row so far!`);
            if(even_count == 3) {
                console.log("Even more so!");
                even_count = 0;
            }
        }
    }
    return arr; // Just so we're not returning undefined :) 
}
console.log(evensAndOdds([12,4,4,1,3,5,2,1,3,4,6,8]));

// 7. Increment the Seconds - Given an array of numbers arr, add 1 to every other element, specifically those whose index is odd (arr[1], arr[3], arr[5], etc). 
// Afterward, console.log each array value and return arr.
function incrementTheSeconds(arr) {
    for(var j = 1; j < arr.length; j += 2) {
        arr[j] = arr[j] + 1;
    }
    console.log(arr);
    return arr;
}
console.log(incrementTheSeconds([]));

// 8. Previous Lengths - You are passed an array (similar to saying 'takes in an array' or 'given an array') containing strings.  Working within that same array, replace
// each string with a number - the length of the string at the previous array index - and return the array.  For example, previousLengths(["hello", "dojo", "awesome"])
// should return ["hello", 5, 4]. Hint: Can for loops only go forward?
function previousLengths(arr) {
    for(var j = arr.length -1; j > 0; j--) {
        arr[j] = arr[j - 1].length;
    }
    return arr;
}
console.log(previousLengths([]));

// 9. Add Seven - Build a function that accepts an array. Return a new array with all the values of the original, but add 7 to each. Do not alter the original array. 
// Example, addSeven([1,2,3]) should return [8,9,10] in a new array.
function addSeven(arr) {
    var newArr = [];
    for(var j = 0; j < arr.length; j++) {
        newArr.push(arr[j] + 7);
    }
    console.log(arr);
    return newArr;
}
console.log(addSeven([]));

// 10. Reverse Array - Given an array, write a function that reverses its values, in-place.  Example: reverse([3,1,6,4,2]) returns the same array, but now contains
// values reversed like so... [2,4,6,1,3].  Do this without creating an empty temporary array.  (Hint: you'll need to swap values).
function reverseArray(arr) {
    for(var i = arr.length -1; i >= 0; i--) {
        console.log(arr[i]);
        arr[i] = arr[i];
    }
    return arr;
}
console.log(reverseArray([3,1,6,4,2]));