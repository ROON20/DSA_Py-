class Solution:
    def maxSubarraySum(self, arr):
        # Initialize current max and global max to the first element
        max_ending_here = arr[0]
        max_so_far = arr[0]
        
        # Traverse from the second element
        for i in range(1, len(arr)):
            # Update max_ending_here to either current element or extend the previous subarray
            max_ending_here = max(arr[i], max_ending_here + arr[i])
            # Update overall max
            max_so_far = max(max_so_far, max_ending_here)
        
        return max_so_far
