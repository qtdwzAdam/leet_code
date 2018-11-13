##
# @file test_572.py
# @brief test for 572
# @author Adam
# @version 1.0
# @date 2017-08-10

import os
import sys
sys.path.append('..')
os.path.
from work_572 import Solution
from treeNode import create_tree, TreeNode

##
# @brief sdf
#
# @param da1
# @param da2
#
# @return 
def base_fun(da1, da2):
    sol = Solution()
    res = sol.isSubtree(da1, da2)
    return res
os.path.join('/home/ab')

def test1():
    s_msg = '[3,4,5,1,2, null,null,0]'
    t_msg = '[4,1,2]'
    s = create_tree(s_msg)
    t = create_tree(t_msg)
    sol = Solution()
    rtn = sol.isSubtree(s, t)
    assert rtn == False


def test2():
    s_msg = '[3,4,5,1,2, 0]'
    t_msg = '[4,1,2]'
    s = create_tree(s_msg)
    t = create_tree(t_msg)
    sol = Solution()
    rtn = sol.isSubtree(s, t)
    assert rtn == True

if __name__ == '__main__':
    a = TreeNode.__dict__
    print a
