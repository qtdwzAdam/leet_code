/*
 * File Name       : function.cpp
 *
 * Author        : Adam
 * Email         : zju_duwangze@163.com
 *
 * Created on    : 2018-08-18 16:18:18
 * Last Modified : 2018-08-22 23:19:53
 * Description   : 
 */

#include <iostream>
#include <vector>

using namespace std;
template <typename T> void printOneVect(const T &todo){
    cout << "####### start of printOneVect######" << endl;
    for (auto x: todo){
        cout << x << " ";
    }
    cout << endl;
    cout << "####### end of printOneVect######" << endl;
}

template <typename T> void printTwoVect(const T &todo){
    cout << "####### start of printTwoVect######" << endl;
    for (auto vec: todo){
        for (auto x: vec){
            cout << x << " ";
        }
        cout << endl;
    }
    cout << "####### end of printTwoVect######" << endl;
}

template <typename T> vector<vector<T> > getTwoVec(string s){
    vector<vector<T> > res;
    auto tmp = s.find("],", 90);
    cout << tmp;
    cout << s;
    return res;
}

void test(){
    cout << "in test" << endl;
}

int main(){
    string s = "[[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]";
    getTwoVec<vector<vector<int> > >(s);
    //vector<int> a1{1,2,3}, a2{4,5,6};
    //vector<vector<int> > a{a1, a2};
    //printOneVect(a1);
    //printTwoVect(a);
    cout << "hello world!";
}

