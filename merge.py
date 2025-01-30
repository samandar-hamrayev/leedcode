from importlib.metadata import pass_none


def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key = lambda nums: nums[0])
    merged = []
    previous = intervals[0]
    for interval in intervals[1:]:
        if previous[1] >= interval[0]:
            previous[1] = max(previous[1], interval[1])
        else:
            merged.append(previous)
            previous = interval
    merged.append(previous)
    return merged




print(merge([[1,3],[2,6],[8,10],[15,18]]))
