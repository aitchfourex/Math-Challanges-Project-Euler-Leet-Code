# SOLUTION TO:
# https://www.cemc.uwaterloo.ca/resources/potw/2019-20/English/POTWE-19-AE-CP-14-P.pdf

# create class to represent size of current set
class row_size:
	def __init__(self, x):
		self.size = x

class total_sum:
	def __init__(self, y):
		self.sum = y

# function that will calculate the solution
def solution(row_size_counter, sum_counter):
	# set some variables needed for function
	# total sum of current row
    tot_sum = sum_counter.sum
    # current integer (start at 2)
    integer = 2
    # flag for while loop
    flag = True

    # loop runs until flag is set to false, flag will be set to false once loop checks and sees that the integer 2020 exists in the current row
    while flag:
    	# list containing contents of current row
        array = []

        # appends current integer to the row then adds two to the integer
        for i in range(row_size_counter.size):
            array.append(integer)
            integer = integer + 2

        # print the contents of the current row
        print(array)
        # print the sum of the current row
        print(sum(array))

        # set sum_counter object to the current sum
        sum_counter.sum = sum(array)


        tot_sum = sum(array)

        # incease row size by 1
        row_size_counter.size = row_size_counter.size + 1
        
        # check to see if 2020 exists in current row
        if 2020 in array:
            flag = False
        else:
            pass

# initiate row_size and total_sum objects
row = row_size(1)
total = total_sum(0)

# call function to calculate
solution(row, total)
