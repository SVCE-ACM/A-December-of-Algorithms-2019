// Input: jane.austen_691@dnarifle.com
// Output: jane.austen_691@dnarifle.com is a valid email address
const input = process.argv[2];
if (!input) {
	console.log('no email adress to validate is given');
	process.exit(1);
}

let emailRegex = /^[a-zA-Z0-9\-_\.]+@[a-zA-Z]+\.com$/g;
let isValid = emailRegex.test(input);
console.log(`${input} is${(isValid) ? '' : ' not'} a valid email address`);