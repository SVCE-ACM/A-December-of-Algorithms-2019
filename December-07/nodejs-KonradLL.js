// Input:
//-Enter N: 5
//-Enter (token no, id):
//(1, a)
//(2, b)
//(3, c)
//(4, d)
//(5, e)
//-Enter k: c
// Output:
//-The order is:
//(3, c)
//(1, a)
//(2, b)
//(4, d)
//(5, e)

class Queue {
	constructor() {
		this.queue = [];
	}

	enqueue(item) {
		this.queue.push(item);
	}

	dequeue() {
		return this.queue.splice(0,1)[0];
	}

	isEmpty() {
		return this.queue.length === 0;
	}
}

const standard_input = process.stdin;
standard_input.setEncoding("utf-8");
process.stdout.write("Enter N: ");

let input = 0;
let queueLength;
let originalQueue = new Queue();
standard_input.on("data", function(data) {
	if (input === 0) {
		queueLength = Number(data);
		input++;
		console.log("Enter (token no, id):");
	} else if (input > 0 && input < queueLength) {
		originalQueue.enqueue(data.replace(/(\n|\r)+$/, ''));
		input++;
	} else if (input === queueLength) {
		originalQueue.enqueue(data.replace(/(\n|\r)+$/, ''));
		input++;
		process.stdout.write("Enter k: ");
	} else {
		cutLine(data.replace(/(\n|\r)+$/, ''));
		process.exit(0);
	}
});

function cutLine(cutterId) {
	let tmpQueue = new Queue();
	let newQueue = new Queue();
	while(!originalQueue.isEmpty()) {
		const item = originalQueue.dequeue();
		if (item.includes(cutterId)) {
			newQueue.enqueue(item);
		} else {
			tmpQueue.enqueue(item);
		}
	}

	while(!tmpQueue.isEmpty()) {
		let item = tmpQueue.dequeue();
		newQueue.enqueue(item);
	}

	printQueue(newQueue);
}


function printQueue(queue) {
	console.log('The order is:');
	while(!queue.isEmpty()) {
		console.log(queue.dequeue());
	}
}

