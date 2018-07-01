/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} t1
 * @param {TreeNode} t2
 * @return {TreeNode}
 */
var mergeTrees = function(t1, t2) {
    if (!t1 || !t2) {
        return t1 || t2;
    }
    let s1 = [t1], s2 = [t2];
    while (s1.length !== 0) {
        let n1 = s1.pop(), n2 = s2.pop();
        n1.val += n2.val;
        if (!n1.right && n2.right) {
            n1.right = n2.right;
        } else if (n1.right && n2.right) {
            s1.push(n1.right);
            s2.push(n2.right);
        }
        if (!n1.left && n2.left) {
            n1.left = n2.left;
        } else if (n1.left && n2.left) {
            s1.push(n1.left);
            s2.push(n2.left)
        }
    }
    return t1;
};