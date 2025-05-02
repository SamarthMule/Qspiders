// Functions
// The function is a block of code that performs a specific task. It is executed when "something" invokes or calls it. Functions are reusable pieces of code that can be called multiple times with different arguments.

// Named Function
function add(a, b) {
    console.log("a + b = " + (a + b));
}
add(5, 10); // Output: a + b = 15
add(20, 30); // Output: a + b = 50
add('Hello ', 'Everyone'); // Output: a + b = 510 (string concatenation)

// Nan = Not a Number - after declaring a parameter in function, if we not pass any value as argument, it will be undefined. If we try to perform any operation on undefined, it will return NaN.

add(5); // Output: a + b = NaN (undefined + 5 = NaN)
add(); // Output: a + b = NaN (undefined + undefined = NaN)

function greet(name) {
    console.log("Hello, " + name + "!");
}
greet("Alice"); // Output: Hello, Alice!
greet("Bob"); // Output: Hello, Bob!

// Function with default parameters
function task(x=20, y=30) {
    console.log("x + y = " + (x + y));
}
task(); // Output: x + y = 50 (default values are used)
task(10); // Output: x + y = 40 (x is 10, y is default 30)
task(10, 20); // Output: x + y = 30 (x is 10, y is 20)

// function task2(a,b){
//     let a = 10; // Identifier 'a' has already been declared (local variable)
//     let b = 30; // Identifier 'b' has already been declared (local variable)
//     console.log("a + b = " + (a + b)); 
// }

function task2(a,b){
    var a = 10; 
    var b = 30;
    console.log("a + b = " + (a + b));
}
task2(5, 15); // Output: a + b = 40 (local variables a and b are used)
task2(); // Output: a + b = 40 (local variables a and b are used)

// Unnamed Function (Anonymous Function)
// An anonymous function is a function that does not have a name. It is often used as a callback function or when you want to create a function on the fly without giving it a name.
// Anonymous functions are often used in JavaScript for event handling, callbacks, and functional programming.
// They can be assigned to variables, passed as arguments to other functions, or used as immediately invoked function expressions (IIFE).

// Example of an anonymous function assigned to a variable
// function (){
//     console.log("This is an anonymous function.");
// }

// First-Class Functions (First citizen function / Function with expression) -> Any Function which is assigned to an variable is called First-Class Function.
// In JavaScript, functions are first-class citizens, meaning they can be treated like any other value. This means you can assign functions to variables, pass them as arguments to other functions, return them from other functions, and even create them on the fly.
const firstClassFunction = function() {
    console.log("This is a first-class function.");
};
firstClassFunction();

let multiply = function(a, b) {
    console.log("a * b = " + (a * b));
};

multiply(5, 10); // Output: a * b = 50
multiply(20, 30); // Output: a * b = 600

const divide = function(a, b) {
    console.log(`a / b = ${(a / b)}`);
}

divide(10, 5); // Output: a / b = 2
divide(20, 4); // Output: a / b = 5

// Arrow Function (Arrow Function)
// An arrow function is a shorter syntax for writing function expressions in JavaScript. It uses the `=>` syntax and does not have its own `this`, `arguments`, or `super` bindings. Arrow functions are often used for short, one-liner functions or when you want to preserve the context of `this` from the surrounding code.
// Arrow functions are particularly useful in functional programming and when working with higher-order functions, such as `map`, `filter`, and `reduce`.
// They are also commonly used in React and other modern JavaScript frameworks for defining components and event handlers.
// It is introduced in ES6 (ECMAScript 2015) and provides a more concise syntax for writing functions. Arrow functions are often used in modern JavaScript development due to their simplicity and readability. 
// It is most used function in React.js and Node.js. because it is having short syntax.

// Example of an arrow function
const subtract = (a, b) => {
    console.log("a - b = " + (a - b));
};
subtract(10, 5); // Output: a - b = 5
subtract(90, 30); // Output: a - b = 60

const square = (x) => x * x; // Shorter syntax for a single expression
console.log(square(5)); // Output: 25

let task3 = () =>{
    console.log("This is an arrow function.");
};

task3(); // Output: This is an arrow function.


// Nested Function
// A nested function is a function defined inside another function. The inner function can access variables and parameters of the outer function, creating a closure. Nested functions are often used for encapsulation and to create private variables or helper functions that are only relevant within the scope of the outer function.

// Note : Not to many functions are nested inside another function. It will create confusion and it is not a good practice.
function outerFunction() {
    let outerVariable = "I am from outer function.";
    console.log(outerVariable); 

    function innerFunction() {
        let innerVariable = "I am from inner function.";
        console.log(innerVariable);
    }
    innerFunction(); // Calling the inner function
}
outerFunction(); // Output: I am from outer function. I am from inner function.