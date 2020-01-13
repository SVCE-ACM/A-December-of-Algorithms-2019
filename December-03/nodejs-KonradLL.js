// Input: '10,43,3,86,34,86,4,32,9'
// Output: a sorted array, ex  [10, 43, 86]

const input = argsToArray(1);
if (!input) {
	console.log('no array is specified to sort');
	process.exit(1);
}

console.log(thanosSort(input));
process.exit(0);

function thanosSort(array) {
	while(!isSorted(array)) {
		array = snapArray(array);
	}
	return array;
}

function isSorted(array) {
	for (const index in array) {
		if (index == array.length-1){
			return true;
		} else if (array[index] > array[Number(index)+1]) {
			return false;
		}
	}
}

function snapArray(array) {
	const originalArrayLength = array.length;
	let index = 0;
	while(array.length > Math.ceil(originalArrayLength / 2)) {
		snapIndex(index, array);
		if(index === array.length-1) {
			index = 0;
		} else {
			index++;
		}
	}
	return array;
}

function snapIndex(index, array) {
	if(Math.random() < 0.5) {
		array.splice(index, 1);
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