/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    if (n <= 2)
        return n;
    var dp0 = 1, dp1 = 2;
    for (let i = 2; i < n; i++) {
        let dp = dp0 + dp1;
        dp0 = dp1;
        dp1 = dp;
    }
    return dp1;
};