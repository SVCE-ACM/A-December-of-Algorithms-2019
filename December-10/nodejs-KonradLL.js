// Input: 10 2 5
// Output: 6
const inputN = process.argv[2];
const inputP = process.argv[3];
const inputC = process.argv[4];

if (!inputN) {
	console.log('no money amount (N) is given');
	process.exit(1);
} else if (!inputP) {
	console.log('no jar cost (P) is given');
	process.exit(1);
} else if (!inputC) {
	console.log('no turnin amount (C) is given');
	process.exit(1);
}

const initialCookieJars = buyCookieJars(inputN, inputP);
const possibleCookies = initialCookieJars + calcAdditionalJars(initialCookieJars, inputC)[0];
console.log(possibleCookies);

function buyCookieJars(money, cost) {
	return money / cost;
}

function calcAdditionalJars(jars, turninAmount) {
	let returnArray = [0, jars];  // extraJars, leftoverjars
	if (jars < turninAmount) return returnArray;

	const leftoverJars = jars % turninAmount;
	let additionalJars = Math.floor(jars / turninAmount);
	additionalJars += calcAdditionalJars(additionalJars + leftoverJars, turninAmount)[0];
	
	return [additionalJars, leftoverJars];
}