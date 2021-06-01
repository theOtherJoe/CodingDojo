// Predict 1 ---> 
for(var num = 0; num < 15; num++){
    console.log(num);
}

// This for loop starts the counter (num) at 0, and for each increment IF the number is less than
// 15, log the number to the console, then increment number, and cycle through the loop again
// (until the number is no longer less than 15).

//-----------------------------------------

// Predict 2 ---> 
for(var i = 1; i < 10; i+=2){
    if(i % 3 == 0){
        console.log(i);
    }
}

// This for loop sets the counter (i) to 1, for each increment IF i is less than 10 AND IF i is
// divisible by 3, log i to the conole and add 2 to i, then cylce through again until i is no
// longer less than 10.

//-----------------------------------------

// Predict 3 ---> 
for(var j = 1; j <= 15; j++){
    if(j % 2 == 0){
        j+=2;
    }
    else if(j % 3 == 0){
        j++;
    }
    console.log(j);
}

// This for loop sets the counter (j) to 1, for each increment IF j is less than or equal to 15
// AND IF j is divisible by 2, add 2 to j, log j to the console, and also add 1 to j and then
// cycle through again, if j IS NOT divisible by 2, check if j is divisible by 3, if it is just
// increment j plus one, log j to the console, and then add one again as the increment is already
// set in the for loop, if neither the if or else statements are met, still log j to the console
// and increment again (until j is less greater than 15).