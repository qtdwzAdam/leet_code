/*
 * File Name       : lc_905.java
 *
 * Author        : Adam
 * Email         : zju_duwangze@163.com
 *
 * Created on    : 2018-10-10 23:19:57
 * Last Modified : 2018-10-29 23:21:08
 * Description   : 
 */
class Solution {
    public int[] sortArrayByParity(int [] a) {
        int [] c = new int[a.length];
        int len = a.length;
        if (len<2) return a;
        int st=0, end=a.length-1;
        int tmp = 0;
        while (st <= end){
            while (st < len && a[st] % 2 == 0) st ++;
            while (end >= 0 && a[end] % 2 == 1) end --;
            if (st > end) break;
            tmp = a[st];
            a[st] = a[end];
            a[end] = tmp;
            st ++;
            end --;

        }
        return a;
    }
}

public class lc_905 {
    public static void main(String[] args) {
        int[] a = {0, 2};
        System.out.println("Hello World");
        Solution so = new Solution();
        int [] b = so.sortArrayByParity(a);
        for (int x: b)
        System.out.print(x);
    }
}
