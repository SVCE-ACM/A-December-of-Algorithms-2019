// Input: "147,149,149,155,150" 2
// Output: Number of pairs: 2

function main() {
	const inputStudents = process.argv[2].replace(/ /g, '').split(',');
	const inputDifference = Number(process.argv[3]);
	if (!inputStudents) {
		console.log('no student group is given');
		process.exit(1);
	} else if (!inputDifference) {
		console.log('no maximum height difference is given');
		process.exit(1);


	}

	inputStudents.forEach((studentHeight, index, theArray) => {
		theArray[index] = Number(studentHeight);
	});

	inputStudents.sort((studentA, studentB) => {
		return studentA - studentB;
	});

	const pairs = getPairs(inputStudents, inputDifference);
	const numberOfPairs = pairs.length;
	console.log(`Number of pairs: ${numberOfPairs}`);
}

function getPairs(students, maxHeightDiffernece) {
	const pairs = [];
	let index1 = 0;
	while (index1 < students.length) {
		let firstStudent = students[index1];

		for (let index2 = index1+1; index2 < students.length; index2++) {
			index1 = index2;
			let secondStudent = students[index2];
			if (firstStudent - secondStudent <= maxHeightDiffernece) {
				index1++;
				pairs.push(`${firstStudent}&${secondStudent}`);
				break;
			}
		}
	}

	return pairs;
}

main();