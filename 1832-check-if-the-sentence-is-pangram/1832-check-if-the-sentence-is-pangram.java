class Solution {
    public boolean checkIfPangram(String sentence) {
            int n=sentence.length();
            Set<Character> seen=new HashSet<>();
            for(int i=0;i<n;i++){
                char c=sentence.charAt(i);
                if(Character.isLetter(c)){
                seen.add(Character.toLowerCase(c));
                }
            }
        if(seen.size()==26){
            return true;
        }
        else{
            return false;

        }
        }
    }