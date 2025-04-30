// declaration
var a;
console.log(a); // undefined


// initialization
a = 10;
console.log(a); // 10

// redeclaration
var a;
console.log(a); // 10

// reinitialization
a = 20;
console.log(a); // 20


let nam;
nam = "John";
console.log(nam); // John
// let name;  // SyntaxError: Identifier 'name' has already been declared
nam = "Doe";
console.log(nam); // Doe

// const place; // SyntaxError: Missing initializer in const declaration
const place = "Pune";
console.log(place); // Pune
// const place = "Delhi"; // TypeError: Assignment to constant variable.
// place = "Delhi"; // TypeError: Assignment to constant variable.

