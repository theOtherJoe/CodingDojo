// Predict 1
var arr = [8,6,7,5,3,0,9]
for(var i = 0; i < arr.length; i++){    
    console.log(arr[i]);
}

// This loop sets the index (i) to 0 which is the start of the array (arr), it then increments through as long as i is less than the array length, logging each index
// item (i) of the array to the console, then incrememting the index by 1. 
// -------------------------------------

// Predict 2
var arr = [7,3,8,4,2,0,1];
for(var i = 0; i < arr.length; i++){ 
    if(arr[i] % 2 == 0){
        console.log(arr[i]);
    } 
    else{
        console.log("That is odd!");
    }
}

// This loop sets the index (i) to 0, as long as i is less than the array length, it will increment through and then check if the index is divisible by 2, if it is
// it will log it to the console, if not it will log "That is odd!" to the console, increment by 1 and repeat the loop (until i is no longer less than the array length).
// -------------------------------------

// Predict 3
var arr = [1,3,8,-5,0,-2,4,-1];
var newArr = [];
for(var i = 0; i< arr.length; i++){
    if(arr[i] < 0){
        newArr.push(arr[i]);
        arr[i] = arr[i] * -1;
    }
    else if(arr[i] == 0){
        arr[i] = "Zero";
    }
    else{
        arr[i] = arr[i] * -1;
    }
}
console.log(arr);
console.log(newArr);

// This loop starts the index (i) at 0, as long as i is less than the length of the array, it will increment through and check if the index (i) is less than 0, if it is it's going to push that index to the new (empty) array (newArr) and then it will multiply the index by -1, setting it negative. If the index is not less than 0, it will check if the index is equal to 0, if it is it's going to set the index equal to the string "Zero". If niether of the previous checks were satisifed, it will multiply the index by -1, making it negative. It will then add 1 to the increment and loop through until i is no longer less than the length of the array. Once that completes it will log both the original array (arr) and the new array (newArr) to the console.