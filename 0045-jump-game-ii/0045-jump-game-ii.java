class Solution {
    public int jump(int[] nums) {
        if(nums.length<=1) return 0;
        int jump=0;
        int farthest=0;
        int currentEnd=0;
        for(int i=0;i<=nums.length;i++){
            if(i+nums[i]>farthest){
                farthest=i+nums[i];
            }
            if(i==currentEnd){
                jump++;
                currentEnd=farthest;

                if(currentEnd>=nums.length-1){
                    break;
                }
            }
        }  
        return jump;
    }
}