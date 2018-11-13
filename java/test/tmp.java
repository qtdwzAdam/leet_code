/*
 * File Name       : tmp.java
 *
 * Author        : Adam
 * Email         : zju_duwangze@163.com
 *
 * Created on    : 2018-11-05 09:29:45
 * Last Modified : 2018-11-09 16:38:08
 * Description   : 
 */
import java.util.*;
import javax.swing.Timer;
import java.util.logging.Logger;


interface InterfaceTest{
    int x = 0;
    default void test(){
        System.out.println("default test work");
    }
}

class PrintSteam{
    public static double max(double... vals){
        double ma = Double.NEGATIVE_INFINITY;
        for (double v: vals)
            if (v > ma) ma = v;
        return ma;
    }
}

abstract class Person{
    public void test(){
        System.out.println("in Person test");
    }
    private String name;
    public Person(String name){
        this.name = name;
    }
    public abstract String getDescription();
    public String getName(){
        return name;
    }
}

public class tmp extends Person implements InterfaceTest{
    private String major;
    public tmp(String name, String major){
        super(name);
        this.major = major;
    }
    public String getDescription(){
        return "a student majorint in " + major;
    }
    public static void main(String[] args) {
        Comparator<String> comp
            = (a, b) -> a.length() - b.length();

        tmp[] people = new tmp[2];
        people[0] = new tmp("aa", "ma1");
        people[1] = new tmp("ab", "ma2");
        people[0].test();
        //System.out.println(Arrays.deepToString(people));
        //for (Person p: people){
            //System.out.println(p.getName() + ", " + p.getDescription());
            //System.out.println(p);
        //}
        //String[] planets = new String[] {"Mercury", "venus", "earth", "mars",
            //"jupiter", "saturn", "Uranus", "neptune"};
        //System.out.println(Arrays.toString(planets));
        //Arrays.sort(planets);
        //System.out.println(Arrays.toString(planets));
        //System.out.println("another");
        //Arrays.sort(planets, comp);
        //System.out.println(Arrays.toString(planets));
        //Logger.getGlobal().info("work");
        //Thread.dumpStack();
    }
    public String toString(){
        return getClass().getName() + "[name=" + getName() + "]";
    }
}
