/*
 * File Name       : lc709.cpp
 *
 * Author        : Adam
 * Email         : zju_duwangze@163.com
 *
 * Created on    : 2018-08-12 21:38:10
 * Last Modified : 2018-11-04 10:59:45
 * Description   : 
 */

#include <iostream>

using namespace std;

class Solution {
public:
    string toLowerCase(string str) {
        string out;
        for (auto i: str){
            if('A' <= i && i <= 'Z'){
                out += i- 'A' + 'a';
            } else {
                out += i;
            }
        }
        return out;

    }
};

int main(){
    Solution s;
    cout << s.toLowerCase("Hello");
}

