/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    let sa = 0, sb = 0;
    for (let i = 0; i < nums.length; i++) {
        if (i % 2 == 0)
            sa = Math.max(sa + nums[i], sb);
        else
            sb = Math.max(sb + nums[i], sa);
    }
    return Math.max(sa, sb);
};