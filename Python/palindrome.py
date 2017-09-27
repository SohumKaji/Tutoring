def Palindrome(x):
	return list(x) == list(x)[::-1]

answer = []

for x in range(100000, 1000000):
	if(Palindrome(str(x)[:-5:-1])):
		if(Palindrome(str(x+1)[:-6:-1])):
			if(Palindrome(str(x+2)[-2:-6:-1])):
				if(Palindrome(str(x+3))):
					answer.append(str(x))

print "The possible values are: ", ', '.join(answer)
	