// 1. Sigma - Implement function sigma(num) that, given a number, returns the sum of all positive integers up to the given number
// (inclusive).  Ex: sigma(3) = 6 (or 1+2+3); sigma(5) = 15 (or 1+2+3+4+5).
function sigma(num) {
    var sum = 0;
    for(var j = 0; j <= num; j++) {
        sum += j;
    }
    return sum;
}
console.log(sigma());

// 2. Factorial - Write a function factorial(num) that, given a number, returns the product (multiplication) of all positive integers
// from 1 up to the given number (inclusive).  For example, factorial(3) = 6 (or 1*2*3); factorial(5) = 120 (or 1*2*3*4*5).
function factorial(num) {
    var sum = 1;
    for(var j = 1; j <= num; j++) {
        sum *= j; 
    }
    return sum;
}
console.log(factorial());

// 3. Fibonacci - Create a function to generate Fibonacci numbers.  In this famous mathematical sequence, each number is the sum of
// the previous two, starting with values 0 and 1.  Your function should accept one argument, an index into the sequence (where 0
// corresponds to the initial value, 4 corresponds to the value four later, etc).  Examples: fibonacci(0) = 0 (given), fibonacci(1) =
// 1 (given), fibonacci(2) = 1 (fib(0)+fib(1), or 0+1), fibonacci(3) = 2 (fib(1) + fib(2)3, or 1+1), fibonacci(4) = 3 (1+2), fibonacc
// (5) = 5 (2+3), fibonacci(6) = 8 (3+5), fibonacci(7) = 13 (5+8). 
// Basically, n = n−1 + n−2
function fibonacci(num) {
    var arr = [0,1];
    for(var j = 2; j <= num; j++) {
        arr.push(arr[j-1] + arr[j-2]);
        console.log(arr);
    }
    return arr[num];

}
console.log(fibonacci());

// 4. Array: Second-to-Last: Return the second-to-last element of an array. Given [42, true, 4, "Liam", 7], return "Liam".  If array
// is too short, return null.
function secondToLast(arr) {
    if(arr.length < 3) {
        return null;
    }
    else {
        for(var j = 0; j < arr.length; j++) {
            return arr[arr.length - 2];
        }
    }
}
console.log(secondToLast([]));

// 5. Array: Nth-to-Last: Return the element that is N-from-array's-end.  Given ([5,2,3,6,4,9,7],3), return 4.  If the array is too
// short, return null.
function nthToLast(arr, num) {
    if(arr.length < num) {
        return null;
    }
    else {
        for(var j = 0; j < arr.length; j++) {
            return arr[arr.length - num];
        }
    }
}
console.log(nthToLast([]));

// 6. Array: Second-Largest: Return the second-largest element of an array. Given [42,1,4,3.14,7], return 7.  If the array is too
// short, return null.
function secondLargest(arr) {
    var largest = arr[0];
    var second_largest = arr[arr.length - 1];
    if(arr.length < 3) {
        return null;
    }
    for(var j = 1; j < arr.length; j++) {
        if(arr[j] > largest) {
            largest = arr[j];
        }
    }
    for(var r = 1; r < arr.length; r++) {
        if(arr[r] < largest && arr[r] > second_largest) {
            second_largest = arr[r];
        }
    }
    console.log(largest);
    return second_largest;
}
console.log(secondLargest([]));

// 7. Double Trouble: Create a function that changes a given array to list each existing element twice, retaining original order. 
// Convert [4, "Ulysses", 42, false] to [4,4, "Ulysses", "Ulysses", 42, 42, false, false].
function doubleTrouble(arr) {
    var newArr = [];
    for(var j = 0; j < arr.length; j++) {
        newArr.push(arr[j],arr[j]);
    }
    return newArr;
}
console.log(doubleTrouble([]));