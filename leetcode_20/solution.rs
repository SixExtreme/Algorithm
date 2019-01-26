struct Solution;

//fn abs(a: char, b: char) -> u8 {
//    let ia = a as u8;
//    let ib = b as u8;
//
//    if ia < ib {
//        ib - ia
//    } else {
//        ia - ib
//    }
//}

impl Solution {
//    pub fn is_valid(s: String) -> bool {
//        let mut stack = vec![];
//
//        for c in s.chars() {
//            if stack.is_empty() {
//                stack.push(c);
//            } else {
//                let peek = *stack.last().unwrap();
//                let delta = abs(peek, c);
//                if delta > 0 && delta < 3 {
//                    stack.pop();
//                } else {
//                    stack.push(c);
//                }
//            }
//        }
//
//        return stack.is_empty();
//    }

    pub fn is_valid(s: String) -> bool {
        let mut stack = vec![];

        for c in s.chars() {
            if c == '(' {
                stack.push(')');
            } else if c == '[' {
                stack.push(']');
            } else if c == '{' {
                stack.push('}');
            } else if stack.is_empty() || stack.pop().unwrap() != c {
                return false;
            }
        }

        return stack.is_empty();
    }
}


fn main() {
    println!("{}", Solution::is_valid("([)".to_string()));
}