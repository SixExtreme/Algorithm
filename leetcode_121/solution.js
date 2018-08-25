/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let n = prices.length;
    if (n == 0) {
        return 0;
    } else {
        let _min = prices[0], profit = 0;
        for (let i = 1; i < n; i++) {
            if (prices[i] < _min) {
                _min = prices[i];
            } else {
                let delta = prices[i] - _min;
                if (delta > profit) {
                    profit = delta;
                }
            }
        }
        return profit;
    }
};