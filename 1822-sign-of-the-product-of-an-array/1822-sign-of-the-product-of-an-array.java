class Solution {
    public int arraySign(int[] nums) {
        int x=1;
        for(int i=0;i<nums.length;i++){
            if(nums[i]==0){
                return 0;
            }
            if(nums[i]<0){
                x*=-1;
            }
        }
        return x;
    }
}