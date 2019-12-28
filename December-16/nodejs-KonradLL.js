// Input: 2h  3h  2d  3c  3d
// Output: full-house

function main() {
	const input = process.argv.slice(2);
	if (!input || input.length < 5) {
		console.log('no valid poker hand is given is given');
		process.exit(1);
	}
	
	const hand = new Hand(input);
	console.log(hand.getHandCategory())
}


class Card {
	constructor(cardStr) {
		this.kind = cardStr[cardStr.length-1];

		let cardRank = cardStr.slice(0, cardStr.length-1);
		if (!isNaN(cardRank)) {
			this.rank = Number(cardRank);
		} else {
			if(cardRank === 'a') {
				this.rank = 14;
			} else if(cardRank === 'j') {
				this.rank = 11;
			} else if(cardRank === 'q') {
				this.rank = 12;
			} else if(cardRank === 'k') {
				this.rank = 13;
			}
		}
	}
}

class Hand {
	constructor(cardStrArr) {
		this.cardArr = [];
		for (const cardStr of cardStrArr) {
			this.cardArr.push(new Card(cardStr));
		}
		this.cardArr.sort((cardA, cardB) => {
			return cardB.rank - cardA.rank;
		})

		this.isStraight = handIsStraight(this.cardArr);
		this.isFlush = handIsFlush(this.cardArr);
		this.numberOfRanks = numberOfRanksInHand(this.cardArr);
		this.highestOfSameRankInHand = highestOfSameRankInHand(this.cardArr);
	}

	getHandCategory() {
		if (this.isStraight && this.isFlush) {
			return 'straight-flush'; 
		} else if (this.highestOfSameRankInHand === 4) {
			return 'four-of-a-kind';
		} else if (this.highestOfSameRankInHand === 3 && this.numberOfRanks === 2) {
			return 'full-house';
		} else if (this.isFlush) {
			return 'flush';
		} else if (this.isStraight) {
			return 'straight';
		} else if (this.highestOfSameRankInHand === 3) {
			return 'three-of-a-kind';
		} else if (this.numberOfRanks === 3) {
			return 'two-pair';
		} else if (this.numberOfRanks === 4) {
			return 'one-pair';
		} else {
			return 'high-card';
		}
	}
}

function handIsFlush(cards) {
	let firstKind = cards[0].kind;
	for (let index = 1; index < cards.length; index++) {
		if (firstKind !== cards[index].kind) return false
	}
	return true;
}

function handIsStraight(cards) {
	let prevRank = cards[0].rank;
	for (let index = 1; index < cards.length; index++) {
		if (prevRank !== cards[index].rank+1) return false;
		else prevRank = cards[index].rank;
	}
	return true;
}

function numberOfRanksInHand(cards) {
	let ranks = {};
	for (let index = 0; index < cards.length; index++) {
		const cardRank = cards[index].rank;
		ranks[cardRank] = 1;
	}
	return Object.keys(ranks).length;
}

function highestOfSameRankInHand(cards) {
	let ranks = {};
	for (let index = 0; index < cards.length; index++) {
		const cardKind = cards[index].rank;
		ranks[cardKind] = ranks[cardKind] + 1 || 1;
	}

	let highest = 0;
	for (const rank in ranks) {
		if (ranks.hasOwnProperty(rank)) {
			if (highest < ranks[rank]) highest = ranks[rank];			
		}
	}
	return highest;
}


main();