/*
 * File Name       : lc_821.java
 *
 * Author        : Adam
 * Email         : zju_duwangze@163.com
 *
 * Created on    : 2018-11-12 17:47:19
 * Last Modified : 2018-11-13 09:33:22
 * Description   : 
 * Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.
 *
 * Example 1:
 *
 * Input: S = "loveleetcode", C = 'e'
 * Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 */
import java.util.Arrays;
import java.util.ArrayList;

class Solution {
    public int[] shortestToChar(String s, char c) {
        ArrayList<Integer> idxC = new ArrayList<>();
        int [] res = new int[s.length()];
        for (int i=0; i<s.length(); i++) {
            if (s.charAt(i) == c) {
                idxC.add(i);
            }
        }

        int now = 0;
        int lenIdx = idxC.size() - 1;
        if (lenIdx == -1) {
            for (int i = 0; i<res.length; i++)
                res[i] = Integer.MAX_VALUE;
            return res;
        }
        for (int i=0; i<s.length(); i++) {
            if (s.charAt(i) == c){
                res[i] = 0;
                if (now < lenIdx) now ++;
                continue;
            }
            if (i > idxC.get(now))
                res[i] = i - idxC.get(lenIdx);
            else if (now == 0){
                res[i] = Math.abs(idxC.get(now) - i);
            } else {
                res[i] = Math.min(i-idxC.get(now-1), idxC.get(now) - i);
            }

        }

        return res;
    }
}

public class lc_821 {
    public static void main(String[] args) {
        String s = "aaba";
        char c = 'a';
        Solution so = new Solution();
        int [] res = so.shortestToChar(s, c);
        System.out.println(Arrays.toString(res));
    }
}
