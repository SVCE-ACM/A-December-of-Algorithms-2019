// Input: monkey
// Output: The winner is B with 14 pts
const input = process.argv[2];
if (!input) {
	console.log('no word is given');
	process.exit(1);
}

class wordplayScoreboard {
	constructor() {
		this.subStrings = {};
	}

	addSubstring(subString) {
		this.subStrings[subString] = this.subStrings[subString] + 1 || 1;
	} 

	getScore() {
		let score = 0;
		for (const subString in this.subStrings) {
			if (this.subStrings.hasOwnProperty(subString)) {
				score += this.subStrings[subString];				
			}
		}
		return score;
	}
}

const VOWELS = ['a', 'e', 'i', 'o', 'u'];
const CONSTANTS = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'];

const scoreA = wordplay(input, VOWELS);
const scoreB = wordplay(input, CONSTANTS);

if (scoreA > scoreB) {
	console.log(`The winner is A with ${scoreA} pts`);
} else if (scoreB > scoreA) {
	console.log(`The winner is B with ${scoreB} pts`);
} else {
	console.log(`The result is a draw with ${scoreA} pts`);
}

function wordplay(word, startingCharacters) {
	let scoreboard = new wordplayScoreboard();
	for (const letterI in word) {
		if (!startingCharacters.includes(word[letterI])) continue;
		let subString = '';
		for (let i = letterI; i < word.length; i++) {
			subString += word[i];
			scoreboard.addSubstring(subString);
		}
	}
	return scoreboard.getScore();
}

