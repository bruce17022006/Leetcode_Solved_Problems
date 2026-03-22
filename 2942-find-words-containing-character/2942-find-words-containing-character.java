class Solution {
    public List<Integer> findWordsContaining(String[] words, char x) {
        int n=words.length;
        List<Integer> res=new ArrayList<>();
        for(int i=0;i<n;i++){
            String s=String.valueOf(x);
            if(words[i].contains(s)){
                res.add(i);
            }
        }
        return res;
    }
}