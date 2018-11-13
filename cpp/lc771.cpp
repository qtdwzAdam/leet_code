/*
 * File Name       : lc771.cpp
 *
 * Author        : Adam
 * Email         : zju_duwangze@163.com
 *
 * Created on    : 2018-08-12 21:25:38
 * Last Modified : 2018-08-12 21:32:00
 * Description   : 
 */

#include <iostream>
#include <set>

using namespace std;

class Solution {
public:
    int numJewelsInStones(string J, string S) {
        set<char> jset;
        for (auto i: J){
            jset.insert(i);
        }
        int cnt = 0;
        for (auto j: S){
            if (jset.count(j))
                cnt += 1;
        }
        return cnt;

    }
};

int main(){
    Solution s;
    cout << s.numJewelsInStones("aB", "aaabB");
}

