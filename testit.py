import shared as sh

sh.afunction()

sh.clean_string("this is it")

try:
    sh.clean_string(2)
except Exception as e:
    print(e)
