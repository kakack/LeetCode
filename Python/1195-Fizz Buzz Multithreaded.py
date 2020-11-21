# -*- coding: utf-8 -*
"""
@author: Kaka Chen
@license: (C) Copyright Personal Uncommercial Limited.
@contact: kakachen1990@gmail.com
@file: 1195-Fizz Buzz Multithreaded.py
@time: 2020/11/21 10:39 上午
@desc:
Write a program that outputs the string representation of numbers from 1 to n, however:

If the number is divisible by 3, output "fizz".
If the number is divisible by 5, output "buzz".
If the number is divisible by both 3 and 5, output "fizzbuzz".
For example, for n = 15, we output: 1, 2, fizz, 4, buzz, fizz, 7, 8, fizz, buzz, 11, fizz, 13, 14, fizzbuzz.

Suppose you are given the following code:

class FizzBuzz {
  public FizzBuzz(int n) { ... }               // constructor
  public void fizz(printFizz) { ... }          // only output "fizz"
  public void buzz(printBuzz) { ... }          // only output "buzz"
  public void fizzbuzz(printFizzBuzz) { ... }  // only output "fizzbuzz"
  public void number(printNumber) { ... }      // only output the numbers
}
Implement a multithreaded version of FizzBuzz with four threads. The same instance of FizzBuzz will be passed to four different threads:

Thread A will call fizz() to check for divisibility of 3 and outputs fizz.
Thread B will call buzz() to check for divisibility of 5 and outputs buzz.
Thread C will call fizzbuzz() to check for divisibility of 3 and 5 and outputs fizzbuzz.
Thread D will call number() which should only output the numbers.

"""


from threading import Lock

class FizzBuzz(object):
    def __init__(self, n):
        self.n = n
        self.both3and5 = Lock()
        self.either3 = Lock()
        self.either5 = Lock()
        self.num = Lock()

        self.both3and5.acquire()
        self.either3.acquire()
        self.either5.acquire()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz):
        """
        :type printFizz: method
        :rtype: void
        """
        for i in range(1, self.n + 1):
            if not i % 3 and i % 5:
                self.either3.acquire()
                printFizz()
                self.num.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz):
        """
        :type printBuzz: method
        :rtype: void
        """
        for i in range(1, self.n + 1):
            if i % 3 and not i % 5:
                self.either5.acquire()
                printBuzz()
                self.num.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz):
        """
        :type printFizzBuzz: method
        :rtype: void
        """
        for i in range(1, self.n + 1):
            if not i % 15:
                self.both3and5.acquire()
                printFizzBuzz()
                self.num.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1, self.n + 1):
            self.num.acquire()
            if not i % 15:
                self.both3and5.release()
            elif not i % 3:
                self.either3.release()
            elif not i % 5:
                self.either5.release()
            else:
                printNumber(i)
                self.num.release()



