// Input : 49927398716
// Output: 49927398716 passes the test
const input = Number(process.argv[2]);
if (!input) {
	console.log('no credit card number was given');
	process.exit(1);
}

let cardIsValid = validateCardNumber(input)
console.log(`${input} ${(cardIsValid) ? 'passed' : 'failed'} the test`);
process.exit(0);

/* Functions */

function validateCardNumber(cardNumber) {
	let reverseNumberArr = reverseNumber(cardNumber);
	const s1 = getS1(reverseNumberArr);
	const s2 = getS2(reverseNumberArr);
	const res = String(s1 + s2);
	return (res[1] === "0") ? true : false;  // or: % 10
}

function getS1(arr) {
	let result = 0;
	for (const i in arr) {
		if (i % 2 === 0) {
			result += arr[i];
		}
	}
	return Number(result);
}

function getS2(arr) {
	let result = 0;
	for (const i in arr) {
		if (i % 2 !== 0) {
			let tmp = arr[i] * 2;
			if (tmp > 9) tmp = tmp - 9;
			result += tmp;
		}
	}
	return result;
}

function reverseNumber(number) {
	let numberArr = String(number).split("");
	let reverseNumberArr = numberArr.reverse();
	reverseNumberArr.forEach((item, index, theArray) => {
		theArray[index] = Number(item);
	});
	return reverseNumberArr;
}