// Input:
//-Enter the value for (n): 5
// Output:
//-Generated Fibonacci Prime Number Generation upto (5): 
//-2, 3, 5, 13, 89


let fibonachiNumbers = [1, 1];
let fiboPrimes = [];

const standard_input = process.stdin;
standard_input.setEncoding("utf-8");
process.stdout.write("Enter the value for (n): ");
standard_input.on("data", function(data) {
	if (isNaN(Number(data))) {
		console.log("invalid number is given");
		process.exit(1);
	} else {
		getFiboPrime(Number(data));
		process.exit(0);
	}
});

function getFiboPrime(limit) {
	let lastFibo = 2;
	let lastPrime = 2;
	while (fiboPrimes.length < limit) {
		if (lastFibo < lastPrime) {
			lastFibo = getNextFibonachi(lastFibo);
		} else if (lastFibo > lastPrime) {
			lastPrime = getNextPrime(lastPrime);
		} else {
			fiboPrimes.push(lastPrime);
			lastFibo = getNextFibonachi(lastFibo);
			lastPrime = getNextPrime(lastPrime);
		}
	}
	return printQueue(fiboPrimes);
}

function getNextFibonachi() {
	const lastFibo = fibonachiNumbers[fibonachiNumbers.length - 1];
	const secondLastFibo = fibonachiNumbers[fibonachiNumbers.length - 2];
	const newFibo = secondLastFibo + lastFibo;

	fibonachiNumbers.push(newFibo);
	return newFibo;
}

function getNextPrime(lastPrime) {
	if (lastPrime > 2) {
		var i, q;
		do {
			i = 3;
			lastPrime += 2;
			q = Math.floor(Math.sqrt(lastPrime));
			while (i <= q && lastPrime % i) {
				i += 2;
			}
		} while (i <= q);
		return lastPrime;
	}
	return lastPrime === 2 ? 3 : 2;
}

function printQueue(numbers) {
	let output = '';
	for (const fiboPrime of numbers) {
		output += fiboPrime + ', ';
	}
	console.log(`\nGenerated Fibonacci Prime Number Generation upto (${numbers.length}):`)
	console.log(output.slice(0, -2));
}