/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> result;
        if(!root)
        return {};
        queue<TreeNode*> q;
        q.push(root);
        bool l_to_r=true;
        while(!q.empty()){
            int s=q.size();
            vector<int> l(s);
            int index;
            for(int j=0;j<s;j++){
                TreeNode* x=q.front();
                q.pop();
                index=l_to_r ? j : s - j - 1;
                l[index]=x->val;
                if(x->left)
                q.push(x->left);
                if(x->right)
                q.push(x->right);
            }
            result.push_back(l);
            l_to_r= !l_to_r;
        }
        return result;
    }
};