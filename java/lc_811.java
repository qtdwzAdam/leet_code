/*
 * File Name       : lc_811.java
 *
 * Author        : Adam
 * Email         : zju_duwangze@163.com
 *
 * Created on    : 2018-11-13 10:12:56
 * Last Modified : 2018-11-14 20:44:42
 * Description   : 
 */

import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.HashMap;

class Solution {
    public List<String> subdomainVisits(String[] msgs) {
        ArrayList <String> res = new ArrayList<>();
        Map<String, Integer> cnt = new HashMap<>();
        String [] eachSplit, eachDomain;
        String tmpDomain;
        int eachCnt;
        for (String each : msgs) {
            eachSplit = each.split(" ");
            eachCnt = Integer.valueOf(eachSplit[0]);
            eachDomain = eachSplit[1].split("\\.");
            tmpDomain = eachDomain[eachDomain.length-1];
            cnt.merge(tmpDomain, eachCnt, (a, b) -> a + b);
            for (int i=eachDomain.length-2; i>=0; i--){
                tmpDomain = eachDomain[i] + "." + tmpDomain;
                //cnt.merge(tmpDomain, eachCnt, (a, b) -> a + b);
                cnt.put(tmpDomain, cnt.getOrDefault(tmpDomain, 0) + eachCnt);
            }
        }
        for (String eachKey: cnt.keySet()) {
            res.add(cnt.get(eachKey) + " " + eachKey);
        }

        return res;
    }
}

public class lc_811 {
    public static void main(String [] args) {
        String [] msgs = {"900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"};
        Solution so = new Solution();
        System.out.println((so.subdomainVisits(msgs)));
    }
}
