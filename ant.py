import unittest
import re
def look_and_say_sequence(n):
    dp = {}
    dp[1] = '1'
    if n == 1:
        return dp[1]

    pattern = r'((\d)\2*)'

    for i in range(2, n+1):
        matches = re.findall(pattern, dp[i-1])
        dp[i] = ''.join(map(lambda x: str(len(x[0])) + x[1], matches))

    return int(dp[i][len(dp[i])//2-1:len(dp[i])//2+1])


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(look_and_say_sequence(5), 12)
        self.assertEqual(look_and_say_sequence(8), 21)

if __name__ == '__main__':
    unittest.main()