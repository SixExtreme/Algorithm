/**
 * @param {string} J
 * @param {string} S
 * @return {number}
 */
var numJewelsInStones = function(J, S) {
    return [...S].filter(s => J.includes(s)).length
};

function main () {
    J = "aA"
    S = "aAAbbbb"
    ret = numJewelsInStones(J, S)
    console.log(ret)
}

main()