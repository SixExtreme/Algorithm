package main

func rob(nums []int) int {
	sa, sb := 0, 0
	for i, x := range nums {
		if i % 2 == 0 {
			if sa + x < sb {
				sa = sb
			} else {
				sa += x
			}
		} else {
			if sb + x < sa {
				sb = sa
			} else {
				sb += x
			}
		}
	}
	if sa > sb {
		return sa
	} else {
		return sb
	}
}