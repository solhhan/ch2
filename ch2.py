# Sort lexicographically using a simple in-place quicksort
# Average time complexity: O(nlog(n)); worse case: O(n^2)
# If we anticipate that inputted words are generally short and inputs contain many words,
# consider using radix sort instead for O(wn) time.
def sortLexicographically(seq, order):
	# Sort using a quicksort algorithm
	quickSort(seq, 0, len(seq)-1, order)

def quickSort(seq, low, high, order):
	# Finished sorting this section
	if (low >= high):
		return

	# Choose pivot and sort the two resulting subarrays
	pivot = partition(seq, low, high, order)
	quickSort(seq, low, pivot, order)
	quickSort(seq, pivot+1, high, order)

def partition(seq, low, high, order):
	# Use Hoare partition scheme to partition seq and return new pivot
	pivot = seq[low]
	i = low - 1
	j = high + 1
	while (True):
		jAfterPivot = True
		while (jAfterPivot):
			j = j - 1
			jAfterPivot = compareWords(seq[j], pivot, order) > 0
		iBeforePivot = True
		while (iBeforePivot):
			i = i + 1
			iBeforePivot = compareWords(seq[i], pivot, order) < 0
		if i < j:
			temp = seq[i]
			seq[i] = seq[j]
			seq[j] = temp
		else:
			return j

# Compare two strings, %str1 and %str2, based on %order
# Return -1 if obj1 precedes obj2
# Return 0 if obj1 == obj2
# Return 1 if obj1 follows obj2
def compareWords(str1, str2, order):
	str1_len = len(str1)
	str2_len = len(str2)
	shorter_len = min(str1_len, str2_len)

	# Compare str1 and str2, character by character
	for i in range(shorter_len):
		ind1 = order.index(str1[i])
		ind2 = order.index(str2[i])
		if (ind1 < ind2):
			return -1
		elif (ind1 > ind2):
			return 1

	# If one of the strings is a substring of the other, compare their lengths
	if (str1_len < str2_len):
		return -1
	elif (str1_len == str2_len):
		return 0
	else: # if (str1_len > str2_len):
		return 1

