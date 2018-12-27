/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    if (nums.length == 0)
        return 0;
    let sum = 0, max = nums[0];
    for (let i = 0; i < nums.length; i++) {
        sum += nums[i];
        if (nums[i] > sum) {
            sum = nums[i]
        }
        if (sum > max)
            max = sum
    }
    return max
};