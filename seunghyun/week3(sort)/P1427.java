/*
 * https://www.acmicpc.net/problem/1427
 * 실버V
 *
 * 선택정렬 특징 - O(n^2)
 *
 */

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();

        int[] A = new int[str.length()];
        for (int i = 0; i < str.length(); i++) {
            A[i] = Integer.parseInt(str.substring(i, i+1));
        }

        for (int i = 0; i < A.length; i++) {
            int maxIdx = i;
            for (int j = i + 1; j < A.length; j++) {
                if (A[j] > A[maxIdx]) {
                    maxIdx = j;
                }
            }
            if (A[maxIdx] > A[i]) {
                int temp = A[i];
                A[i] = A[maxIdx];
                A[maxIdx] = temp;
            }
        }

        for (int i = 0; i < A.length; i++) {
            System.out.print(A[i]);
        }
    }
}
