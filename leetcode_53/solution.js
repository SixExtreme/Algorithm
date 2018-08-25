/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let n = nums.length
    if (n == 0)
        return 0;
    let sum = 0, _max = nums[0];
    for (let i = 0; i < n; i++) {
        sum += nums[i];
        sum = Math.max(sum, nums[i])
        if (sum > _max)
            _max = sum
    }
    return _max
};