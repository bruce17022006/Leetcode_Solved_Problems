class Solution {
    public boolean canAliceWin(int[] nums) {
        int single=0, doublee=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]<=9){
                single+=nums[i];
            }
            else{
                doublee+=nums[i];
            }
        }
        if(single!=doublee){
            return true;
        }
        return false; 
    }
}