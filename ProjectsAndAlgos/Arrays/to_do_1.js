// Push Front
function pushFront(arr, newVal) {
    for(var j = arr.length - 1; j >= 0; j--) {
        arr[j + 1] = arr[j];
    }
    arr[0] = newVal;
    return arr;
}
console.log(pushFront([6,12,17,3,7], 4));

// Pop Front (Basically will need to reverse the array to pop the first item)
function popFront(arr) {
    for(var j = 0; j < (arr.length / 2); j++) {
        [arr[j], arr[arr.length -1 -j]] = [arr[arr.length -1 -j], arr[j]];
    }
    return arr.pop();
}
console.log(popFront([14,2,7,5,10]));

// Insert At
function insertAt(arr, ind, newVal) {
    for(var j = arr.length -1; j >= arr.length -1; j--) {
        arr[j + 1] = arr[j];
    }
    arr[ind] = newVal;
    return arr;
}
console.log(insertAt([6,12,17,3,7], 4, 5))

