# readline() is used to read a file line ny line
f=open('myfile.txt')
while True:
    line=f.readline()
    m1=f.split(",")[0]
    m2=f.split(",")[1]
    m3=f.split(",")[2]
    if not  line:
      break

    print(line)