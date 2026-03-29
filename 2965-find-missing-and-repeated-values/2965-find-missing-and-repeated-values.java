class Solution {
    public int[] findMissingAndRepeatedValues(int[][] grid) {
        HashMap<Integer,Integer> map= new HashMap<>();
        ArrayList<Integer> answer=new ArrayList<>();
        int expected_sum=0,actual_sum=0;
        int n=grid.length;
        int ans[]=new int[2];
        for(int i=0;i<grid.length;i++){
            for(int j=0;j<grid[i].length;j++){
                 actual_sum+=grid[i][j];
                int element=grid[i][j];
                map.put(element,map.getOrDefault(element,0)+1);
            }
        }
        int a=0;
        for(Integer key : map.keySet()){
            if(map.get(key)>1){
                a=key;
                answer.add(key);
            }
        }
        expected_sum=(n*n)*(n*n+1)/2;
        int b=expected_sum+a-actual_sum;
        answer.add(b);
        for(int i=0;i<answer.size();i++){
            ans[i]=answer.get(i);
        }
        return ans;
    }
}