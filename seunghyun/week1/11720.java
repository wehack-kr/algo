import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int sum = 0;

        String sNum = sc.next();
        char[] cNum = sNum.toCharArray();

        for (int i = 0; i < cNum.length; i++) {
            sum += cNum[i] - '0'; // or 48
        }

        System.out.println(sum);
    }
}