# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 1269-Number of Ways to Stay in the Same Place After Some Steps.py
@time: 2021/5/13 10:02
@desc:

You have a pointer at index 0 in an array of size arrLen. At each step, you can move 1 position to the left, 1 position to the right in the array or stay in the same place  (The pointer should not be placed outside the array at any time).

Given two integers steps and arrLen, return the number of ways such that your pointer still at index 0 after exactly steps steps.

Since the answer may be too large, return it modulo 10^9 + 7.



Example 1:

Input: steps = 3, arrLen = 2
Output: 4
Explanation: There are 4 differents ways to stay at index 0 after 3 steps.
Right, Left, Stay
Stay, Right, Left
Right, Stay, Left
Stay, Stay, Stay
Example 2:

Input: steps = 2, arrLen = 4
Output: 2
Explanation: There are 2 differents ways to stay at index 0 after 2 steps
Right, Left
Stay, Stay
Example 3:

Input: steps = 4, arrLen = 2
Output: 8


Constraints:

1 <= steps <= 500
1 <= arrLen <= 10^6

"""


class Solution(object):
    def numWays(self, steps, arrLen):
        """
        :type steps: int
        :type arrLen: int
        :rtype: int
        """
        mod = 10 ** 9 + 7
        maxColumn = min(arrLen - 1, steps)
        dp = [0] * (maxColumn + 1)
        dp[0] = 1
        for i in range(1, steps + 1):
            dpNext = [0] * (maxColumn + 1)
            for j in range(0, maxColumn + 1):
                dpNext[j] = dp[j]
                if j - 1 >= 0:
                    dpNext[j] = (dpNext[j] + dp[j - 1]) % mod
                if j + 1 <= maxColumn:
                    dpNext[j] = (dpNext[j] + dp[j + 1]) % mod
            dp = dpNext
        return dp[0]


if __name__ == '__main__':
    nameList = ["crop_mix+L0-0",
                "crop_mix+L0-1",
                "crop_mix+L0-2",
                "crop_mix+L0-3",
                "crop_mix+L0-4",
                "crop_mix+L0-5",
                "crop_mix+L1-0",
                "crop_mix+L1-1",
                "crop_mix+L10-0",
                "crop_mix+L10-1",
                "crop_mix+L11-0",
                "crop_mix+L11-1",
                "crop_mix+L12-0",
                "crop_mix+L12-1",
                "crop_mix+L12-2",
                "crop_mix+L12-3",
                "crop_mix+L12-4",
                "crop_mix+L12-5",
                "crop_mix+L13-0",
                "crop_mix+L14-0",
                "crop_mix+L15-0",
                "crop_mix+L16-0",
                "crop_mix+L2-0",
                "crop_mix+L2-1",
                "crop_mix+L2-2",
                "crop_mix+L2-3",
                "crop_mix+L2-4",
                "crop_mix+L2-5",
                "crop_mix+L3-0",
                "crop_mix+L4-0",
                "crop_mix+L4-1",
                "crop_mix+L5-0",
                "crop_mix+L5-1",
                "crop_mix+L6-0",
                "crop_mix+L7-0",
                "crop_mix+L8-0",
                "crop_mix+L9-0",
                "image_datasets_od_bus_plate_samples+L0-0",
                "image_datasets_od_bus_plate_samples+L0-1",
                "image_datasets_od_bus_plate_samples+L0-2",
                "image_datasets_od_bus_plate_samples+L0-3",
                "image_datasets_od_bus_plate_samples+L0-4",
                "image_datasets_od_bus_plate_samples+L0-5",
                "image_datasets_od_bus_plate_samples+L1-0",
                "image_datasets_od_bus_plate_samples+L1-1",
                "image_datasets_od_bus_plate_samples+L10-0",
                "image_datasets_od_bus_plate_samples+L10-1",
                "image_datasets_od_bus_plate_samples+L11-0",
                "image_datasets_od_bus_plate_samples+L11-1",
                "image_datasets_od_bus_plate_samples+L12-0",
                "image_datasets_od_bus_plate_samples+L12-1",
                "image_datasets_od_bus_plate_samples+L12-2",
                "image_datasets_od_bus_plate_samples+L12-3",
                "image_datasets_od_bus_plate_samples+L12-4",
                "image_datasets_od_bus_plate_samples+L12-5",
                "image_datasets_od_bus_plate_samples+L13-0",
                "image_datasets_od_bus_plate_samples+L14-0",
                "image_datasets_od_bus_plate_samples+L15-0",
                "image_datasets_od_bus_plate_samples+L16-0",
                "image_datasets_od_bus_plate_samples+L2-0",
                "image_datasets_od_bus_plate_samples+L2-1",
                "image_datasets_od_bus_plate_samples+L2-2",
                "image_datasets_od_bus_plate_samples+L2-3",
                "image_datasets_od_bus_plate_samples+L2-4",
                "image_datasets_od_bus_plate_samples+L2-5",
                "image_datasets_od_bus_plate_samples+L3-0",
                "image_datasets_od_bus_plate_samples+L4-0",
                "image_datasets_od_bus_plate_samples+L4-1",
                "image_datasets_od_bus_plate_samples+L5-0",
                "image_datasets_od_bus_plate_samples+L5-1",
                "image_datasets_od_bus_plate_samples+L6-0",
                "image_datasets_od_bus_plate_samples+L7-0",
                "image_datasets_od_bus_plate_samples+L8-0",
                "image_datasets_od_bus_plate_samples+L9-0",
                "image_datasets_od_carface_samples+L0-0",
                "image_datasets_od_carface_samples+L0-1",
                "image_datasets_od_carface_samples+L0-2",
                "image_datasets_od_carface_samples+L0-3",
                "image_datasets_od_carface_samples+L0-4",
                "image_datasets_od_carface_samples+L0-5",
                "image_datasets_od_carface_samples+L1-0",
                "image_datasets_od_carface_samples+L1-1",
                "image_datasets_od_carface_samples+L10-0",
                "image_datasets_od_carface_samples+L10-1",
                "image_datasets_od_carface_samples+L11-0",
                "image_datasets_od_carface_samples+L11-1",
                "image_datasets_od_carface_samples+L12-0",
                "image_datasets_od_carface_samples+L12-1",
                "image_datasets_od_carface_samples+L12-2",
                "image_datasets_od_carface_samples+L12-3",
                "image_datasets_od_carface_samples+L12-4",
                "image_datasets_od_carface_samples+L12-5",
                "image_datasets_od_carface_samples+L13-0",
                "image_datasets_od_carface_samples+L14-0",
                "image_datasets_od_carface_samples+L15-0",
                "image_datasets_od_carface_samples+L16-0",
                "image_datasets_od_carface_samples+L2-0",
                "image_datasets_od_carface_samples+L2-1",
                "image_datasets_od_carface_samples+L2-2",
                "image_datasets_od_carface_samples+L2-3",
                "image_datasets_od_carface_samples+L2-4",
                "image_datasets_od_carface_samples+L2-5",
                "image_datasets_od_carface_samples+L3-0",
                "image_datasets_od_carface_samples+L4-0",
                "image_datasets_od_carface_samples+L4-1",
                "image_datasets_od_carface_samples+L5-0",
                "image_datasets_od_carface_samples+L5-1",
                "image_datasets_od_carface_samples+L6-0",
                "image_datasets_od_carface_samples+L7-0",
                "image_datasets_od_carface_samples+L8-0",
                "image_datasets_od_carface_samples+L9-0",
                "image_datasets_od_plate_samples_+L0-0",
                "image_datasets_od_plate_samples_+L0-1",
                "image_datasets_od_plate_samples_+L0-2",
                "image_datasets_od_plate_samples_+L0-3",
                "image_datasets_od_plate_samples_+L0-4",
                "image_datasets_od_plate_samples_+L0-5",
                "image_datasets_od_plate_samples_+L1-0",
                "image_datasets_od_plate_samples_+L1-1",
                "image_datasets_od_plate_samples_+L10-0",
                "image_datasets_od_plate_samples_+L10-1",
                "image_datasets_od_plate_samples_+L11-0",
                "image_datasets_od_plate_samples_+L11-1",
                "image_datasets_od_plate_samples_+L12-0",
                "image_datasets_od_plate_samples_+L12-1",
                "image_datasets_od_plate_samples_+L12-2",
                "image_datasets_od_plate_samples_+L12-3",
                "image_datasets_od_plate_samples_+L12-4",
                "image_datasets_od_plate_samples_+L12-5",
                "image_datasets_od_plate_samples_+L13-0",
                "image_datasets_od_plate_samples_+L14-0",
                "image_datasets_od_plate_samples_+L15-0",
                "image_datasets_od_plate_samples_+L16-0",
                "image_datasets_od_plate_samples_+L2-0",
                "image_datasets_od_plate_samples_+L2-1",
                "image_datasets_od_plate_samples_+L2-2",
                "image_datasets_od_plate_samples_+L2-3",
                "image_datasets_od_plate_samples_+L2-4",
                "image_datasets_od_plate_samples_+L2-5",
                "image_datasets_od_plate_samples_+L3-0",
                "image_datasets_od_plate_samples_+L4-0",
                "image_datasets_od_plate_samples_+L4-1",
                "image_datasets_od_plate_samples_+L5-0",
                "image_datasets_od_plate_samples_+L5-1",
                "image_datasets_od_plate_samples_+L6-0",
                "image_datasets_od_plate_samples_+L7-0",
                "image_datasets_od_plate_samples_+L8-0",
                "image_datasets_od_plate_samples_+L9-0"]
    for name in nameList:
        print("python manipulate_files.py -m generate_file_list -d /home/c00453140/data/tun/lpd/round1/"+name+" -o /home/c00453140/data/tun/lpd/filelist/round01/"+name+".txt -v")
