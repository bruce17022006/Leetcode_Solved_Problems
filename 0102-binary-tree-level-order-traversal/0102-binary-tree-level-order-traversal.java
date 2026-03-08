/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        Queue<TreeNode> q=new LinkedList<>();
        q.add(root);
        List<List<Integer>> res= new ArrayList();
        if(root==null) return res;
        while(q.size()!=0)
        {
            int size=q.size();
            ArrayList<Integer> currentLevelElements=new ArrayList<>();
            while(size-- >0)
            {
                TreeNode current_element = q.poll();
                currentLevelElements.add(current_element.val);
                if(current_element.left!=null) q.add(current_element.left);
                if(current_element.right!=null) q.add(current_element.right);
            }
            res.add(currentLevelElements);             
        }   
        return res;     
    }
}