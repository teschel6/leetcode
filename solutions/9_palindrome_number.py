# Check if a number is a palindrome.
# No using string because that is lame
#
# https://leetcode.com/problems/palindrome-number/description/


class Solution:
    def countDigits(self, n: int) -> int:
        if n == 0:
            return 1

        count = 0

        while n != 0:
            n = n // 10
            count += 1

        return count

    def isPalindrome(self, n: int) -> bool:
        if n < 0:
            return False

        fwd = n  # forwards
        bwd = n  # backwards
        n_digits = self.countDigits(n)
        fwd_digits = n_digits

        while fwd_digits > n_digits // 2:
            bwd_digit = bwd % 10
            bwd = bwd // 10

            fwd_divisor = 10 ** (fwd_digits - 1)
            fwd_digit = fwd // fwd_divisor
            fwd_digits = fwd_digits - 1
            fwd = fwd % fwd_divisor

            if fwd_digit != bwd_digit:
                return False

        return True


test = [
    123,
    121,
    123321,
    123421,
    1221,
    10,
    101,
    -121,
]

solution = Solution()

for x in test:
    print(f"{x}\t: {solution.isPalindrome(x)}")
