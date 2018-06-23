/**
 * @param {string[]} words
 * @return {number}
 */
var uniqueMorseRepresentations = function(words) {
    const codes = [
        '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', 
        '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..'
    ];
    const morseIndex = char => char.charCodeAt(0) - 'a'.charCodeAt(0);
    return new Set(words.map(
        word => [...word].map(char => codes[morseIndex(char)]).join('')
    )).size;
};

function main () {
    words = ["gin", "zen", "gig", "msg"];
    ret = uniqueMorseRepresentations(words);
    console.log(ret);
}

main()