# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 187-Repeated DNA Sequences.py
@time: 2020/9/3 9:49
@desc:
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T,
for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]
"""


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        L, n = 10, len(s)
        seen, result = set(), set()
        for start in range(n - L + 1):
            tmp = s[start: start + L]
            if tmp in seen:
                result.add(tmp)
            else:
                seen.add(tmp)
        return result

        """
        Rabin-Karp：使用旋转哈希实现常数时间窗口切片
    Rabin-Karp 算法用于多模式搜索，常用于重复检测和生物信息学中寻找两个或多个蛋白质的相似性。
    
    在文章最长的重复子串中详细实现了 Rabin-Karp 算法，在这里我们做一个基本的实现。
    
    其思想是对字符串进行切片并在滑动窗口中计算序列的哈希值，两者都是在一个常数的时间内进行的。
    
    可以发现窗口切片和计算散列都是在常数时间内完成的。
    
    算法：
    
    从序列初始位置遍历序列：从 1 到 N-1。
    如果 start==0，计算第一个序列 s[0:L] 的哈希值。
    否则，从上一个哈希值计算旋转哈希。
    如果哈希值在 hashset 中，则找到了重复的序列，则更新输出。
    否则，添加到将哈希值添加到 hashset 中。

        """

    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        L, n = 10, len(s)
        if n <= L:
            return []
        a = 4
        aL = pow(a, L)
        to_int = {"A": 0, "C": 1, "G": 2, "T": 3}
        nums = [to_int.get(s[i]) for i in range(n)]
        h = 0
        seen, result = set(), set()
        for start in range(n - L + 1):
            if start != 0:
                h = h * a - nums[start - 1] * aL + nums[start + L - 1]
            else:
                for i in range(L):
                    h = h * a + nums[i]
            if h in seen:
                result.add(s[start: start+L])
            else:
                seen.add(h)
        return list(result)
