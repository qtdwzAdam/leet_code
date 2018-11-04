/*
 * File Name       : lc476.cpp
 *
 * Author        : Adam
 * Email         : zju_duwangze@163.com
 *
 * Created on    : 2018-06-15 22:20:53
 * Last Modified : 2018-10-29 23:22:22
 * Description   : 
 */

#include <iostream>

using namespace std;

class Solution {
public:
    int findComplement(int n) {
        int res = 0;
        int pow = 0;
        int tmp = 0;
        while (n){
            tmp = (n%2)^1;
            n = n>>1;
            res += tmp << pow;
            pow++;
        }
        return res;
    }
};

int main(){
    cout << Solution().findComplement(9);
    return 0;
}
