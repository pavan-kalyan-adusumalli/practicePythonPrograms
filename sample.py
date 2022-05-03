# 26) Write a program that reads a list of temperatures from a file called temps.txt, converts
# those temperatures to Fahrenheit, and writes the results to a file called ftemps.txt.
f = open("sample.txt", 'r')
res = ''
for mail in f.readlines():
    if(mail[-1].isalpha()):
        res += mail
    else:
        res += mail[:-1]+":"
print(res)
f.close()
