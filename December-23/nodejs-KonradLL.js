// Input: {{3,4},{5,2},{6,7}}
// Output: Centroid: {4.666666666666667, 4.333333333333333}
function main() {
	const input = process.argv[2].replace(/ /g, '').slice(2, -2).split('},{');
	if (!input) {
		console.log('no piont set is given');
		process.exit(1);
	}

	let vertices = []
	input.forEach(pointStr => {
		let pointArr = pointStr.split(',');
		let point = new Point(Number(pointArr[0]), Number(pointArr[1]));
		vertices.push(point);
	});

	const centroid = getCentroid(vertices);
	console.log(`Centroid: ${centroid.toString()}`);
}

class Point {
	constructor(x, y) {
		this.x = x;
		this.y = y;
	}

	toString() {
		return `{${this.x}, ${this.y}}`;
	}
}

function getCentroid(vertices) {
	const centroid = new Point(0, 0);
	let signedArea = 0.0;
	let x0 = 0.0;
	let y0 = 0.0;
	let x1 = 0.0; 
	let y1 = 0.0;
	let a = 0.0;

	for (let i = 0; i < vertices.length; ++i) {
		x0 = vertices[i].x;
		y0 = vertices[i].y;
		x1 = vertices[(i+1) % vertices.length].x;
		y1 = vertices[(i+1) % vertices.length].y;
		a = x0*y1 - x1*y0;
		signedArea += a;
		centroid.x += (x0 + x1)*a;
		centroid.y += (y0 + y1)*a;
	}

	signedArea *= 0.5;
	centroid.x /= (6.0*signedArea);
	centroid.y /= (6.0*signedArea);

	return centroid;
}

main();