def twoNumberSum(array, targetSum):
    # Write your code here.
	result = []
	for i in array: 
		print('numbers in the array and difference', i, targetSum - i)
		if i != targetSum - i:
			if present(targetSum - i, array):
				result.append(i)
				result.append(targetSum-i)
				print('result:', result)
	return list(set(result))
def present(number, array):
	print('inside present', number, array)
	for i in array:
		print(i)
		if i == number:
			print('found')
			return True
	return False
