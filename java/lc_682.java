/*
 * File Name       : lc_682.java
 *
 * Author        : Adam
 * Email         : zju_duwangze@163.com
 *
 * Created on    : 2018-10-30 16:33:43
 * Last Modified : 2018-10-30 17:04:52
 * Description   : 
 */
import java.util.ArrayDeque;

public class lc_682 {
    public int calPoints(String[] ops){
        int res = 0;
        int first = 0;
        int second = 0;
        ArrayDeque<Integer> stack = new ArrayDeque<Integer>();
        for (String each: ops){
            switch (each){
                case "D":
                    first = stack.peek();
                    res += first * 2;
                    stack.push(first * 2);
                    break;
                case "C":
                    first = stack.pop();
                    res -= first;
                    break;
                case "+":
                    first = stack.pop();
                    second = stack.peek();
                    res += first + second;
                    stack.push(first);
                    stack.push(first + second);
                    break;
                default:
                    first = Integer.valueOf(each);
                    res += first;
                    stack.push(first);
                    break;
            }

        }
        return res;
    }
    public static void main(String[] args) {
        lc_682 so = new lc_682();
        //String [] ops = {"5","2","C","D","+"};
        String [] ops = {"5","-2","4","C","D","9","+","+"};
        System.out.println(so.calPoints(ops));
    }
}

