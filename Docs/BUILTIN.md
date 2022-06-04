## Complete list of Built-ins
___
PeanutScript has quite a few Built-in functions!<br>
Here is a simple complete list of them all :)<br>
- print() : Good ol' print. Can take in a string or a number.
- printReturn() : Prints and returns a number or string.
- input() : Takes a string input from the user and returns it.
- inputNumber() : Takes a number input from the user and returns it.
- cls() : Clears the console.
- isNumber() : Takes in any input and returns if that input is a number.
- isString() : Takes in any input and returns if that input is a string.
- isArray() : Takes in any input and returns if that input is an array.
- isFunction() : Takes in any input and returns if that input is a function.
- typeof() : Takes in any input and returns that input's type.
- append() : Adds a value to an array. **May be broken, use `array + n` instead**
- removeIndex() : Removes a value from an array at a specified index. **May be broken, use `array - n` instead**
- concat() : Combines two or more arrays into one. **May be broken, use `array * array` instead**
- length() : Takes in an Array or String and returns the length.
- break : Force exits a loop.
- continue : Skips an iteration of a loop.
- return() : Returns a value. Can be a string or a number.
- time() : Returns the current Unix Timestamp.
- b64Encode() : Takes in a string and returns a Base64 Encoded version of that string.
- b64Decode() : Takes in a string and returns a Base64 Decoded version of that string.
- toUnicode() : Takes in a number and returns the Unicode character associated with it.
- fromUnicode() : Takes in a Unicode character and returns the number associated with it.
- run() : Takes in a string and runs the PeanutScript file with the same name.
- use() : Takes in a string and allows the file it is used in to access the PeanutScript file with the same name. Also runs that file.

### Built-in Values
- TRUE_VALUE : returns 1
- FALSE_VALUE : returns 0
- INFINITY : returns `inf`
- NEGATIVE_INF : returns `-inf`
