// Input: "B,B,B, R, B,B"
// Output: 1 1 3 2 1 1
const inputBalls = process.argv[2].replace(/ /g, '').split(',');
if (!inputBalls) {
	console.log('no balls list is given');
	process.exit(1);
}

let firstBall = inputBalls.splice(0, 1)[0];
let alternatingBalls = alternatingLengths(firstBall, inputBalls);
console.log(alternatingBalls.join(' '));


function alternatingLengths(ball, remainingBalls) {
	let lastBall = ball;
	let length = [1];
	for (const nextBall of remainingBalls) {
		if (lastBall === nextBall) break;
		lastBall = nextBall;
		length[0]++;
	}

	if (remainingBalls.length > 0) {
		let nextBall = remainingBalls.splice(0, 1)[0];
		length = length.concat(alternatingLengths(nextBall, remainingBalls));
	}

	return length;
}