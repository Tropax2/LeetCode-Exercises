class Solution:
    def romanToInt(self, number):
        chars = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        for i in range(len(number)):
            if i + 1 < len(number) and chars[number[i]] < chars[number[i + 1]]:
                total -= chars[number[i]]

            else:
                total += chars[number[i]]
        return total
 