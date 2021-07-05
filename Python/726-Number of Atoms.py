# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 726-Number of Atoms.py
@time: 2021/7/5 9:33
@desc:
Given a chemical formula (given as a string), return the count of each atom.

The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.

Two formulas concatenated together to produce another formula. For example, H2O2He3Mg4 is also a formula.

A formula placed in parentheses, and a count (optionally added) is also a formula. For example, (H2O2) and (H2O2)3 are formulas.

Given a formula, return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.





Example 1:

Input: formula = "H2O"
Output: "H2O"
Explanation: The count of elements are {'H': 2, 'O': 1}.
Example 2:

Input: formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation: The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
Example 3:

Input: formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
Explanation: The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
Example 4:

Input: formula = "Be32"
Output: "Be32"


Constraints:

1 <= formula.length <= 1000
formula consists of English letters, digits, '(', and ')'.
formula is always valid.
"""


class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        i = 0
        n = len(formula)
        element_info = list()  # list of [element_name, number_of_element, number_of_parentheses]
        parentheses_stack = list()
        # atom = str()
        distribution = dict()
        while i < n:
            # 如果遇到的是字母
            # 如果遇到的是大写字母
            atom = str()
            if formula[i].isupper():
                atom = formula[i]
                i += 1
            # 跟着小写字母
            while i < n and formula[i].islower():
                atom += formula[i]
                i += 1
            cnt = str()
            # 如果后面有数
            if i < n and formula[i].isdigit():
                # 遍历所有的数
                while i < n and formula[i].isdigit():
                    cnt += formula[i]
                    i += 1
                element_info.append([atom, int(cnt), len(parentheses_stack)])
            # 如果后面没有数
            else:
                # 如果前面的if都执行过（即得到了某一个atom，而不是一开始就从(开头）
                # print("i, atom:", i, atom)
                if len(atom) and len(cnt) == 0:
                    element_info.append([atom, 1, len(parentheses_stack)])
                if i < n and formula[i] == '(':
                    parentheses_stack.append('(')
                    i += 1
                elif i < n and formula[i] == ')':
                    i += 1
                    cnt = str()
                    if i < n and formula[i].isdigit():
                        # 遍历所有的数
                        while i < n and formula[i].isdigit():
                            cnt += formula[i]
                            i += 1
                        cnt = int(cnt)
                    else:
                        cnt = 1
                    # parentheses_stack.pop()
                    for k in range(len(element_info) - 1, -1, -1):
                        if element_info[k][2] == len(parentheses_stack):
                            element_info[k][1] *= cnt
                            element_info[k][2] -= 1
                        else:
                            break
                    parentheses_stack.pop()

        # print(element_info)
        for ele in element_info:
            if ele[0] in distribution:
                distribution[ele[0]] += ele[1]
            else:
                distribution[ele[0]] = ele[1]

        # print(distribution)
        lst = sorted(distribution.items(), key=lambda obj: obj[0])
        # print(lst)
        ans = str()
        for name, number in lst:
            if number == 1:
                ans += name
            else:
                ans += name + str(number)
        return ans

