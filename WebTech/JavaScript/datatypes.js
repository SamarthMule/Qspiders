// //  Data Types
// JavaScript has 8 data types:
// 1. Number: Represents both integer and floating-point numbers.
// 2. String: Represents a sequence of characters enclosed in quotes (single, double, or backticks).
// 3. Boolean: Represents a logical entity and can have two values: true or false.
// 4. Undefined: A variable that has been declared but has not yet been assigned a value is of type undefined.
// 5. Null: Represents the intentional absence of any object value. It is a primitive value that represents "nothing" or "empty".
// 6. Symbol: A unique and immutable primitive value that can be used as the key of an object property. Introduced in ES6 (ECMAScript 2015).
// 7. BigInt: A numeric data type that can represent integers with arbitrary precision. Introduced in ES11 (ECMAScript 2020).
// 8. Object: A non-primitive data type that is used to store collections of data and more complex entities. Objects can be created using object literals, constructor functions, or the Object.create() method.


// // Number
// let num1 = 42; // Integer
// let num2 = 3.14; // Floating-point number
// let num3 = 1e6; // Exponential notation (1 million) 
// let num4 = 0b1010; // Binary notation (10 in decimal)
// let num5 = 0o12; // Octal notation (10 in decimal)
// let num6 = 0xA; // Hexadecimal notation (10 in decimal)
// let num7 = NaN; // Not a Number (result of an invalid mathematical operation)
// let num8 = Infinity; // Represents positive infinity
// let num9 = -Infinity; // Represents negative infinity
// let num10 = 0; // Represents zero
// let num11 = Number.MAX_VALUE; // Maximum representable number in JavaScript
// let num12 = Number.MIN_VALUE; // Minimum representable number in JavaScript
// let num13 = Number.POSITIVE_INFINITY; // Positive infinity
// let num14 = Number.NEGATIVE_INFINITY; // Negative infinity
// let num15 = Number.NaN; // Not a Number

// console.log(num1); // 42
// console.log(num2); // 3.14
// console.log(num3); // 1000000
// console.log(num4); // 10
// console.log(num5); // 10
// console.log(num6); // 10
// console.log(num7); // NaN
// console.log(num8); // Infinity
// console.log(num9); // -Infinity
// console.log(num10); // 0
// console.log(num11); // 1.7976931348623157e+308
// console.log(num12); // 5e-324
// console.log(num13); // Infinity
// console.log(num14); // -Infinity
// console.log(num15); // NaN

// // String
// let str1 = "Hello, World!"; // Double quotes
// let str2 = 'Hello, World!'; // Single quotes
// let str3 = `Hello, World!`; // Backticks (template literals)
// let str4 = "Hello, I'm John"; // Single quote inside double quotes
// let str5 = 'Hello, I\'m John'; // Escape single quote inside single quotes
// let str6 = "Hello, \"John\""; // Escape double quote inside double quotes
// let str7 = `Hello, ${str1}`; // Template literal with variable interpolation

// log(str1); // Hello, World!
// log(str2); // Hello, World!
// log(str3); // Hello, World!
// log(str4); // Hello, I'm John
// log(str5); // Hello, I'm John
// log(str6); // Hello, "John"
// log(str7); // Hello, Hello, World!

// // Boolean
// let bool1 = true; // Boolean true
// let bool2 = false; // Boolean false
// let bool3 = Boolean(1); // Converts 1 to true
// let bool4 = Boolean(0); // Converts 0 to false
// let bool5 = Boolean(""); // Converts empty string to false
// let bool6 = Boolean("Hello"); // Converts non-empty string to true
// let bool7 = Boolean(null); // Converts null to false
// let bool8 = Boolean(undefined); // Converts undefined to false
// let bool9 = Boolean(NaN); // Converts NaN to false
// let bool10 = Boolean({}); // Converts empty object to true
// let bool11 = Boolean([]); // Converts empty array to true

// console.log(bool1); // true
// console.log(bool2); // false
// console.log(bool3); // true
// console.log(bool4); // false
// console.log(bool5); // false
// console.log(bool6); // true
// console.log(bool7); // false
// console.log(bool8); // false
// console.log(bool9); // false
// console.log(bool10); // true
// console.log(bool11); // true

// // Undefined
// let undef1; // Variable declared but not initialized
// let undef2 = undefined; // Explicitly set to undefined
// let undef3 = null; // Explicitly set to null (not the same as undefined)

// let undef4 = {}; // Empty object
// let undef5 = []; // Empty array
// let undef6 = ""; // Empty string

// console.log(undef1); // undefined
// console.log(undef2); // undefined
// console.log(undef3); // null
// console.log(undef4); // {}
// console.log(undef5); // []
// console.log(undef6); // ""

// // Null
// let null1 = null; // Explicitly set to null
// let null2 = undefined; // Explicitly set to undefined (not the same as null)

// console.log(null1); // null
// console.log(null2); // undefined

// console.log(typeof null1); // object (this is a known quirk in JavaScript)
// console.log(typeof null2); // undefined

// // Symbol
// let sym1 = Symbol("description"); // Unique symbol
// let sym2 = Symbol("description"); // Symbol with a description

// console.log(sym1); // Symbol(description)
// console.log(sym2); // Symbol(description)

// let notSym = "description"; // String (not a symbol)
// let notSym2 = "description"; // String (not a symbol)
// console.log(notSym); // description
// console.log(notSym2); // description

// console.log(notSym === notSym2); // true (strings are equal)
// console.log(sym1 === sym2); // false (symbols are unique)
// console.log(typeof sym1); // symbol


// // BigInt
// let bigInt1 = BigInt(1234567890123456789012345678901234567890); // BigInt from a number
// let bigInt2 = BigInt("1234567890123456789012345678901234567890"); // BigInt from a string
// let bigInt3 = 1234567890123456789012345678901234567890n; // BigInt literal
// let bigInt4 = 1234567890123456789012345678901234567890; // Regular number (not BigInt)

// console.log(bigInt1); // 1234567890123456789012345678901234567890n
// console.log(bigInt2); // 1234567890123456789012345678901234567890n
// console.log(bigInt3); // 1234567890123456789012345678901234567890n
// console.log(bigInt4); // 1234567890123456789012345678901234567890 (regular number)
// console.log(typeof bigInt1); // bigint
// console.log(typeof bigInt2); // bigint
// console.log(typeof bigInt3); // bigint
// console.log(typeof bigInt4); // number (not bigint)
// console.log(bigInt1 === bigInt2); // true (both are equal)

// // Object
// let obj1 = { name: "John", age: 30 }; // Object literal
// let obj2 = new Object(); // Object constructor

// console.log(obj1); // { name: "John", age: 30 }
// console.log(obj2); // {}
// console.log(typeof obj1); // object


// // Example 1
// // let product1 = parseInt(prompt("Enter your first product price"));
// // let product2 = parseInt(prompt("Enter your second product price"));
// // let product3 = parseInt(prompt("Enter your third product price"));
// // let product4 = parseInt(prompt("Enter your fourth product price"));

// let product1 = parseInt(document.getElementById("product1").value);
// let product2 = parseInt(document.getElementById("product2").value);
// let product3 = parseInt(document.getElementById("product3").value);
// let product4 = parseInt(document.getElementById("product4").value);
// let total = 0;

// function calculateTotal() {
//     let product1 = parseInt(document.getElementById("product1").value);
//     let product2 = parseInt(document.getElementById("product2").value);
//     let product3 = parseInt(document.getElementById("product3").value);
//     let product4 = parseInt(document.getElementById("product4").value);

//     let total = product1 + product2 + product3 + product4;
//     console.log(total);
    
//     if (total >= 5000) {
//         document.getElementById("result").innerHTML = "Dear customer, Congrats! You won a voucher of 20% discount on your purchase amount: " + total + " Rs.<br>Your discount voucher is: " + (total * 0.2) + " Rs.<br>Your total amount after discount is: " + (total - (total * 0.2)) + " Rs.";
//     }
//     else {
//         document.getElementById("result").innerHTML = "Dear Customer, buy some more products to get a discount voucher. Your are " + (5000 - total) + " Rs. away from the discount voucher.";
//     }
// }
// function reset() {
//     document.getElementById("product1").value = "";
//     document.getElementById("product2").value = "";
//     document.getElementById("product3").value = "";
//     document.getElementById("product4").value = "";
//     document.getElementById("result").innerHTML = "";
// }

// Example 2
// let gender = prompt("Enter your gender:");
// let state = "Andhra Pradesh"; // Assuming the state is Andhra Pradesh for this example

// if (gender == "female" && state == "Andhra Pradesh") {
//     document.writeln("Bus ticket is Free");
// }
// else {
//     document.writeln("Bus ticket is 100 Rs.");
//     document.writeln("Thank you for your understanding.");
// }


// Example 3
Bike = 7
Auto = 4
Car = 2

let Location = prompt("Enter your location:");
let distance = parseInt(prompt("Enter the distance in km:"));
let mode = prompt("Enter your mode of transport (Bike, Auto, Car):");

if (mode == "Bike"){
    document.writeln("You location is "+ Location + " and the distance is " + distance + " km.");
    document.writeln("<br>You have selected Bike as your mode of transport. The cost per km is " + Bike + " Rs.");
    document.writeln("<br>So the cost of your travel is " + (distance * Bike) + " Rs.");
}
else if (mode == "Auto"){
    document.writeln("You location is "+ Location + " and the distance is " + distance + " km.");
    document.writeln("<br>You have selected Auto as your mode of transport. The cost per km is " + Auto + " Rs.");
    document.writeln("<br>So the cost of your travel is " + (distance * Auto) + " Rs.");
}
else if (mode == "Car"){
    document.writeln("You location is "+ Location + " and the distance is " + distance + " km.");
    document.writeln("<br>You have selected Car as your mode of transport. The cost per km is " + Car + " Rs.");
    document.writeln("<br>So the cost of your travel is " + (distance * Car) + " Rs.");
}
else {
    document.writeln("Invalid mode of transport selected. Please select either Bike, Auto, or Car.");
}