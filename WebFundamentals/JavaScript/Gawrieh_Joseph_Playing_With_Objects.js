// Imagine that you are given an array of objects.  For example,
var users = [{name: "Michael", age:37}, {name: "John", age:30}, {name: "David", age:27}];
// * How would you print/log John's age?
// * How would you print/log the name of the first object?
// * How would you print/log the name and age of each user using a for loop?  Your output should look something like this
console.log(users[1].age);
console.log(users[0].name);
for(var person in users) {
    console.log(users[person].name + ' - ' + users[person].age);
}