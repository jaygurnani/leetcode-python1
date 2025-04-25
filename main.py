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

    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}

        # first k letters
        count = 0
        for i in range(k):
            count = count + int(s[i] in vowels)
        answer = count

        # go through the rest - start at k, end at len(s)
        for i in range(k, len(s)):
            count = count + int(s[i] in vowels)
            count = count - int(s[i-k] in vowels)
            answer = max(answer, count)

        return answer

def main():
    sol = Solution()

    #result = sol.KidWithCandiesLeetCode([1,2,3], 1)
    result = sol.maxVowels("abciiidef", 3)

    print(result)

main()