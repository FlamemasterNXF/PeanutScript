# Complete PeanutScript Overview
PeanutScript, like all languages, has a semi-unique syntax.<br>
Though some syntax may be familiar to users, other syntax may be confusing or totally new.<br>
This guide aims to avoid any confusion by explaining *all* of the language's syntax!<br>
## Variables
____
Variables have 3 types: Number, String, and Array.<br>
These types are dynamically decided based on the value of the Variable. These types can be changed after initial declaration, so be careful.<br>
- Number: A simple numerical value. Can be a Float or an Int. Though the difference is minor and is never made clear this allows for usage of decimals!<br>Ex: `var abcd = 0`
- String: A simple input of letters.<br>Ex: `var abcd = "abcd"`
- Array: A list of many Number or String values.<br>Ex: `var abcd = ["a","b","c","d"]`<br>

### String Interpolation
As mentioned above, Strings are simple combinations of letters.<br>
However, using String Interpolation, you can display variables and even do Mathematical Operations inside a String!<br>
The syntax is a simple extension of usual Strings! Simply putting `${}` anywhere within a String will allow you to put whatever code you want within the curly braces.

### Creating a Variable
Variables can be created simply using the `var` keyword, followed by a name for the Variable, then a `=`, and then finally a value for the Variable.<br>
If you wish, you can create a variable without a default value!<br>
Note that `let` can be used instead of `var`!<br>
### Re-assignment 
Variables can have a new value assigned to them by using the same syntax originally used to create them!<br>
### Accessing a Variable
Numbers and Strings can simply be accessed by typing the variable name.<br>
To access a Variable at the index of an Array you have to do a bit more, but it's still simple. Simply type the Array's name, followed by `/`, and then the index you wish to access. Ex: `array / 0` for index 0.<br>
To access a certain character in a String simply type the String's name, followed by a `/`, and then the index of the character you wish to access. Ex `"hi" / 0` returns "h".<br> 
### Scoped Variables
If you'd like to create a variable that only exists within the scope of its declaration you can use the `scoped` keyword instead!<br>
Scoped Variables work the same as normal Variables but cannot be access outside the scope they are declared in.<br>
Be warned that if you create a `scoped` Variable and a `var` Variable in the same context the `var` will override the `scoped`!<br>
### Strict Variables
If you'd like to create a variable that has an explicitly assigned type and cannot have its type changed you can use the `strict` keyword!<br>
Strict Variables work the same as normal Variables, but you must assign a type to the variable during its declaration!<br>
You do this very simply: `strict type myStrictVar = 1`. The possible types are: `int, float, and string`.<br>
Strings are any variable which has non-numerical characters in it, Ints are numbers without any decimal values, and Floats are numbers with or without decimal values.<br>
Once you've created the variable you will not be able to re-assign it to a new type without changing the original declaration!<br>
Note that Strict Variables are currently not compatible with arrays, and they must always have a default value.

## Mathematical Operators
___
Math! Who doesn't love math?<br>
Like any good language, PeanutScript comes with all the basic mathematical operators you need.
- \+ : The plus operator. Simply use `value + value` to add two values together! This also works for more than two values.
- \- : The minus operator. Simply use `value - value` to subtract the first value by the second! This also works for more than two values.
- \* : The multiplication operator. Simply use `value * value` to multiply the first value by the second! This also works for more than two values.
- \ : The division operator. Simply use `value / value` to divide the first value by the second! This also works for more than two values.
- ^ : The exponentiation operator. Simply use `value ^ value` to raise the first value to the second! This also works for more than two values.
- % : The modulus operator. Simply use `value % value` to divide the first value by the second and return the remainder!
- () : Parentheses! These can be used for order of operations purposes. Simply use `(mathematical operation)` to run that particular operation before all others!

## Comparisons
____
PeanutScript uses a lot of slightly strange syntax for comparisons. Here's a quick explanation of them all!<br>
`=>` Can be used in place of `then`!<br>
- if : A simple if statement. Contains all of these Comparisons.<br>Syntax: `if COMPARISON then SOMETHING`
- elif : A special if statement that only runs after an if statement. `elif` can only be used after a `if` or an `elif` and in a Multi-Line statement.
- else : A default case for an if statement. The code in an `else` is only run if all prior `if` and `elif` statements return false.
- == : Checks if one Number or String equals another.<br>Syntax: `n == x`
- and : Checks if two different conditions are true. `and` can be chained multiple times!<br>Syntax: `COMPARISON and COMPARISON`
- or : Checks if one of two statements are true. `or` can be chained multiple times!<br>Syntax: `COMPARISON or COMPARISON`
- not : Checks if one statement is not true.<br>Syntax: `not SOMETHING`
- < : Checks if one value is less than another.<br>Syntax: `1 < 2`
- <= : Checks if one value is less than or equal to another.<br>Syntax: `1 <= 2`
- \> : Checks if one value is greater than another.<br>Syntax: `1 > 2`
- \>= : Checks if one value is greater than or equal to another.<br>Syntax: `1 >= 2`

## For and While loops
____
For and While loops are great things to have! They are very important to all programs, here's how to use them in PeanutScript!<br>
Remember to mark the end of all loops with an `end` line!

### While
While loops are very simple. <br>
Syntax: `while COMPARISON => SOMETHING` <br>
This will run until COMPARISON returns false! <br>

### For
For loops are slightly more complex. <br>
Syntax: `for i=n until x => SOMETHING`<br>
n is a value you choose for your For loop to start with.<br>
The loop will run SOMETHING until n reaches x, incrementing n by 1 each time.<br>

### Single and Multi-line notes
Remember that in all Multi-Line loops the `=>` is required to be on the first line of the loop!<br>
An `end` keyword is not required in Single-Line loops!

## Functions
____
Like all good languages, PeanutScript allows the user to create their own custom functions!<br>
Functions are declared like so: `function myFirstFunc()`!<br>
Everything on the following lines is part of the function; when you run the function all the code on those lines will be run!<br>
Remember to mark the end of a function with an `end` line! <br>
### Arguments 
Arguments can be passed into functions! <br>
For example: `function mySecondFunc(input)`<br>
This "input" variable has its value assigned when running the function: `mySecondFunc(96)`<br>
This "input" variable can be used within the scope of the function!<br>
Remember that all arguments put into a function are *required*. You cannot run the function without all its arguments!<br>
You can also assign default values to arguments! For example: `function myThirdFunc(input=96)`<br>
### Single-Line Functions
Single-Line functions have a *very slightly* different syntax.<br>
After the name of the function you must have a `=>` before the function code.<br>
Single-Line functions also do not require an `end` keyword.<br>

## Using Other Files
____
As of v1.1 PeanutScript has official support for using multiple files!<br>
Simply use the `use()` Built-In and pass in your file! An example of this can be seen in the `example` file.<br>
Be aware that the `use()` function doesn't just access the file you pass in, it runs it too!<br>

## Ending Notes
____
Thank you for taking the time to read this! If you have any questions about the syntax be sure to message me on Discord, my tag is Flamemaster#9696 :)<br>
Also, be sure to check out the [Examples](EXAMPLES.md)!
