/*
 * File Name       : lc_868.java
 *
 * Author        : Adam
 * Email         : zju_duwangze@163.com
 *
 * Created on    : 2018-10-20 11:24:11
 * Last Modified : 2018-10-25 23:40:06
 * Description   : 
 */
class Solution{
    public int binaryGap(int N){
        int ma = 0;
        int now_gap = -1;
        while (N > 0){
            if (N % 2 == 1){
                now_gap += 1;
                if (now_gap > 0){
                    ma = ma > now_gap ? ma: now_gap;
                    now_gap = 0;
                }
            } else if (now_gap > -1){
                now_gap += 1;
            }
            N = N / 2;
        }

        return ma;
    }
}

public class lc_868 {
    public static void main(String[] args) {
        Solution so = new Solution();
        System.out.println(so.binaryGap(5));
    }
}
