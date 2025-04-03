import java.util.Arrays;

class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        // 오름차순 정렬
        Arrays.sort(numbers);
        
        //자바는 음수 인덱스 불가
        int idx = numbers.length - 1;
        answer = numbers[idx] * numbers[idx - 1];
        
        return answer;
    }
}