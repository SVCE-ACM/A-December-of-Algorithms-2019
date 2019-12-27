// Input: 3
// Output: [ 'AAABBB', 'AABABB', 'AABBAB', 'ABAABB', 'ABABAB' ]
const input = process.argv[2];
if (!input) {
	console.log('no N is given');
	process.exit(1);
}


console.log(possibleCombinations(input, input));

function possibleCombinations(remainingA, remainingB) {
	let newArray = [];
	if (remainingA) {
		let tmpArray = possibleCombinations(remainingA-1, remainingB);
		newArray = prependToEach('A', tmpArray);
	}
	if (remainingB > remainingA) {
		let tmpArray = possibleCombinations(remainingA, remainingB-1);
		newArray = newArray.concat(prependToEach('B', tmpArray));
	}

	return newArray;
}

function prependToEach(prepend, array) {
	let newArray = array.slice();
	if (newArray.length === 0) return [prepend]; 
	newArray.forEach((element, index, theArray) => {
		theArray[index] = prepend + element;
	});
	return newArray;
}
