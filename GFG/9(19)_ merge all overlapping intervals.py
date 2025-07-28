from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort the intervals based on the start time
        intervals.sort(key=lambda x: x[0])

        merged = []  # This will store the merged intervals

        for interval in intervals:
            # If merged is empty OR no overlap with the last interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)  # Add the interval as it is
            else:
                # Overlapping: merge the current interval with the last one
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged
