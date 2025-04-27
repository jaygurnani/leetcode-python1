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

    def longestOnes1(self, nums: List[int], k: int) -> int:
        answer = 0
        for i in range(0, len(nums)):
            currentLongest = 0
            j = i
            m = k
            while j < len(nums):
                if nums[j] == 0:
                    if m > 0:
                        m-= 1
                        currentLongest += 1
                    else:
                        break
                if nums[j] == 1:
                    currentLongest += 1
                j += 1

            answer = max(currentLongest, answer)

        return answer

    def longestOnes2(self, nums: List[int], k: int) -> int:
        answer = 0

        # step 1, create longest 1 first
        endpoint = 0
        basket = []
        for i in range(0, len(nums)):
            if nums[i] == 1:
                endpoint += 1
                basket.append(nums[i])
            if nums[i] == 0:
                if k > 0:
                    k -= 1
                    endpoint += 1
                    basket.append(nums[i])
                if k == 0:
                    break

        answer = len(basket)
        # step 2, create list and check count of list

        i, j = 0, endpoint
        while j < len(nums):
            if nums[j] == 1:
                answer += 1
            if nums[j] == 0:
                i += 1

            j += 1
        return answer

    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0

        for right in range(0, len(nums)):
            if nums[right] == 0:
                k-=1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1

        return right - left +1

def main():
    sol = Solution()

    #result = sol.KidWithCandiesLeetCode([1,2,3], 1)
    #result = sol.maxVowels("abciiidef", 3)
    result = sol.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)

    print(result)

main()