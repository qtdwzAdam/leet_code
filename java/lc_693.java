/*
 * File Name       : lc_693.java
 *
 * Author        : Adam
 * Email         : zju_duwangze@163.com
 *
 * Created on    : 2018-11-03 15:37:19
 * Last Modified : 2018-11-03 16:00:41
 * Description   : 
 */
import java.util.*;
class Solution {
    public boolean hasAlternatingBits(int n){
        int tmp = n % 2;
        int no = 0;
        n = n / 2;
        while (n != 0){
            no = n % 2;
            if (no == tmp) return false;
            tmp = no;
            n = n / 2;
        }
        return true;
    }
}

public class lc_693 {
    public static void main(String[] args) {
        Solution so = new Solution();
        System.out.println(so.hasAlternatingBits(7));
    }
}
