/**
 * @param {number[]} A
 * @return {number}
 */
var peakIndexInMountainArray = function(A) {
    let l = 0, r = A.length - 1;
    while (l < r) {
        let mid = Math.floor((l + r) / 2);
        if (A[mid] < A[mid + 1]) {
            l = mid;
        } else if (A[mid] < A[mid - 1]) {
            r = mid;
        } else {
            return mid;
        }
    }
};

function main () {
    let A = [0, 1, 0];
    let ret = peakIndexInMountainArray(A);
    console.log(ret);
}

main()