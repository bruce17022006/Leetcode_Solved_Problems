class Solution {
    public int firstMissingPositive(int[] nums) {
        int [] arr=new int[nums.length+1];
        int i=0;
        for(i=0;i<nums.length;i++)
        {
            int j=nums[i];
            if(j>=0 && j<=nums.length)
            {
                arr[j]=1;
            }
        }
        for(i=1;i<nums.length+1;i++)
        {
            if(arr[i]!=1)
            {
                return i;
            }
        }
        if(i==nums.length) return nums.length;
        else return nums.length+1;
    }
}