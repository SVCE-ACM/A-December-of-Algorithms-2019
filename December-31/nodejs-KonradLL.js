// Input: /path/to/visualization/output.png (optional, leave blank for no visualization)
// Output: 
//-Store 1: 4.864857142857142,5.036000000000001
//-Store 2: 0.9666666666666667,-0.195
//-Store 3: -4.54057142857143,-5.086571428571428

const fs = require('fs');
const kmeans = require('node-kmeans');	// npm install node-kmeans
const ChartjsNode = require('chartjs-node'); //npm install chart.js canvas jsdom chartjs-node
// (the above might give errors which requires the following as a fix) 
// sudo apt-get update && sudo apt-get install libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-essential g++

function main() {
	const input = process.argv[2];

	let buildings = getBuildings();
	kmeans.clusterize(buildings, {k: 3}, (err,res) => {
		if (err) console.error(err);

		res.forEach((cluster, index) => {
			console.log(`Store ${index+1}: ${cluster.centroid}`);
		});

		if (input) vizualizeData(res, input);
	});
}

function vizualizeData(clusters, outFilePath) {
	let buildingsDataSets = [];
	let marketPoints = []; 

	let buildingColors = ["rgb(250, 0, 0)", "rgb(0, 250, 0)", "rgb(0, 0, 250)"];
	clusters.forEach((cluster, index) => {
		let data = [];
		cluster.cluster.forEach(building => {
			data.push({
				x: building[0],
				y: building[1]
			});
		})

		buildingsDataSets.push({
			label: `Cluster: ${index+1}`,
			backgroundColor: buildingColors[index],
			data: data,
		});

		marketPoints.push({
			x: cluster.centroid[0],
			y: cluster.centroid[1]
		});
	});

		
	let storesSet = [{
		label: 'Stores',
		backgroundColor: "rgb(255,215,0)",
		data: marketPoints
	}];
	
	let dataSets = storesSet.concat(buildingsDataSets);

	let chartJsOptions = {
		type: 'scatter',
		data: {
			datasets: dataSets,
		},
		options: {
			scales: {
				xAxes: [{
					type: 'linear',
					position: 'bottom'
				}]
			}
		}
	}

	const chartNode = new ChartjsNode(600, 600);
	chartNode.drawChart(chartJsOptions)
	.then(() => {
			return chartNode.getImageBuffer('image/png');
	})
	.then(buffer => {
			return chartNode.getImageStream('image/png');
	})
	.then(streamResult => {
			return chartNode.writeImageToFile('image/png', outFilePath);
	});
}

function getBuildings() {
	let csvFile = fs.readFileSync(__dirname + '/../src/res/build_city_csv.csv').toString().replace(/\r/g, '');
	let csvLst = csvFile.split('\n')
	
	let buildings = [];
	csvLst.forEach(line => {
		let buildintPoints = line.split(',');
		let pointX = parseFloat(buildintPoints[0]);
		let pointY = parseFloat(buildintPoints[1]);
		if (!isNaN(pointX) && !isNaN(pointY)) {
			buildings.push([pointX, pointY]);
		}
	});

	return buildings;
}


main();