###################################################################################################
#                                            24 Solver                                            #
#-------------------------------------------------------------------------------------------------#
# Given 4 digits, searching the solution space for values that calculate to 24 using only +,-,*,/ #
###################################################################################################

							#Python doesn't support tail-call 
from copy import copy					# optimization. So these types of problems 
import sys						# would be better solved with iteration.
 							# Ignoring that fact, we can increase the 					
sys.setrecursionlimit(1500)				# maximum depth recursion limit so that the 
							# optimization is not an issue for our needs



def recursive_calc(nums, operations = "333", nums_list = [], oper_list = []):						#Recursively check all digit & operations 
	solution_list = []												# orders/combinations

	if(is24(nums, operations) and operations not in oper_list): 							#Check if the current configuration
		solution_list.append([copy(nums), copy(operations)])							# yields 24, if so save the configuration
		oper_list.append(copy(operations))									

	if(int(operations) != 0):											#if we aren't at the last operator
		operations = str(int(operations)-1)									# configuration, move to the next one
		operations = ''.join([str(elem) if int(elem) <= 3 and int(elem)>=0   else '3' for elem in operations])
		if(len(operations) == 2): operations = '0'+operations
		if(len(operations) == 1): operations = '00'+operations
	else:														#if we are at the last operator
		operations = "333"											# configuration, reset the configuration
		nums = shuffle(nums, nums_list)										# counter and shuffle the number order
	
	if(nums not in nums_list): 											#As long as this isn't a repeated number 			
		nums_list.append(copy(nums))										# order check through all combinations for 24
		return solution_list + recursive_calc(nums, operations, nums_list, oper_list)

	elif(operations != "333"):											#If this is a repeated number, as long as  
		return solution_list + recursive_calc(nums, operations, nums_list, oper_list)				# this is a continued series of operations
															# configuration keep searching for solutions

	return solution_list												#This branch is exhausted, return

def is24(nums, operations):												 
	ans = float(nums[0]) 
	operations = list(operations)											
	
	for elem, oper in zip(nums[1:], operations):			#Check if this particular ordering of the
		if(oper == '3'): ans += float(elem)			# input with this particular ordering of the
		elif(oper == '2'): ans -= float(elem)			# operators, yields 24
		elif(oper == '1'): ans *= float(elem)
		elif(oper == '0'): 
			if(elem != 0): ans /= float(elem)
			else: ans = -100
	
	return ans == 24

def shuffle(nums, nums_list):						#Shuffle the input numbers
	iter = len(nums_list) % 6
									#This follows the pattern:
	if(iter == 0): nums[0], nums[3] = nums[3], nums[0]		# 1, 2, 3, 4
	if(iter == 1): nums[2], nums[3] = nums[3], nums[2]		# 1, 2, 4, 3
	if(iter == 2): nums[1], nums[3] = nums[3], nums[1]		# 1, 3, 4, 2
	if(iter == 3): nums[2], nums[3] = nums[3], nums[2]		# 1, 3, 2, 4
	if(iter == 4): nums[1], nums[3] = nums[3], nums[1]		# 1, 4, 2, 3
	if(iter == 5): nums[2], nums[3] = nums[3], nums[2]		# 1, 4, 3, 2
									#Exhausting all combinations of 1 first
									#The first if will now put 2 first
	return nums

###########
#24 Solver#
###########

answers = []; no_ans = []; total = 0; ans_string = ''
nums = ''

while(len(nums) !=4 or not nums.isdigit()): 						#Check input
	nums = raw_input("Enter 4 numbers to calculate 24 from (Eg. 1234): ")		#Take input
nums = [int(elem) for elem in nums]

answers = recursive_calc(nums)								#Find Answers

for e in answers:									#Format and print Solutions
	ans_string ='((('+str(e[0][0])
	for i, ii in zip(e[0][1:], e[1]):
		if(ii == '3'): ans_string += '+'
		if(ii == '2'): ans_string += '-'
		if(ii == '1'): ans_string += '*'
		if(ii == '0'): ans_string += '/'
		ans_string += str(i) +')'

	print ans_string + ' = 24'

if( answers == []): print "\nSorry, no solutions! :-(\n"				#If there are no Solutions
