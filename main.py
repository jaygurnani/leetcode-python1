from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = [False] * len(candies)
        largestValue = 0
        for index, value in enumerate(candies):
            if value > largestValue:
                largestValue = value

        for index, value in enumerate(candies):
            if value + extraCandies >= largestValue:
                result[index] = True

        return result

    def KidWithCandiesLeetCode(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Find out the greatest number of candies among all the kids.
        maxCandies = max(candies)
        # For each kid, check if they will have greatest number of candies
        # among all the kids.
        result = []
        for i in range(len(candies)):
            result.append(candies[i] + extraCandies >= maxCandies)
        return result

def main():
    sol = Solution()
    result = sol.KidWithCandiesLeetCode([1,2,3], 1)
    print(result)

main()