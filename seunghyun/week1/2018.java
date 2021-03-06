import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        int count = 1;
        int left = 1;
        int right = 1;
        int sum = 1;

        while (right != N) {
            if (sum < N) {
                right++;
                sum += right;
            } else if (sum > N) {
                sum -= left;
                left++;
            } else if (sum == N) {
                count++;
                right++;
                sum += right;
            }
        }

        System.out.println(count);
    }
}
