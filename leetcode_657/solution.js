var judgeCircle = function(moves) {
    let x = 0, y = 0;
    [...moves].map((step) => {
        switch (step) {
            case "L": x -= 1; break;
            case "R": x += 1; break;
            case "U": y += 1; break;
            case "D": y -= 1; break;
        }
    });
    return (x === 0) && (y === 0);
};

function main () {
    moves = "UDDD";
    ret = judgeCircle(moves);
    console.log(ret);
}

main()