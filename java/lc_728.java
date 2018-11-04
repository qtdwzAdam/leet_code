/*
 * File Name       : lc_728.java
 *
 * Author        : Adam
 * Email         : zju_duwangze@163.com
 *
 * Created on    : 2018-10-16 22:43:40
 * Last Modified : 2018-10-18 22:43:51
 * Description   : 
 */

import java.util.*;

class Solution {
    private static boolean checkAvailable(int val){
        int x, tmp=val;
        while (tmp > 0){
            x = tmp % 10;
            if (x==0 || val % x != 0) return false;
            tmp = tmp / 10;
        }
        return true;
    }
    public List <Integer> selfDividingNumbers(int left, int right){
        ArrayList <Integer> res = new ArrayList <Integer>();
        for (int i=left; i<=right; i++){
            if (Solution.checkAvailable(i)){
                res.add(i);
            }
        }
        return res;
    }

}

public class lc_728 {
    public static void main(String[] args) {
        int l = 1, r = 22;
        Solution so = new Solution();
        List<Integer> out = so.selfDividingNumbers(l, r);
        for (Integer x: out){
            System.out.println(x);
        }

    }
}
