/*
 * File Name       : TreeNode.java
 *
 * Author        : Adam
 * Email         : zju_duwangze@163.com
 *
 * Created on    : 2018-11-03 16:12:55
 * Last Modified : 2018-11-12 16:55:17
 * Description   :
 */

package MakeLeetCodeClass;

import java.util.Arrays;

public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int x) { val = x; }

    public String toString(){
        return Integer.toString(val);
    }

    private void _firstPrint() {
        System.out.print(val + " ");
        if (left != null) left._firstPrint();
        if (right != null) right._firstPrint();
    }

    public void firstPrint() {
        _firstPrint();
        System.out.println("");
    }

    private void _midPrint(){
        if (left != null) left._midPrint();
        //else System.out.print("null ");
        System.out.print(val + " ");
        if (right != null) right._midPrint();
        //else System.out.print("null ");
    }

    public void midPrint() {
        _midPrint();
        System.out.println("");
    }

    private void _lastPrint(){
        if (left != null) left._lastPrint();
        //else System.out.print("null ");
        if (right != null) right._lastPrint();
        else System.out.print("null ");
        //System.out.print(val + " ");
    }

    public void lastPrint() {
        _lastPrint();
        System.out.println("");
    }

//    int []arr = {3, 9, 20, Integer.MAX_VALUE, Integer.MAX_VALUE, 15, 7};
    private static int[] StrToIntArray(String str) {
        str = str.substring(1, str.length() - 1);
        String []strs = str.split(",");
        int []arr = new int[strs.length];

        for (int i = 0; i < arr.length; i++) {
            if (strs[i].equals("null")) {
                arr[i] = Integer.MAX_VALUE;
            } else {
                arr[i] = Integer.parseInt(strs[i]);
            }
        }

        return arr;
    }

//    String str = "[3,9,20,null,null,15,7]";
    public static TreeNode mkTree(String str) {

        int []arr = StrToIntArray(str);
        TreeNode []nodes = new TreeNode[arr.length + 1];
        for (int i = 1; i < nodes.length; i++) {
            if (arr[i - 1] != Integer.MAX_VALUE) {
                nodes[i] = new TreeNode(arr[i - 1]);
            }else {
                nodes[i] = null;
            }
        }

        TreeNode node = null;
        for (int i = 1; i < nodes.length; i++) {
            node = nodes[i];
            if (node == null) continue;
            if (2*i < nodes.length) node.left = nodes[2 * i];
            if (2*i+1 < nodes.length) node.right = nodes[2 * i + 1];
        }
        return nodes[1];
    }

    public static void main(String [] args) {
        String str = "[5,3,6,2,4,null,8,1,null,null,null,null,null,7,9]";
        TreeNode node = TreeNode.mkTree(str);
        node.firstPrint();
        node.midPrint();
    }
}
