// Input:  "CSE ECE CSE"  "ECE ECE CSE"
// Output: 
//0 0.225 0.2
//0.225 0.5 0.3
const input = argsToMatrix(2);
if (!input) {
	console.log('no arguments were given');
	process.exit(1);
}

const probabilityMatrix = checkExamineesCheatingProbability(input);
printProbabilityMatrix(probabilityMatrix);

function checkExamineesCheatingProbability(examineesMatrix) {
	let probabilities = [];
	for(let row = 0; row < examineesMatrix.length; row++) {
		probabilities.push([]);
		for (let column = 0; column < examineesMatrix[row].length; column++) {
			probabilities[row][column] = checkCheaterProbability(row, column, examineesMatrix);
		}
	}
	return probabilities;
}

function checkCheaterProbability(row, column, examineesMatrix) {
	let probability = 0;
	if (sameInFront(row, column, examineesMatrix)) probability += 0.3; 
	if (sameInBack(row, column, examineesMatrix)) probability += 0.2;
	if (sameToSide(row, column, examineesMatrix)) probability += 0.2;
	if (sameInDiagonal(row, column, examineesMatrix))	probability += 0.025;
	return probability;
}

function sameInFront(row, column, examineesMatrix) {
	if (!examineesMatrix[row-1]) return false;
	return examineesMatrix[row][column] === examineesMatrix[row-1][column];
}

function sameInBack(row, column, examineesMatrix) {
	if (!examineesMatrix[row+1]) return false;
	return examineesMatrix[row][column] === examineesMatrix[row+1][column];
}

function sameToSide(row, column, examineesMatrix) {
	const sameToLeft = examineesMatrix[row][column] === examineesMatrix[row][column-1];
	const sameToRight = examineesMatrix[row][column] === examineesMatrix[row][column+1];
	return sameToLeft || sameToRight;
}

function sameInDiagonal(row, column, examineesMatrix) {
	return sameInDiagonalBack(row, column, examineesMatrix)
		|| sameInDiagonalBack(row, column, examineesMatrix);
}

function sameInDiagonalFront(row, column, examineesMatrix) {
	if (!examineesMatrix[row-1]) return false;
	const sameInFrontRight = examineesMatrix[row][column] === examineesMatrix[row-1][column+1];
	const sameInFrontLeft = examineesMatrix[row][column] === examineesMatrix[row-1][column-1];
	return sameInFrontRight || sameInFrontLeft;
}

function sameInDiagonalBack(row, column, examineesMatrix) {
	if (!examineesMatrix[row+1]) return false;
	const sameInBackRight = examineesMatrix[row][column] === examineesMatrix[row+1][column+1];
	const sameInBackLeft = examineesMatrix[row][column] === examineesMatrix[row+1][column-1];
	return sameInBackRight || sameInBackLeft;
}

function argsToMatrix() {
	let args = process.argv.splice(2);
	let argsMatrix = [];
	args.forEach(item => {
		argsMatrix.push(item.split(' '));
	});
	return argsMatrix;
}

function printProbabilityMatrix(probabilityMatrix) {
	for (const row in probabilityMatrix) {
		for (const item of probabilityMatrix[row]) {
			process.stdout.write(`${item} `);
		}
		console.log();
	}
}