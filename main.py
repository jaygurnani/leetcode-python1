import collections
import heapq
from typing import List, Collection, Set, Optional, Dict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

    def longestSubarray(self, nums: List[int]) -> int:
        left, right = 0, 0
        k = 1
        for right in range (0, len(nums)):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1

        return right - left

    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        n = len(grid)

        row_counter = collections.Counter(tuple(row) for row in grid)

        for c in range(n):
            col = [grid[i][c] for i in range (n)]
            count = count + row_counter[tuple(col)]

        return count

    def customSortString(self, order: str, s: str) -> str:
        result = ""
        dictionary = {}
        for char in s:
            dictionary[char] = dictionary.get(char, 0) + 1

        for char in order:
            if char in dictionary:
                result = result + (char * dictionary[char])
                dictionary.pop(char)
        for char, count in dictionary.items():
            result = result + (char * count)

        return result

    def traverseTreeVertical(self, root: TreeNode, column, level, dic):
        if not root:
            return
        dic[column].append((root.val, level))
        self.traverseTreeVertical(root.left, column -1, level +1, dic)
        self.traverseTreeVertical(root.right, column +1, level + 1, dic)

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dict = collections.defaultdict(list)
        self.traverseTreeVertical(root, 0, 0, dict)
        result = []
        for i in sorted(dict.keys()):
            temp = []
            for j in sorted(dict[i]):
                temp.append(j[1])
            result.append(temp)

        return result

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return [""]
        phone_map = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        output = []
        self.backtrack("", digits, phone_map, output)

        return output

    def backtrack(self, combination: str, nextDigits: str, phone_map: List[str], output: List[str]):
        if not nextDigits:
            output.append(combination)
        else:
            check = nextDigits[0]
            item = phone_map[ord(check) - ord('2')]
            for letter in item:
                self.backtrack(combination + letter, nextDigits[1::], phone_map, output)

    def right_align_text_with_splitting(self, max_width: int, words: List[str]) -> List[str]:
        lines: List[str] = []
        current_line = ""

        for word in words:
            while word:
                # if the current line is empty, try and fit it
                if not current_line:
                    if len(word) <= max_width:
                        current_line = word
                        word = ""
                    else:
                        # split it to find the max it can fit
                        lines.append(word[:max_width].rjust(max_width))
                        word = word[max_width:]
                else:
                    if len(current_line) + 1 + len(word) <= max_width:
                        current_line += " " + word
                        word = ""
                    else:
                        lines.append(current_line.rjust(max_width))
                        current_line = ""

        if current_line:
            lines.append(current_line.rjust(max_width))

        return lines

    def sum_of_interval_products(self, arr):
        MOD = 10 ** 9 + 7
        n = len(arr)
        total_sum = 0

        # Iterate over all possible starting points
        for i in range(n):
            product = 1
            for j in range(i, n):
                # Calculate the product for the current interval
                product = (product * arr[j]) % MOD
                # Add this product to the total sum
                total_sum = (total_sum + product) % MOD

        return total_sum


class SmallestInfiniteSet:
    def __init__(self):
        self.pq = []
        self.seen = set()
        self.min_num = 1

    def popSmallest(self) -> int:
        if self.pq:
            num = heapq.heappop(self.pq)
            self.seen.remove(num)
            return num
        self.min_num += 1
        return self.min_num - 1

    def addBack(self, num: int) -> None:
        if self.min_num > num and num not in self.seen:
            self.seen.add(num)
            heapq.heappush(self.pq, num)

def main():
    sol = Solution()
    sol1 = SmallestInfiniteSet()

    #result = sol.KidWithCandiesLeetCode([1,2,3], 1)
    #result = sol.maxVowels("abciiidef", 3)
    #result = sol.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)
    #result = sol.longestSubarray([0,1,1,1,0,1,1,0,1])
    #result = sol.equalPairs([[3,2,1],[1,7,6],[2,7,7]])
    #result = sol.customSortString("cba", "abcd")
    #result = sol.letterCombinations("23")
    #result = sol1.popSmallest()
    #result = sol.right_align_text_with_splitting(20, ["HackerRank123456789101112131415", "is", "a", "great", "place", "to", "learn", "coding", "and", "it", "provides", "many", "challenging", "problems."])
    result = sol.sum_of_interval_products([1,2,3])

    print(result)

main()