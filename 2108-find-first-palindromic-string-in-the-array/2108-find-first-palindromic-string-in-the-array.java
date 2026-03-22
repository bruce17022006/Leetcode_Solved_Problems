class Solution {
    public String firstPalindrome(String[] words) {
        for(int i=0;i<words.length;i++){
                StringBuilder temp= new StringBuilder();
                temp.append(words[i]);
                temp.reverse();
                if(temp.toString().equals(words[i])){
                    return words[i];
                }
        }
        return "";
        
    }
}