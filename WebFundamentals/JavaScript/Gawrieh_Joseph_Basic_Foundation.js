// 1. Get 1 to 255 - Write a function that returns an array with all the numbers from 1 to 255.
function big_ole_array() {
    var arr = [];
    for(var j = 1; j <= 255; j++) {
        arr.push(j);
    }
    return arr;
}
console.log(big_ole_array())

// ---------------------------------------
// 2. Get even 1000 - Write a function that would get the sum of all the even numbers from 1 to 1000.  You may use a modulus operator
// for this exercise.
function sum_of_even() {
    var sum = 0;
    for(var j = 1; j <= 1000; j++) {
        if(j % 2 == 0) {
            sum += j;
        }
        else {
            continue;
        }
    }
    return sum;
}
console.log(sum_of_even());

// ---------------------------------------
// 3. Sum odd 5000 - Write a function that returns the sum of all the odd numbers from 1 to 5000. (e.g. 1+3+5+...+4997+4999).
function sum_of_odds() {
    var sum = 0;
    for(var j = 1; j <= 5000; j++) {
        if(j % 2 !== 0) {
            sum += j;
        }
        else {
            continue;
        }
    }
    return sum;
}
console.log(sum_of_odds());

// ---------------------------------------
// 4. Iterate an array - Write a function that returns the sum of all the values within an array. (e.g. [1,2,5] returns 8. [-5,2,5
// 12] returns 14).
function sum_of_array(arr) {
    var sum = 0;
    for(var j = 0; j < arr.length; j++) {
        sum += arr[j];
    }
    return sum;
}
console.log(sum_of_array([]))

// ---------------------------------------
// 5. Find max - Given an array with multiple values, write a function that returns the maximum number in the array. (e.g. for [-3,3
// 5,7] max is 7)
function find_array_max(arr) {
    var max = 0;
    for(var j = 0; j < arr.length; j++) {
        if(arr[j] > max) {
            max = arr[j];
        }
    }
    return max;
}
console.log(find_array_max([]))

// ---------------------------------------
// 6. Find average - Given an array with multiple values, write a function that returns the average of the values in the array. (e.g.
// for [1,3,5,7,20] average is 7.2)
function find_array_average(arr) {
    var avg = 0;
    var sum = 0;
    for(var j = 0; j < arr.length; j++) {
        sum += arr[j];
    }
    avg = sum / arr.length;
    return avg;
}
console.log(find_array_average([]))

// ---------------------------------------
// 7. Array odd - Write a function that would return an array of all the odd numbers between 1 to 50. (ex. [1,3,5, .... , 47,49]).
// Hint: Use 'push' method.
function find_odd_array(num) {
    var arr = [];
    for(var j = 0; j <= num; j++) {
        if(j % 2 !== 0) {
            arr.push(j);
        }
        else {
            continue;
        }
    }
    return arr;
}
console.log(find_odd_array())

// ---------------------------------------
// 8. Greater than Y - Given value of Y, write a function that takes an array and returns the number of values that are greater than
// Y. For example if arr = [1, 3, 5, 7] and Y = 3, your function will return 2. (There are two values in the array greater than 3,
// which are 5, 7).
function greater_than_y(arr) {
    var Y = 12;
    var count = 0;
    for(var j = 0; j < arr.length; j++) {
        if(arr[j] > Y) {
            count++;
        }
        else {
            continue;
        }
    }
    return count;
}
console.log(greater_than_y([]))

// ---------------------------------------
// 9. Squares - Given an array with multiple values, write a function that replaces each value in the array with the value squared by
// itself. (e.g. [1,5,10,-2] will become [1,25,100,4])
function values_squared(arr) {
    for(var j = 0; j < arr.length; j++) {
        arr[j] = arr[j] ** 2;
    }
    return arr;
}
console.log(values_squared([]))

// ---------------------------------------
// 10. Negatives - Given an array with multiple values, write a function that replaces any negative numbers within the array with the
// value of 0. When the program is done the array should contain no negative values. (e.g. [1,5,10,-2] will become [1,5,10,0])
function replace_negatives(arr) {
    for(var j = 0; j < arr.length; j++) {
        if(arr[j] < 0) {
            arr[j] = 0;
        }
        else {
            continue;
        }
    }
    return arr;
}
console.log(replace_negatives([]))

// ---------------------------------------
// 11. Max/Min/Avg - Given an array with multiple values, write a function that returns a new array that only contains the maximum,
// minimum, and average values of the original array. (e.g. [1,5,10,-2] will return [10,-2,3.5])
function max_min_avg_array(arr) {
    var max = arr[0];
    var sum = 0;
    var min = 0;
    for(var j = 0; j < arr.length; j++) {
        if(arr[j] > max) {
            max = arr[j];
        }
        if(arr[j] < max) {
            min = arr[j];
        }
        sum += arr[j];
    }
    var avg = sum / arr.length;
    return [max,min,avg];
}
console.log(max_min_avg_array([]))

// ---------------------------------------
// 12. Swap Values - Write a function that will swap the first and last values of any given array. The default minimum length of the array is 2. (e.g. [1,5,10,-2]
// will become [-2,5,10,1]).
function swap_array_values(arr) {
    var temp_arr_val = 0;
    for(var j = 0; j < arr.length - 1; j++) {
        temp_arr_val = arr[0];
        arr[0] = arr[arr.length - 1];
        arr[arr.length - 1] = temp_arr_val;
    }
    return arr;
}
console.log(swap_array_values([]))

// ---------------------------------------
// 13. Number to String - Write a function that takes an array of numbers and replaces any negative values within the array with the string 'Dojo'. For example if
// array = [-1,-3,2], your function will return ['Dojo','Dojo',2].
function number_to_string(arr) {
    for(var j = 0; j < arr.length; j++) {
        if(arr[j] < 0) {
            arr[j] = "Dojo";
        }
        else {
            continue;
        }
    }
    return arr;
}
console.log(number_to_string([]))