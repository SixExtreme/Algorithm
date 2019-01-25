struct Solution;

impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        if nums.len() == 0 {
            return 0;
        }

        let mut i = 0;
        for j in 0..nums.len() {
            if nums[j] != nums[i] {
                nums[i + 1] = nums[j];
                i += 1;
            }
        }

        return (i + 1) as i32;
    }
}

fn main() {
    let mut nums = vec![0, 0, 1, 1, 2, 2, 2, 3, 4, 5, 5];
    println!("{}", Solution::remove_duplicates(&mut nums));
}