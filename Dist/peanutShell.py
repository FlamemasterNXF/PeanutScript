#!/bin/python3
import peanut

VERSION_NUM = '1.2.6'

print(f"You're Running PeanutScript v{VERSION_NUM}")
print("Be sure to check https://github.com/FlamemasterNXF/PeanutScript for updates!")
while True:
    text = input('input > ')
    if text.strip() == "": continue
    result, error = peanut.run('{fn}', text)

    if error: print(error.as_string())
    elif result:
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))
