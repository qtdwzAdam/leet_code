/*
 * File Name       : lc_283.java
 *
 * Author        : Adam
 * Email         : zju_duwangze@163.com
 *
 * Created on    : 2018-11-12 17:21:47
 * Last Modified : 2018-11-12 17:44:39
 * Description   : 
 */

import java.util.Arrays;

class Solution {
    public void moveZeroes(int [] nums) {
        int left=0, len=nums.length, right=len-1;
        for (int i=0; i<len; i++){
            if (nums[i] != 0){
                if (i==left){
                    left ++;
                    continue;
                }
                nums[left] = nums[i];
                left ++;
            }
        }
        for (; left<len; left++) {
            nums[left] = 0;
        }

    }
}

public class lc_283{
    public static void main(String[] args) {
        Solution so = new Solution();
        int [] nums = {0,1,0,3,12, 0,4,0};
        System.out.println(Arrays.toString(nums));
        so.moveZeroes(nums);
        System.out.println(Arrays.toString(nums));
    }
}
