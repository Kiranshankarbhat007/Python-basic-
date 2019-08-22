s = []
n = int(input("enter the range :"))
for i in range (n):
	a = int(input("enter the numbers:"))
	s.append(a)

print (s)

for j in range (len(s)):
	for p in range (len(s)-1):
	# for p in range (j):
		if s[p]>=s[p+1]:
			# q = s[p]
			# s[p] = s[p+1]
			# s[p+1] = q
			s[p],s[p+1]=s[p+1],s[p]
			print s

print (s)


