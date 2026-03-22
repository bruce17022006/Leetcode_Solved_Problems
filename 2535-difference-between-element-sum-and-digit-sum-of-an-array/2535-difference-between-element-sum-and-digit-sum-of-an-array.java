class Solution {
    public int differenceOfSum(int[] nums) {
        int x=0, y=0;
        int current=0;
        for(int i=0;i<nums.length;i++){
            x+=nums[i];
            current=nums[i];
            while(current>0){
                y+=current%10;
                current/=10;
            }
        }
        return Math.abs(x - y);
    }
}