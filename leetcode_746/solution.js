/**
 * @param {number[]} cost
 * @return {number}
 */
var minCostClimbingStairs = function(cost) {
    let n = cost.length;
    if (n == 0)
        return 0;
    var dp0 = 0, dp1 = 0;
    for (let i = 2; i < n + 1; i++) {
        let step2 = dp0 + cost[i - 2];
        let step1 = dp1 + cost[i - 1];
        dp0 = dp1;
        dp1 = Math.min(step2, step1);
    }
    return dp1;
};