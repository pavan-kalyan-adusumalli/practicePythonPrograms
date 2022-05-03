# 26) Write a program that reads a list of temperatures from a file called temps.txt, converts
# those temperatures to Fahrenheit, and writes the results to a file called ftemps.txt
f = open("temps.txt", "r")
fh = list()
for temp in f.readlines():
    fh.append(int(temp[:-1]) * 1.8 + 32)
f.close()

f2 = open("ftemps.txt", "a")
for temp in fh:
    f2.write(str(temp)+"\n")
f2.close()

#n*1.8 + 32
