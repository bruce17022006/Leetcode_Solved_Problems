class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        int maxLength = 0;
        
        // Array tracks the next valid index for all 128 ASCII characters
        int[] nextIndex = new int[128];
        
        for (int right = 0, left = 0; right < n; right++) {
            int charCode = s.charAt(right);
            
            // Jump left pointer forward if the character was seen inside the window
            left = Math.max(nextIndex[charCode], left);
            
            maxLength = Math.max(maxLength, right - left + 1);
            
            // Update the next index position (1-based index)
            nextIndex[charCode] = right + 1;
        }
        
        return maxLength;
    }
}