// Input: "Park, Central, Beach, Mylapore, Kilpauk" "Central,T.Nagar,Washerampet, MKB Nagar" Park T.Nagar
// Output: Fastest path: Park -> Central -> T.Nagar
function main() {
	const input1 = process.argv[2].replace(/ /g, '').split(','); //TODO to arr
	const input2 = process.argv[3].replace(/ /g, '').split(',');
	const input3 = process.argv[4];
	const input4 = process.argv[5];

	if (!input1) {
		console.log('railwayline 1 is not given');
		process.exit(1);
	} else if (!input2) {
		console.log('railwayline 2 is not given');
		process.exit(1);
	} else if (!input3) {
		console.log('starting station is not given');
		process.exit(1);
	} else if (!input4) {
		console.log('destination station is not given');
		process.exit(1);
	}

	const railway = new Railway();
	railway.addRailwayLine(input1);
	railway.addRailwayLine(input2);
	const startStation = railway.getStation(input3);
	const destinationStation = railway.getStation(input4);
	const path = new RailwayPath(startStation);
	const shortestPath = getShortestPath(startStation, destinationStation, path);
	console.log(`Fastest path: ${shortestPath.toString()}`);
}

class Station {
	constructor(name) {
		this.name = name;
		this.adjecentStations = [];
	}

	addAdjecentStation(station) {
		if (!(this.adjecentStations.indexOf(station) + 1)) {
			this.adjecentStations.push(station);
		}
	}

	getAdjecentStation() {
		return this.adjecentStations;
	}

	getName() {
		return this.name;
	}
}

class Railway {
	constructor() {
		this.stations = [];
	}

	addRailwayLine(line) {
		// add each individual station
		for (let stationIndex = 0; stationIndex < line.length; stationIndex++) {
			let station = this.getOrCreateStation(line[stationIndex]);

			//add adjecents
			if (line[stationIndex-1]) {
				let adjecentStation = this.getOrCreateStation(line[stationIndex-1]);
				station.addAdjecentStation(adjecentStation);
			}

			if (line[stationIndex+1]) {
				let adjecentStation = this.getOrCreateStation(line[stationIndex+1]);
				station.addAdjecentStation(adjecentStation);
			}
		}
	}

	getOrCreateStation(stationName) {
		let station = this.getStation(stationName);
		if (!station) {
			station = new Station(stationName);
			this.stations.push(station);
		}
		return station;
	}

	getStation(stationName) {
		for(const station of this.stations) {
			if (station.getName() === stationName) return station;
		}
		return false;
	}
}

class RailwayPath {
	constructor(startStation) {
		this.length = 1;
		this.stations = [startStation];
	}

	addToPath(station) {
		this.length++;
		this.stations.push(station);
	}

	containsStation(station) {
		return this.stations.indexOf(station)+1 ? true : false;
	}

	toString() {
		let out = this.stations[0].getName();
		for(let i = 1; i < this.stations.length; i++) {
			out += ` -> ${this.stations[i].getName()}`
		}
		return out;
	}
}

function getShortestPath(station, destination, currPath) {
	let adjecentStations = station.getAdjecentStation();

	let fastestPath;
	for (const adjecentStation of adjecentStations) {
		if (currPath.containsStation(adjecentStation)) continue;

		let newPath = copyObj(currPath, true);
		newPath.addToPath(adjecentStation);
		
		if (adjecentStation !== destination) {
			newPath = getShortestPath(adjecentStation, destination, newPath);
		}

		//if newpath is sorter than other path and contains the destinationx
		if ((!fastestPath || (newPath && newPath.length < fastestPath.length))
			&& (newPath && newPath.containsStation(destination))) {
			fastestPath = newPath;
			break;
		}
	}
	
	return fastestPath;
}

//used to deep copy a circural object
function copyObj(source, deep) {
	var o, prop, type;

 if (typeof source != 'object' || source === null) {
	 // What do to with functions, throw an error?
	 o = source;
	 return o;
 }

 o = new source.constructor();

 for (prop in source) {

	 if (source.hasOwnProperty(prop)) {
		 type = typeof source[prop];

		 if (deep && type == 'object' && source[prop] !== null) {
			 o[prop] = copyObj(source[prop]);

		 } else {
			 o[prop] = source[prop];
		 }
	 }
 }
 return o;
}


main();