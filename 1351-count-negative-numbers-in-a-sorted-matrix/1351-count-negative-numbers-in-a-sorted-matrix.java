class Solution {
    public int countNegatives(int[][] grid) {
        int current = 0;
        int cols = grid[0].length;
        for (int i = 0; i < grid.length; i++) {
            int left = 0;
            int mid = 0;
            int right = cols - 1;
            int index = cols;
            while (left <= right) {
                mid = (left + right) / 2;
                if (grid[i][mid] <0) {
                    index = mid;
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
            current += (cols - index);
        }
        return current;
    }
}