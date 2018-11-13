/*
 * File Name       : PairTest1.java
 *
 * Author        : Adam
 * Email         : zju_duwangze@163.com
 *
 * Created on    : 2018-11-06 11:32:46
 * Last Modified : 2018-11-06 16:31:50
 * Description   : 
 */
import javafx.util.Pair;
import java.util.Collections;

public class PairTest1 {
    public static void main(String[] args) {
        String [] words = {"Mary", "had", "a", "little", "lamb"};
        Pair<String, String> mm = ArrayAlg.minmax(words);
        System.out.println("min = " + mm.getKey());
        System.out.println("max = " + mm.getValue());
        System.out.println("check" + ArrayAlg.getMiddle(1, 2, 4,4 ,5.3 ));
    }
}

class ArrayAlg{
    public static Pair<String, String> minmax(String[] a){
        if (a == null || a.length == 0) return null;
        String min = a[0];
        String max = a[0];
        for (String x : a){
            if (min.compareTo(x) > 0) min = x;
            if (max.compareTo(x) < 0) max = x;
        }
        return new Pair<>(min, max);
    }
    public static <T> T getMiddle(T... a){
        return a[a.length / 2];
    }
}
