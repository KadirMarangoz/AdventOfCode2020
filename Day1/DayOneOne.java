import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

public class DayOneOne {


    public static void main(String[] args) throws IOException {
        ArrayList<Integer> integers = new ArrayList<>();
        Scanner scanner = new Scanner(new File("C:\\Users\\20171909\\Documents\\AOC\\Day1\\input_one.txt"));
        while(scanner.hasNextInt()){
            integers.add(scanner.nextInt());
        }
        for(int i: integers){
            for(int j: integers){
                if(i + j == 2020){
                    System.out.println(i * j);
                    return;
                }
            }
        }
    }
}
