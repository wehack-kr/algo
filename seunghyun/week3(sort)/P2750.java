/*
 * https://www.acmicpc.net/problem/2750
 * 브론즈I
 *
 * 버블정렬 특징 - O(n^2)
 * 전체 요소 개수 - 1 만큼 루프돌면서, 매 루프마다 가장 큰 수가 오른쪽으로 쌓이게 됌.
 * 매 루프마다 가장 큰수가 오른쪽으로 쌓이게 되니 다음 루프에서는 i만큼 뺀만큼만 반복문을 돌면 됌. (이미 정렬된 애들은 비교할 필요 없으니까)
 */

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] A = new int[N];


        for (int i = 0; i < N; i++) {
            A[i] = sc.nextInt();
        }

        for (int i = 0; i < N - 1; i++) {
            for (int j = 0; j < N - 1 - i; j++) {
                if (A[j+1] < A[j]) {
                    int temp = A[j];
                    A[j] = A[j+1];
                    A[j+1] = temp;
                }
            }
        }

        for (int i = 0; i < N; i++) {
            System.out.println(A[i]);
        }
    }
}
