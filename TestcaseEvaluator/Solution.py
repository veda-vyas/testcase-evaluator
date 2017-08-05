sentence = raw_input()
n = int(raw_input())
a=n
res=""
if n==0:
	res = sentence[a]
else:
	for i in range(0,len(sentence)):
		if(a<len(sentence)):
			# print sentence[a]
			res=res+sentence[a]
		a=a+n
print(res)
