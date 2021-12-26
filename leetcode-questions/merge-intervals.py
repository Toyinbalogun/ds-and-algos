# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

# Example 2:
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

def merge_intervals(intervals):
    intervals.sort()
    result = [intervals[0]] #[[1,3],...]

    for i in intervals[1:]: #[[2,6],[8,10],[15,18]]
        if result[-1][1] < i[0]:
            result.append(i)
        else:
           result[-1][1] = max(result[-1][1], i[1]) 
    return result

#TESTS  
intervals1 = [[1,3],[2,6],[8,10],[15,18]]
intervals2 = [[1,4],[4,5]]
intervals3 = [[1,4],[2,3]]

print(merge_intervals(intervals1))
print(merge_intervals(intervals2))
print(merge_intervals(intervals3))