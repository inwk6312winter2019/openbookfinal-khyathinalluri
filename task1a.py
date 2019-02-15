import string
def de_punctuation(line):
    for e in string.punctuation:
             if e in line:
                  line=line.replace(e," ")                  
    return line

def opening_file(myfile):
   c=0
   l1=[]
   for line in myfile:
       line=line.strip(string.whitespace+string.punctuation)
       line=de_punctuation(line)
       for word in line.split():
           l1.append(word.lower())
   return l1


myfile=open("Book1.txt")
res=opening_file(myfile)
print(res)
myfile1=open("Book2.txt")
res1=opening_file(myfile1)
print(res1)
myfile2=open("Book3.txt")
res2=opening_file(myfile2)
print(res2)

