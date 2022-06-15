#!/bin/python3
import peanut

VERSION_NUM = '1.2.8'

print(f"[34mYou're running PeanutScript [96mv{VERSION_NUM}[0m")
print("[34mBe sure to check [94mhttps://github.com/FlamemasterNXF/PeanutScript[34m for updates![0m")
while True:
    text = input('[92mInput >[0m ')
    if text.strip() == "": continue
    result, error = peanut.run(peanut.FILE_NAME, text)

    if error: print(error.as_string())
    elif result:
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))
