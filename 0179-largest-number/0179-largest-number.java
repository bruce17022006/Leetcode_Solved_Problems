class Solution {
    public String largestNumber(int[] nums) {
        int n=nums.length;
        Integer A[]=new Integer[n];
        for(int i=0;i<n;i++){
            A[i]=nums[i];
        }
        Arrays.sort(A,new Comparator<Integer>(){
            public int compare(Integer a,Integer b){
                String ab=a+""+b;
                String ba=b+""+a;
                return ba.compareTo(ab);
            }
        });
        if(A[0]==0) return "0";
        String ans="";
        for(int val:A){
            ans=ans+val;
        }
        return ans;
    }
}