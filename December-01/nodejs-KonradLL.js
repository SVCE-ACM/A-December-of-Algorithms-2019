// Input: 10
// Output: 350
const input = Number(process.argv[2]);
if (!input) {
	console.log('Nth element is not specified');
	process.exit(1);
}

let sevenish = [];
let allNumbers = [];
console.log(sevenish_number(0, input));
process.exit(0);

function sevenish_number(power, target) {
	const newSevenish = Math.pow(7, power);
	allNumbers.push(newSevenish);

	if (sevenish.length >= 1) {
		arraySums(newSevenish, sevenish);
		if (allNumbers.length >= target) {
			return getNumber(target);
		}
	}

	sevenish.push(newSevenish);
	return sevenish_number(power + 1, target);
}

function arraySums(base, array) {
	for(let i = 0; i < array.length; i++) {
		let newNumber = base + array[i];
		allNumbers.push(newNumber);
		if (array[i+1]) arraySums(newNumber, array.slice(1));
	}
}

function getNumber(target) {
	let sorted = allNumbers.sort((a, b) => { 
		return a-b;
	});
	return sorted[target-1];
}

