// // declaration
// var a;
// console.log(a); // undefined


// // initialization
// a = 10;
// console.log(a); // 10

// // redeclaration
// var a;
// console.log(a); // 10

// // reinitialization
// a = 20;
// console.log(a); // 20


// let nam;
// nam = "John";
// console.log(nam); // John
// // let name;  // SyntaxError: Identifier 'name' has already been declared
// nam = "Doe";
// console.log(nam); // Doe

// // const place; // SyntaxError: Missing initializer in const declaration
// const place = "Pune";
// console.log(place); // Pune
// // const place = "Delhi"; // TypeError: Assignment to constant variable.
// // place = "Delhi"; // TypeError: Assignment to constant variable.

// Hoisting
// Hoisting is a JavaScript mechanism where variables and function declarations are moved to the top of their scope during the compile phase. This means that you can use variables and functions before they are declared in the code.
// However, only the declarations are hoisted, not the initializations. This can lead to unexpected behavior if you're not careful.
// For example, if you try to access a variable before it's declared, you'll get `undefined` instead of a `ReferenceError`.

// Example of hoisting with var
console.log(x); // undefined  
x = 15; // Initialization
console.log(x); // 15
var x; // Declaration and initialization
x = 51; // Reinitialization
console.log(x); // 51