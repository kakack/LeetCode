# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 406-Queue Reconstruction by Height.py
@time: 2020/11/16 10:13
@desc:
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.


Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

"""


class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # people.sort(key=lambda x: (x[0], -x[1]))
        # # print(people)
        # n = len(people)
        # ans = [[] for _ in range(n)]
        # for person in people:
        #     spaces = person[1] + 1
        #     for i in range(n):
        #         if not ans[i]:
        #             spaces -= 1
        #             if spaces == 0:
        #                 ans[i] = person
        #                 break
        # return ans

        if len(people) <= 1:
            return people

        people = sorted(people, key=lambda x: (-x[0], x[1]))
        new_people = [people[0]]  # 这个人是从前往后、从上往下看到的第一个人
        for i in people[1:]:
            new_people.insert(i[1], i)
        return new_people



if __name__ == '__main__':
    s = Solution()
    ipt = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    print(s.reconstructQueue(ipt))
