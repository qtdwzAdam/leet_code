/*
 * File Name       : lc_872.java
 *
 * Author        : Adam
 * Email         : zju_duwangze@163.com
 *
 * Created on    : 2018-11-12 09:36:34
 * Last Modified : 2018-11-12 15:20:07
 * Description   : 
 */
import MakeLeetCodeClass.TreeNode;
import java.util.ArrayList;

class Solution {
    private void getLeaf(TreeNode root, ArrayList<Integer> res) {
        if (root != null)
            if (root.left == null && root.right == null){
                res.add(root.val);
            } else {
                if (root.left != null) getLeaf(root.left, res);
                if (root.right != null) getLeaf(root.right, res);
            }
    }
    public boolean leafSimilar(TreeNode root1, TreeNode root2){
        ArrayList<Integer> res1 = new ArrayList<>(), res2 = new ArrayList<>();
        getLeaf(root1, res1);
        getLeaf(root2, res2);
        if (res1.equals(res2))
            return true;
        return false;
    }
}

public class lc_872{
    public static void main(String[] args){
        String str1 = "[1,2]";
        String str2 = "[2,2]";
        TreeNode root1 = TreeNode.mkTree(str1);
        TreeNode root2 = TreeNode.mkTree(str2);
        Solution so = new Solution();
        System.out.println(so.leafSimilar(root1, root2));
    }
}
