class Solution:
	def myAtoi(self, s: str) -> int:
		neg_flag = False
		sign_tracker_flag = False 
		digit_tracker_flag = False
		list_of_numbers = []
		list_of_100s = []
		for i in s:

			# means that the first character is " "
			if (i == " ") and (sign_tracker_flag == False) and (digit_tracker_flag == False):
				continue

			elif (i ==' ') and (sign_tracker_flag == True) and (digit_tracker_flag == False):
				return 0

			elif (i ==' ') and (sign_tracker_flag == True) and (digit_tracker_flag == True):
				break
				
			elif (i ==' ') and (digit_tracker_flag == True):
				break

			# This sets the sign tracker flag
			elif (i in ["+","-"]) and (sign_tracker_flag == False):
				sign_tracker_flag = True

				if i == '-':
					neg_flag = True
					
			elif (i in ["+","-"]) and (digit_tracker_flag == False) and (sign_tracker_flag == True):
				return 0

			elif (i in ["+","-"]) and (digit_tracker_flag == True): # and (sign_tracker == True):
				break
			 
			elif (i.isdigit()) and (sign_tracker_flag == False) and (digit_tracker_flag == False):
				sign_tracker_flag = True
				digit_tracker_flag = True
				list_of_numbers.append(i)
				list_of_100s.append(10**len(list_of_100s))
				
			elif (i.isdigit()) and (sign_tracker_flag == True) and (digit_tracker_flag == False):
				digit_tracker_flag = True
				list_of_numbers.append(i)
				list_of_100s.append(10**len(list_of_100s))

			elif (i.isdigit()) and (sign_tracker_flag == True) and (digit_tracker_flag == True):
				list_of_numbers.append(i)
				list_of_100s.append(10**len(list_of_100s))

			elif i == '.' and (digit_tracker_flag == False):
				return 0

			elif i == '.' and (digit_tracker_flag == True):
				break
			
			elif (i.isalpha()) and (digit_tracker_flag==True):
				break
			elif (i.isalpha()) and (digit_tracker_flag==False):
				return 0
			
		list_of_100s.reverse()
		main_number = 0
		
		for i,j in zip(list_of_numbers,list_of_100s):
			main_number = main_number + int(i)*j
		
		if neg_flag:
			main_number = main_number * -1
		
		print(main_number)
		
		if main_number < -2**31:
			return -2**31
		elif main_number > 2**31 -1:
			return 2**31-1
		else:
			return main_number