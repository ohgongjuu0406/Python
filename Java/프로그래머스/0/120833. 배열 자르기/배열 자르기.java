class Solution {
    public int[] solution(int[] numbers, int num1, int num2) {
        int[] answer = new int[num2-num1+1];
        int[] temp = new int[numbers.length - answer.length];
        
     
        for(int i = 0; i< numbers.length; i++){
            if(i<num1)
                temp[i] = numbers[i];
            else if (i>=num1 && i <= num2){
                answer[i-num1] = numbers[i];
            }
            else
                break;
            
        }
        return answer;
    }
}