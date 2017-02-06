package com.company;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuffer sb = new StringBuffer();

        int N = Integer.parseInt(br.readLine());
        int[] seq = new int[N];
        //수열 배열 생성
        for (int i = 0; i < N; i++) {
            seq[i] = Integer.parseInt(br.readLine());
        }

        Stack<Integer> stack = new Stack<>();
        int pointer = 0;    //수열 배열 인덱스
        int seqNum = 1;     //수열에 들어갈 값
        stack.push(seqNum++);   //스택 첫 값 입력
        sb.append("+\n");

        while (pointer < N) {   //배열의 갯수(N)만큼 포인터가 이동하면 종료
            while (stack.peek() < seq[pointer]){
                stack.push(seqNum++);
                sb.append("+\n");
            }

            if(stack.peek() == seq[pointer]){
                stack.pop();
                pointer++;
                sb.append("-\n");
            }

        }
        if(stack.empty()){
            System.out.println(sb);
        }else{
            System.out.println("NO");
        }

    }
}