/*
 * File Name       : arr.cpp
 *
 * Author        : Adam
 * Email         : zju_duwangze@163.com
 *
 * Created on    : 2018-08-21 10:22:35
 * Last Modified : 2018-08-21 16:57:13
 * Description   : 
 */

#include <iostream>
#include <vector>
#include <string.h>
using namespace std;

void test(int n=1){
    cout << n<< endl;
}

int main(){
    cout << "hello";
    char tt[] = "123";
    cout << sizeof(tt);
    cout << strlen(tt);
    test();
    test(2);
    return 0;
}
