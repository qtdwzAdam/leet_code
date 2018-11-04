/*
 * File Name       : lc_657.java
 *
 * Author        : Adam
 * Email         : zju_duwangze@163.com
 *
 * Created on    : 2018-10-12 21:52:34
 * Last Modified : 2018-10-12 22:07:29
 * Description   : 
 */

class Solution {
    public boolean judgeCircle(String moves) {
        int u=0, l=0;
        for (int i=0; i<moves.length(); i++){
            char x = moves.charAt(i);
            if (x == 'U') u++;
            else if (x == 'D') u--;
            else if (x == 'L') l++;
            else if (x == 'R') l--;
            else System.out.println("error");
        }
        return u==0 && l==0;

    }
}

public class lc_657 {
    public static void main(String[] args) {
        Solution so = new Solution();
        System.out.println(so.judgeCircle("UDLR"));
    }
}
