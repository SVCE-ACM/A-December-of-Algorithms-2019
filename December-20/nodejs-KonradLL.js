// Input: "X,A, B, C, D" "A, 0km, 40km, 10km, 30km" "B, 40km, 0km, 20km, 10km" "C, 10km, 20km, 0km, 50km" "D, 30km, 10km, 50km, 0km"
// Output: The shortest distance is: 70

function main() {
	const input = cityMatrixArg();
	if (!input) {
		console.log('no city matrix is given');
		process.exit(1);
	}

	const distances = new DistanceMatrix(input);
	let citiesToVisit = distances.getCities();
	let startingCity = citiesToVisit.splice(0,1)[0];

	const shortestDistance = getShortestDistance(startingCity, citiesToVisit, distances);
	console.log(`The shortest distane is: ${shortestDistance}`)

}

class DistanceMatrix {
	constructor(matrix) {
		this.matrix = matrix;
	}

	getDistance(start, destination) {
		const startingIndex = this.matrix[0].indexOf(start);
		const destinationIndex = this.matrix[0].indexOf(destination);
		return this.matrix[startingIndex][destinationIndex];
	}

	getCities() {
		return this.matrix[0].slice(1);
	}
}


function getShortestDistance(startCity, citiesLeft, distances) {
	let shortestDistance;
	for (const destCityIndex in citiesLeft) {
		let destCity = citiesLeft[destCityIndex];
		let distance = distances.getDistance(startCity, destCity);
		
		if (citiesLeft.length > 1) { // if this isn't the last city, get the shortest distance to the next city
			let newCitiesLeft = citiesLeft.filter(city => {
				return city !== destCity;
			});
			distance += getShortestDistance(destCity, newCitiesLeft, distances);
		} else {
			distance += distances.getDistance(destCity, distances.getCities().splice(0,1)[0]); //add first city
		}

		if (!shortestDistance || shortestDistance > distance) {
			shortestDistance = distance;
		}
	}

	return shortestDistance;
}


function cityMatrixArg() {
	const arg = process.argv.slice(2);
	arg[0] = arg[0].split(',');
	for (let i = 1; i < arg.length; i++) {
		arg[i] = arg[i].split(',');
		for (let j = 1; j < arg[i].length; j++) {
			let distance = arg[i][j].match(/[0-9]+/g)[0];
			arg[i][j] = Number(distance);
		}
	}
	return arg;
}

main();