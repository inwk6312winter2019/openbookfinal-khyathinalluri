import string
l1=[]
def de_punctuation(line):
    for e in string.punctuation:
             if e in line:
                  line=line.replace(e," ")                  
    return line

myfile=open("access.log")
for line in myfile:
    line=line.strip(string.whitespace+string.punctuation)
    line=de_punctuation(line)
    for word in line.split():
        l1.append(word.lower())

print(l1)
