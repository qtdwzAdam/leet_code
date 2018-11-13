/*
 * File Name       : lc_897.java
 *
 * Author        : Adam
 * Email         : zju_duwangze@163.com
 *
 * Created on    : 2018-11-12 15:46:09
 * Last Modified : 2018-11-12 17:21:15
 * Description   : 
 */

import MakeLeetCodeClass.TreeNode;
import java.util.ArrayList;
import java.util.Arrays;

class Solution{
    public TreeNode increasingBST(TreeNode root) {
        ArrayList<Integer> msg = new ArrayList<>();
        midAdd(root, msg);
        TreeNode newRoot = new TreeNode(msg.get(0));
        msg.remove(msg.get(0));
        TreeNode tmpRoot = newRoot;
        for (Integer x: msg){
            TreeNode thisNode = new TreeNode(x);
            tmpRoot.right = thisNode;
            tmpRoot = thisNode;
        }

        return newRoot;
    }

    private void midAdd(TreeNode root, ArrayList<Integer> msg){
        if (root == null) return;
        midAdd(root.left, msg);
        msg.add(root.val);
        midAdd(root.right, msg);
    }

}

public class lc_897 {
    public static void main(String[] args) {
        String str = "[5,3,6,2,4,null,8,1,null,null,null,null,null,7,9]";
        TreeNode root = TreeNode.mkTree(str);
        root.firstPrint();

        Solution so = new Solution();
        System.out.println(so.increasingBST(root));
    }
}
