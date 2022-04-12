class Solution:
    def removeCoveredIntervals(self, intervals):
        # Brute Force
        # n^2
        intervals_to_be_removed_dict = {}
        for interval in intervals:
            for interval_temp in intervals:
                if interval != interval_temp:
                    if (interval[0] <= interval_temp[0]) and (interval[1] >= interval_temp[1]):
                        try:
                            intervals_to_be_removed_dict[tuple(interval)].extend([interval_temp])
                        
                        except:
                            intervals_to_be_removed_dict[tuple(interval)] = [interval_temp]

        all_consol = []
        
        for value in intervals_to_be_removed_dict.values():
            all_consol.extend(value)
        
        tbr = set(tuple(x) for x in all_consol)
        
        return len(intervals) - len(tbr)
        
        ############################################################
        # Optimal Solution
        # nlogn
        # This will sort the list of lists and put the second element first
        intervals.sort(key = lambda i: (i[0], -i[[1]]))

        result = [intervals[0]]

        for l, r in intervals[1:]:
            prevL, prevR = res[-1]

            if prevL <= l and prevR >= r:
                continue

            res.append([l,r])

            return len(res)


solution = Solution()
final_result = solution.removeCoveredIntervals([[34335,39239],[15875,91969],[29673,66453],[53548,69161],[40618,93111]])

print(final_result)