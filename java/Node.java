/*
 * File Name       : Node.java
 *
 * Author        : Adam
 * Email         : zju_duwangze@163.com
 *
 * Created on    : 2018-10-12 22:08:52
 * Last Modified : 2018-10-16 22:20:36
 * Description   : 
 */
package lc;

import java.util.List;

public class Node {
    public int val;
    public List<Node> children;
    public Node() {}
    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
    public void make_nodes(){}
    public static void main(String[] args) {
        {"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6","children":[],"val":6}],"val":3},{"$id":"3","children":[],"val":2},{"$id":"4","children":[],"val":4}],"val":1}
    }
}
