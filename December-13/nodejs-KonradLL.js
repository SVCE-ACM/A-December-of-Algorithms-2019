// Input: 5
// Output: 
//-No of switches in the 'on' state at the end: 2
//-Switches that are on are: 1, 4
const input = process.argv[2];
if (!input) {
	console.log('no amount of switches given');
	process.exit(1);
}

const switchesInOnState = switchesOn(input);
console.log(`No of switches in the 'on' state at the end: ${switchesInOnState.length}`);
console.log(`Switches that are on are: ${switchesInOnState.join(', ')}`);

// O(n)
function switchesOn(numberOfSwitches) {
	let on = []
	for (let theSwitch = 1; theSwitch <= numberOfSwitches; theSwitch++) {
		if (isOn(theSwitch)) on.push(theSwitch);
	}
	return on
}

// O(1)
function isOn(theSwitch) {
	return Math.sqrt(theSwitch) % 1 === 0;
}