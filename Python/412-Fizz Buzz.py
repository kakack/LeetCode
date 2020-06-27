# -*- coding: utf-8 -*
"""
@author: Kaka Chen
@license: (C) Copyright Personal Uncommercial Limited.
@contact: kakachen1990@gmail.com
@file: 412.-Fizz Buzz.py
@time: 2020/6/26 3:32 上午
@desc:
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

"""

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        for i in range(1, n + 1):
            if i % 3 != 0 and i % 5 != 0:
                ans.append(str(i))
            elif i % 15 == 0:
                ans.append("FizzBuzz")
            elif i % 3 == 0:
                ans.append("Fizz")
            else:
                ans.append('Buzz')
        return ans


if __name__ == '__main__':
    # s = Solution()
    # print(s.fizzBuzz(20))

    def foo():
        print("starting...")
        while True:
            res = yield 4
            print("res:", res)


    g = foo()
    print(next(g))
    print("*" * 20)
    print(next(g))
    print(g.send(7))