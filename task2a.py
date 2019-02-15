import string
def de_punctuation(line):
    for e in string.punctuation:
             if e in line:
                  line=line.replace(e," ")                  
    return line

#function to find top 20 common words
def common_words(l1,l2,l3):
	d={}
	for word in l1:
		if word in l2:
			if word in l3:
				if word not in d:
					d[word]=1
				else:
					d[word]+=1

	return d

# function to open files
def opening_file(myfile):
   c=0
   l1=[]
   for line in myfile:
       line=line.strip(string.whitespace+string.punctuation)
       line=de_punctuation(line)
       for word in line.split():
           l1.append(word.lower())
   return l1


#opening files

myfile=open("Book1.txt")
res=opening_file(myfile)
myfile1=open("Book2.txt")
res1=opening_file(myfile1)
myfile2=open("Book3.txt")
res2=opening_file(myfile2)
result=common_words(res,res1,res2)
#print(result)
sorted_d=sorted((value,key) for (key,value) in result.items())
for i in range(20):
	print(sorted_d[i])
