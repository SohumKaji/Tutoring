def check(num):
    split = list(str(num))									#split the current integer into a list of digits
    if(len(set(split)) == len(split)): return True						#if there are no repeat digits return True
    return False										#Otherwise return false

start = "0"
while(len(start) !=9 or not check(start)): 							#Take a valid input
	start = raw_input("Enter a 9 digit number where no digit appears twice: ") 		

finish = int(start) + 1										#Set finish to the next highest integer after the input
unused = [str(elem) for elem in range(0,10) if str(elem) not in list(start)].pop()		#Set Unused to the 1 digit from 0-9 inclusive that is not used

while((not check(finish) or unused in str(finish)) and len(str(finish)) == 9): 			#if finish is start rearranged, we have our answer otherwise,
	finish += 1										#take a look at the next integer. Stop if we exhaust 9 digit ints.
	
if(len(str(finish)) == 9): 									#Output
	print "The next highest number created by rearranging", start, "is:", finish
else: print "No Answer"