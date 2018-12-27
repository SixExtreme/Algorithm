/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    if (n <= 2)
        return n;
    var dp1 = 1, dp2 = 2;
    for (let i = 2; i < n; i++) {
        let dp = dp1 + dp2;
        dp1 = dp2;
        dp2 = dp;
    }
    return dp2;
};