// Input:  "1 2 3 4" "5 6 7 8" "9 10 11 12" "13 14 15 16"
// Output: "1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10"

const input = studentMatrixArg();
if (!input) {
	console.log('no student matrix was given');
	process.exit(1);
}

let studentSpiral = topSpiral(input);
console.log(studentSpiral.join(' '));


function topSpiral(studentsMatrix) {
	let topRow = studentsMatrix.splice(0,1)[0];

	if (studentsMatrix.length <= 0) return topRow;
	else return topRow.concat(rightSpiral(studentsMatrix));
}

function rightSpiral(studentsMatrix) {
	//if last row, do bottom
	if (studentsMatrix.length <= 1) {
		return bottomSpiral(studentsMatrix);
	}

	let rightColumn = [];
	for (const studentRow of studentsMatrix) {
		rightColumn.push(studentRow.splice(-1, 1)[0]);
	}

	return rightColumn.concat(bottomSpiral(studentsMatrix));
}

function bottomSpiral(studentsMatrix) {
	let bottomRow = studentsMatrix.splice(-1, 1)[0];
	let bottomRowReverse = bottomRow.reverse();

	if (studentsMatrix.length <= 0) return bottomRowReverse;
	else return bottomRowReverse.concat(leftSpiral(studentsMatrix));
}

function leftSpiral(studentsMatrix) {
	if (studentsMatrix.length <= 1) {
		return topSpiral(studentsMatrix);
	}

	let leftColumnReverse = [];
	for (let index = studentsMatrix.length-1; index >= 0; index--) {
		leftColumnReverse.push(studentsMatrix[index].splice(0,1)[0]);
	}

	return leftColumnReverse.concat(topSpiral(studentsMatrix));

}

function studentMatrixArg() {
	const arg = process.argv.slice(2);
	for (const argRow in arg) {
		arg[argRow] = arg[argRow].split(' '); 
	}
	return arg;
}