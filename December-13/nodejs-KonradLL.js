// Input: 5
// Output: 
//-Iteration 0: 1->off  2->off  3->off  4->off  5->off
//-Iteration 1: 1->on   2->on   3->on   4->on   5->on
//-Iteration 2: 1->on   2->off  3->on   4->off  5->on
//-Iteration 3: 1->on   2->off  3->off  4->off  5->on
//-Iteration 4: 1->on   2->off  3->off  4->on   5->on
//-Iteration 5: 1->on   2->off  3->off  4->on   5->off
//-
//-No of switches in the 'on' state at the end: 2
const input = process.argv[2];
if (!input) {
	console.log('no amount of switches given');
	process.exit(1);
}

class SwitchList {
	constructor(amount) {
		this.amountOn = 0;
		this.switches = [];
		for (let i = 0; i < amount; i++) {
			this.switches.push(new Switch());
		}
	}

	setAllOn() {
		this.amountOn = this.switches.length; 
		for (let i = 0; i < this.switches.length; i++) {
			this.switches[i].setOn();
		}
	}

	toggleSwitch(index) {
		this.switches[index].toggle();
		if (this.switches[index].isOn()) {
			this.amountOn++;
		} else {
			this.amountOn--;
		}
	}

	getAmountOn() {
		return this.amountOn;
	}

	getAmountOfSwitches() {
		return this.switches.length;
	}

	printSwitchList(iteration) {
		let out = `Iteration ${iteration}:`
		for(const index in this.switches) {
			out += `  ${Number(index)+1}->${this.switches[index].stateToString()}`;
		}
		console.log(out);
	}
}

class Switch {
	constructor() {
		this._isOn = false;
	}

	setOn() {
		this._isOn = true;
	}

	setOff() {
		this._isOn = false;
	}

	toggle() {
		this._isOn = !this._isOn;
	}

	isOn() {
		return this._isOn;
	}

	stateToString() {
		return (this._isOn) ? 'On ' : 'Off';
	}
}

let switches = new SwitchList(input);
switches.printSwitchList(0);
let afterSwitches = roundOne(switches);
console.log(`\nNo of switches in the 'on' state at the end: ${afterSwitches.getAmountOn()}`);


function roundOne(switches) {
	switches.setAllOn();
	switches.printSwitchList(1);
	return roundN(2, switches);
}

function roundN(round, switches) {
	for(let index = round-1; index < switches.getAmountOfSwitches(); index += round) {
		switches.toggleSwitch(index);
	}

	switches.printSwitchList(round, switches)
	if (round < switches.getAmountOfSwitches()) {
		return roundN(round+1, switches);
	} else {
		return switches;
	}
}