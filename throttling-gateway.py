from typing import List
def droppedRequest(requestTime: List[int]) -> int:
	# There is a way of tracking requests with duplicate violations
	# using a hashmap (O(1) access time). But this has a O(n) space complexity.
	count = 0
	for i in range(len(requestTime)):
		# The count method here is mutually exclusive 
		# -> once current request is dropped by one of the 3 violations,
		# the other condition checks for count increases can be skipped.
		if (i >= 3) and (requestTime[i] - requestTime[i - 3] < 1):
			count += 1
			print(f"Request {requestTime[i]} - Dropped. At most 3 requests are allowed in one second.")
		elif (i >= 20) and (requestTime[i] - requestTime[i - 20] < 10):
			count += 1
			print(f"Request {requestTime[i]} - Dropped. At most 20 requests are allowed in 10 second.")
		elif (i >= 60) and (requestTime[i] - requestTime[i - 60] < 60):
			count += 1
			print(f"Request {requestTime[i]} - Dropped. At most 60 requests are allowed in 1 minute.")
		else:
			print(f"Request {requestTime[i]} - Not Dropped.")
	print(f"Total of {count} request(s) are dropped.")
	return count

if __name__ == "__main__":
	requestTime = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 11, 11, 11, 11]
	droppedRequest(requestTime)
