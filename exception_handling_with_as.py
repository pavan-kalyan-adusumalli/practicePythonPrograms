# 34) Write a program to demonstrate try/finally and with/as.
# using with statement
try:
    with open('xyz.txt', 'r') as file:
        print(file.read)
except FileNotFoundError:
    print("File specefied by you is not present at current location")
finally:
    print("end of program")
