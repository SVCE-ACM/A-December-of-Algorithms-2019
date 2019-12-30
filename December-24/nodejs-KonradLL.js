// Input: "54, 65, 44, 65, 44, 89, 44, 89, 54, 89"
// Output: "The circular doubly linked list: 54 65 44 89"
function main() {
	const input = process.argv[2].replace(/ /g, '').split(',');
	if (!input) {
		console.log('no N is given');
		process.exit(1);
	}

	const linkedList = parseCircularDoublyLinkedList(input);
	console.log(`The circular doubly linked list: ${linkedList.toString()}`);
}

class DoublyNode {
	constructor(value) {
		this.value = value
		this.prev;
		this.next;
	}
}

class CircularDoublyLinkedList {
	constructor() {
		this.first;
		this.last;
	}

	getAndAddNode(value) {
		const newNode = new DoublyNode(value);

		if(!this.first) {
			this.first = newNode;
			this.last = newNode;
		} else {
			newNode.prev = this.last;
			this.last.next =newNode;

			newNode.next = this.first;
			this.first.prev = newNode;
		}

		this.last = newNode;
		return newNode;
	}

	toString() {
		let string = this.first.value;
		let nextNode = this.first.next;
		while (nextNode !== this.first) {
			string += ` ${nextNode.value}`
			nextNode = nextNode.next;
		}

		return string;
	}
}

function parseCircularDoublyLinkedList(valueLst) {
	const linkedList = new CircularDoublyLinkedList();
	let currNode = linkedList.getAndAddNode(valueLst.splice(0, 1)[0]);
	for (const value of valueLst) {
		// if value isn't linked to currNode, add new node to list
		if (currNode.next && value === currNode.next.value) {
			currNode = currNode.next;
		} else if (currNode.prev && value === currNode.prev.value) {
			currNode = currNode.prev;
		} else {
			currNode = linkedList.getAndAddNode(value);
		}
	}

	return linkedList;
}


main();