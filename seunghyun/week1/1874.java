import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        int[] A = new int[N];
        for (int i = 0; i < N; i++) {
            A[i] = sc.nextInt();
        }

        Stack<Integer> stack = new Stack<>();
        StringBuilder sb = new StringBuilder();

        int num = 1;
        for (int i = 0; i < N; i++) {
            if (num <= A[i]) {
                while (num <= A[i]) {
                    stack.push(num++);
                    sb.append("+\n");
                }
                stack.pop();
                sb.append("-\n");
            } else { // num > A[i]
                int popped = stack.pop();
                if (popped > A[i]) {
                    System.out.println("NO");
                    return;
                }
                sb.append("-\n");
            }
        }

        System.out.println(sb.toString());
    }
}