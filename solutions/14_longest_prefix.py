# find the least common prefix in a list of string
#
# https://leetcode.com/problems/longest-common-prefix/description/

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        min_str = min([len(s) for s in strs])

        lcp = ""
        for i in range(min_str):
            candidate = strs[0][i]
            lcp_found = False

            for s in strs:
                if s[i] != candidate:
                    lcp_found = True
                    break

            if lcp_found:
                break

            lcp += candidate
        return lcp


tests = [
    ["flower", "flow", "flight"],
    ["dog", "racecar", "car"],
]


def main():
    solution = Solution()

    for test in tests:
        lcp = solution.longestCommonPrefix(test)
        print(f"{test} = {lcp}")


if __name__ == "__main__":
    main()
