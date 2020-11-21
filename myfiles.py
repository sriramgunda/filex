from filex import filex

files = ['one.txt', 'two.java', 'three.cs']
for fl in files:
    file_details = filex(fl)
    for x,y in file_details.items():
        print(x + " : " + y)