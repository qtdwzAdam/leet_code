/*
 * File Name       : lc36.cpp
 *
 * Author        : Adam
 * Email         : zju_duwangze@163.com
 *
 * Created on    : 2018-06-15 23:06:44
 * Last Modified : 2018-10-29 23:22:39
 * Description   : 
 */
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool isValidSudoku(vector<vector<char> > & board) {
        return board.empty();

    }
};

int main(){
    vector<vector<char> > board = {{"5","3",".",".","7",".",".",".","."}, {"6",".",".","1","9","5",".",".","."}, {".","9","8",".",".",".",".","6","."}, {"8",".",".",".","6",".",".",".","3"}, {"4",".",".","8",".","3",".",".","1"}, {"7",".",".",".","2",".",".",".","6"}, {".","6",".",".",".",".","2","8","."}, {".",".",".","4","1","9",".",".","5"}, {".",".",".",".","8",".",".","7","9"} };
    cout << Solution().isValidSudoku(&board);
    return 0;
}
