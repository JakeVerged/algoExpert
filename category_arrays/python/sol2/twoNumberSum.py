def twoNumberSum(array, targetSum):
    # Write your code here.
	nums={}
	for num in array:
		potentialMatch = targetSum -num
		if potentialMatch in nums:
			return [potentialMatch, num]
		else:
			nums[num]=True
	return []
    
