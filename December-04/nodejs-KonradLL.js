// Input: 6 '4,3,0,1,5,4,6'
// Output: 4
const input1 = process.argv[2];
const input2 = argsToArray(2);
if (!input1) {
	console.log('no N is given');
	process.exit(1);
} else if (!input2) {
	console.log('no citation array is given');
	process.exit(1);
}

console.log(calcIndexH(0, input2));


function calcIndexH(currHIndex, PaperCitations) {
	let amountOfSatisfyingPapers = 0;
	for (const citations in PaperCitations) {
		if (citations >= currHIndex) {
			amountOfSatisfyingPapers++;
		}
	}
	
	if (amountOfSatisfyingPapers >= currHIndex) {
		return calcIndexH(currHIndex+1, PaperCitations);
	} else {
		return currHIndex;
	}
}


function argsToArray(argPosition) {
	const ARGS_OFFSET = 1 //where the arguments start
	const arg = process.argv[argPosition + ARGS_OFFSET];
	let argsArr = arg.split(",");
	argsArr.forEach((item, index, theArray) => {
		theArray[index] = Number(item);
	});
	return argsArr;
}