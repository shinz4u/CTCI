class Solution:
    known_palindromes = {}

    def longest_palindrome(self, s: str) -> str:

        s_len = len(s)

        longest_palindrome = ""
        counter = 1
        i = 0
        j = counter
        while (j - i) <= s_len:
            while j <= s_len:
                # print("Going to check {string}".format(string = s[i:j]))
                if self.check_palindrome(s[i:j]):
                    # print("This is palindrome {string}\n".format(string = s[i:j]))
                    if len(longest_palindrome) < len(s[i:j]):
                        longest_palindrome = s[i:j]
                i += 1
                j += 1
            counter += 1
            i = 0
            j = counter

        # print(self.known_palindromes)
        return longest_palindrome

    def check_palindrome(self, sub_string):
        """
        Checks whther the passed string is a palindrome
        return True otherwise False
        """
        if len(sub_string) == 0 or len(sub_string) == 1:
            self.known_palindromes[sub_string] = True
            return True

        if len(sub_string) == 2:
            if sub_string[0] == sub_string[1]:
                self.known_palindromes[sub_string] = True
                return True
            else:
                return False

        # 3 and 4
        to_check = sub_string[1:-1]
        if sub_string[0] == sub_string[-1]:
            if to_check in self.known_palindromes:
                self.known_palindromes[sub_string] = True
                return True
        return False

    def longest_palindrome_checkaround(self, s: str) -> str:
        """ Not Dynamic programming if using this function call"""
        if s is None or len(s) <= 1:
            return s
        end = 0
        start = 0
        length_of_string = len(s)
        i = 0
        for i in range(length_of_string):
            right1, left1 = self.check_around(s, i, i)
            right2, left2 = self.check_around(s, i, i + 1)
            if (right2 - left2) >= (right1 - left1):
                if (right2 - left2) > (end - start):
                    start = left2
                    end = right2
            else:
                if (right1 - left1) > (end - start):
                    start = left1
                    end = right1
        return s[start:end + 1]

    def check_around(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left = left - 1
            right = right + 1
        return right-1, left+1
        # return right - left

Solution = Solution()
print("1", Solution.longest_palindrome_checkaround("babad"))
print("2", Solution.longest_palindrome_checkaround("dadmalayalamdac"))
print("3", Solution.longest_palindrome_checkaround(""))
print("4", Solution.longest_palindrome_checkaround("ff"))
print("5", Solution.longest_palindrome_checkaround("fold"))
print("6", Solution.longest_palindrome_checkaround("qwertyuihfdsasdfgh"))
print("7", Solution.longest_palindrome_checkaround("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))


