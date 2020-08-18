file_name= 'news.txt'

file_ref=open(file_name,"r")

print(file_ref)
for f in file_ref:
    print(f)


f= open("greet","r")

f=f.read(100)
print(f)


file_first_line=f.readline()
print(file_first_line)


file_ref.close()