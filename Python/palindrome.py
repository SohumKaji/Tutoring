def Palindrome(x):
	return list(x) == list(x)[::-1]

answer = []

for x in range(100000, 1000000): 				#For every 6 digit whole number, each instance called x
	if(Palindrome(str(x)[:-5:-1])): 			#if the last 4 digits of x are a palindrome
		if(Palindrome(str(x+1)[:-6:-1])): 		#if the last 5 digits of the next whole number are a palindrome
			if(Palindrome(str(x+2)[-2:-6:-1])): 	#if the 4 middle digits of the next whole number are a Palindrome
				if(Palindrome(str(x+3))): 	#if all 6 digits of the next whole number are a Palindrome
					answer.append(str(x))	#Then x is an answer to the problem

print "The possible values are: ", ', '.join(answer)
	