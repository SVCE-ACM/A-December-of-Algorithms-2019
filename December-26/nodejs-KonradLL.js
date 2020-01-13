// Input: "1, 2, 6, 3, 1"
// Output: "Operations needed: 4"
function main() {
	const input = process.argv[2].replace(/ /g, '').split(',');
	if (!input) {
		console.log('no compartments list is given');
		process.exit(1);
	}

	input.forEach((item, index, theArray) => {
		theArray[index] = Number(item);
	})

	let minimumOperations;
	if (input.length % 2 === 0) { //array has no center
		let center1 = smallestOperation((input.length/2)-1, input);
		let center2 = smallestOperation(input.length/2, input);
		minimumOperations = Math.min(center1, center2);
	} else {
		minimumOperations = smallestOperation(Math.floor(input.length/2), input);
	}

	console.log(`Operations needed: ${minimumOperations}`);
}

function smallestOperation(centerInd, compartmentsLst) {
	let operations = 0;
	// calc Center element
	const sizeOfCenter = Math.ceil(compartmentsLst.length/2);
	operations += compartmentsLst[centerInd] - sizeOfCenter;

	
	//calc Left elements
	let neededSizeOfCompartment = sizeOfCenter - 1
	for (let index = centerInd-1; index >= 0; index--) {
		operations += compartmentsLst[index] - neededSizeOfCompartment;
		neededSizeOfCompartment--;
	}

	//calc Right elements
	neededSizeOfCompartment = sizeOfCenter - 1
	for (let index = centerInd+1; index < compartmentsLst.length; index++) {
		operations += compartmentsLst[index] - neededSizeOfCompartment;
		neededSizeOfCompartment--;
	}

	return operations;
}



main();