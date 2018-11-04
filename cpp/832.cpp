/*
 * File Name       : 832.cpp
 *
 * Author        : Adam
 * Email         : zju_duwangze@163.com
 *
 * Created on    : 2018-08-18 16:13:15
 * Last Modified : 2018-08-22 23:11:01
 * Description   : 
 */

#include <iostream>
#include <vector>
#include "function.cpp"

using namespace std;

class Solution {
public:
    vector<vector<int> > flipAndInvertImage(vector<vector<int> > & A) {
        vector<vector<int> > res;
        for (auto one_line: A){
            auto st = one_line.begin();
            auto end = one_line.end() - 1;
            while (st < end){
                auto tmp = *st;
                *st = ! (*end);
                *end = !tmp;
                ++st; --end;
            }
            if (st == end)
                *st = ! (*st);
            res.push_back(one_line);
        }
        return res;
    }
};

int main(){
    Solution so;
    vector<int> a1{1,1,0,0}, a2{1,0,0,1}, a3{0,1,1,1}, a4{1,0,1,0};
    vector<int> b1{1,1,0}, b2{1,0,1}, b3{0,0,0};
    vector< vector<int> > a{a1, a2, a3, a4};
    vector< vector<int> > b{b1, b2, b3};
    cout << "before" << endl;
    printTwoVect(a);

    auto s = so.flipAndInvertImage(b);
    printTwoVect(s);
    cout << "end" << endl;
    //test();

    cout << "hello world!";
}

