# private static int Solution(int[] nums, int i, int target) {
#         if (i == nums.length - 1){
#             return target == 0?1:0;
#         }
#         return Solution(nums,i + 1,target - nums[i]) + Solution(nums, i + 1, target + nums[i]);
#     }
#
#     public static int findTargetSumWays2(int[] nums, int target){
#         return Solution2(nums,0, target,new HashMap<>());
#     }
from typing import List


def findTargetSumWays2(nums:List, target:int)->int:
    return Solution(nums,0,target)
def Solution(nums, i, target):
    if i == len(nums):
        return 1 if target == 0 else 0
    return Solution(nums, i+1, target - nums[i]) + Solution(nums, i+1, target + nums[i])

# 年会抽奖
import random

staff_list = []
for user in range(1, 301):
    staff_list.append(f"员工{user}")

level = [30, 6, 3]

for i in range(3):
    winner_list = random.sample(staff_list, level[i]) # staff_list,:随机抽取目标 ， level抽取个数

    for winner in winner_list:
        staff_list.remove(winner)

    print(f"获得{3 - i}等奖的是：{winner_list}")
    print(f"还剩{len(staff_list)}人未中奖")