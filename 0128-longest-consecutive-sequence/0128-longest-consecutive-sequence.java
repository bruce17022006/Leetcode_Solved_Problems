class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer>set=new HashSet<>();
        int max=0;
        for(int num:nums){
            set.add(num);
        }
        for(int num:set){
            if(set.contains(num-1)) continue;
            int currentLength=0;
            while(set.contains(num)){
                currentLength++;
                num+=1;
            }
            max=Math.max(max,currentLength);
        }
        return max;
    }
}