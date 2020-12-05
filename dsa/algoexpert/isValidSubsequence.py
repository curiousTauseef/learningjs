"""
Question find if the sequence of array integers is present in the main array. 
It is expected to be present in the same order
array  = [5,1,22,25,6,-1,8,10]
sequence = [1,6,-1,10]
my first attempt isValidSubsequence1 worked only for 16/23 cases, as it didn't work for when the sequence had duplicates. 
the isValidSubsequence2 and isValidSubsequence3 are better approaches because we are 
a) reducing the time complexity, 
b) the length of the sequence is used to determine whether or not we had all of our sequence elements found.
c) the space is also less, there is no need to store the variables to move forward in the first array once we found a match

"""
def isValidSubsequence2(array, sequence):
    # Write your code here.
	seq_i = 0
	arr_i = 0
	while arr_i < len(array) and seq_i < len(sequence):
		if array[arr_i] == sequence[seq_i]:
			seq_i += 1
		arr_i += 1
	return seq_i == len(sequence)


def isValidSubsequence3(array, sequence):
    s_i = 0
	for i in array:
		if s_i == len(sequence):
			break;
		if sequence[s_i] == i:
			s_i += 1
	return s_i == len(sequence)

def isValidSubsequence1(array, sequence):
    # Write your code here.
	result = []
	for i in sequence: #[1,6,-1,10] [1,1,1]
		for j in array: #[5,1,22,25,6,-1,8,10][1,1,1,1,1]
			print('inside second', i, j)
			if i  == j:
				print(i, j, 'if equal')
				# if j not in result:
				result.append(j)
				continue	
	print(result, sequence, result == sequence)
	if result == sequence:
		return True
	return False