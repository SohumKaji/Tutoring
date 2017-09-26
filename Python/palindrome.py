def Palindrome(x):
	x = str(x)
	for i in range(len(x)//2 - (len(x)//2)%2 + 1):
		if(x[i] != x[-i-1]): return False

	return True


y = raw_input("Enter a word, I'll check if it is a Palindrome: ")
print(Palindrome(y))
