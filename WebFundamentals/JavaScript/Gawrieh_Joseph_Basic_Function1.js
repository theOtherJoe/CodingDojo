// 1. 
function a(){
    return 35;
}
console.log(a())
// This function will log 35 to the console.

// --------------------------------------------
// 2.
function a(){
    return 4;
}
console.log(a()+a());
// This function will log 8 to the console.

// --------------------------------------------
// 3. 
function a(b){
    return b;
}
console.log(a(2)+a(4));
// This function will log 6 to the console. 

// --------------------------------------------
// 4. 
function a(b){
    console.log(b);
    return b*3;
}
console.log(a(3));
// This function will log 3 to the console and also log 9 to the console. 

// --------------------------------------------
// 5. 
function a(b){
    return b*4;
    console.log(b);
}
console.log(a(10));
// This function will log 40 to the console and that's it (since the return is before the console.log). 

// --------------------------------------------
// 6. 
function a(b){
    if(b<10) {
        return 2;
    }
    else     {
        return 4;
    }
    console.log(b);
}
console.log(a(15));
// This function will log 4 to the console. 

// --------------------------------------------
// 7. 
function a(b,c){
    return b*c;
}
console.log(10,3);
console.log( a(3,10) );
// This function will log "10 3" to the console, then it will log 30 to the console. 

// --------------------------------------------
// 8. 
function a(b){
    for(var i=0; i<10; i++){
        console.log(i);
    }
    return i;
}
console.log(3);
console.log(4);
// This function will just return 3 and 4 to the console. 

// --------------------------------------------
// 9. 
function a(){
    for(var i=0; i<10; i++){
        i = i +2;
        console.log(i);
    }
}
a();
// This function will log 2, 5, 8, and 11 to the console. 

// --------------------------------------------
// 10. 
function a(b,c){
    for(var i=b; i<c; i++) {
        console.log(i);
    }
    return b*c;
}
a(0,10);
console.log(a(0,10));
// This function will log 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 to the console for the first function call (a(0,10)).
// For the second function call it will do the same thing except it will also return 0 to the console (or better yet, user). 

// --------------------------------------------
// 11. 
function a(){
    for(var i=0; i<10; i++){
        for(var j=0; j<10; j++){
            console.log(j);
        }
        console.log(i);
    }
}
// This function won't log anything to the console because it isn't getting called.

// --------------------------------------------
// 12. 
function a(){
    for(var i=0; i<10; i++){
        for(var j=0; j<10; j++){
            console.log(i,j);
        }
        console.log(j,i);
    }
}
// This function also won't log anything to the console because it isn't getting called.

// --------------------------------------------
// 13. 
var z = 10;
function a(){
    var z = 15;
    console.log(z);
}
console.log(z);
// This function will log 10 to the console.

// --------------------------------------------
// 14. 
var z = 10;
function a(){
    var z = 15;
    console.log(z);
}
a();
console.log(z);
// This function will log 15 to the console for the first function call, then it will log 10 for the console.log since it is being specified as "var" inside of the
// function which then makes it a local variable within the function (that won't affect the global var outside of the function).

// --------------------------------------------
// 15. 
var z = 10;
function a(){
    var z = 15;
    console.log(z);
    return z;
}
z = a();
console.log(z);
// This function will log 15 to the console twice (once for the variable "z" getting assiged the value of a(), and secondly for the console.log call)