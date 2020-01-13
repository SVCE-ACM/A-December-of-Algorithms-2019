// Input: "[ ['S','A',1], ['S','B',5], ['S','C',20], ['A','C',15], ['B','C',10] ]"
// Output: Lowest cost: 16
const input = process.argv[2].replace(/ /g, '').slice(2, -2).split('],[');
if (!input) {
	console.log('no N is given');
	process.exit(1);
}

let vertices = new Set();
input.forEach((item, index, arrayRef) => {
	arrayRef[index] = item.replace(/'/g, '').split(',');

	vertices.add(arrayRef[index][0]);
	vertices.add(arrayRef[index][1]);
	arrayRef[index][2] = Number(arrayRef[index][2]); 
});
vertices.delete('S');

let lowestEdges = new Set();

vertices.forEach(vertice => {
	let lowEdges = shortestPath('S', vertice, input);
	lowEdges.forEach(edge => {
		lowestEdges.add(edge);
	});
});

let cost = 0;
lowestEdges.forEach(edge => {
	cost += edge[2];
});
console.log(`Lowest cost: ${cost}`);


// edge is [ <vertice1>, <vertice2>, <cost>]
function shortestPath(startVertice, destinationVertice, edges) {
	let shortestEdges = [[]];
	let shortestDistance = Infinity;
	for (const edgeIndx in edges) {
		if (!(edges[edgeIndx][0] === startVertice || edges[edgeIndx][1] === startVertice)) {
			continue;
		}

		let shortDistance = edges[edgeIndx][2];
		let shortEdges = [edges[edgeIndx]];

		if (!(edges[edgeIndx][0] === destinationVertice || edges[edgeIndx][1] === destinationVertice)) {
			let toVertice = edges[edgeIndx][0] === startVertice ? edges[edgeIndx][1] : edges[edgeIndx][0];
			let newEdges = edges.slice();
			newEdges.splice(edgeIndx, 1);

			let tmpEdges = shortestPath(toVertice, destinationVertice, newEdges);
			shortDistance += getDistance(tmpEdges);
			shortEdges = shortEdges.concat(tmpEdges);
		}

		if (shortDistance < shortestDistance) { 
			shortestEdges = shortEdges;
			shortestDistance = shortDistance;
		}
	}

	return shortestEdges;
}

function getDistance(edges) {
	let distance = 0;
	edges.forEach(edge => {
		distance += edge[2];
	})
	return distance;
}