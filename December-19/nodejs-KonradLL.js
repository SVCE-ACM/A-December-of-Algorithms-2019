// Input: {{0, 3}, {2, 2}, {1, 1}, {2, 1}, {1, 2},{3, 0}, {0, 0}, {3, 3}}
// Output: The outer limits are: {{0, 3}, {0, 0}, {3, 0}, {3, 3}}

function main() {
	const input = process.argv[2].replace(/ /g, '').slice(2, -2).split('},{');
	if (!input) {
		console.log('no piont set is given');
		process.exit(1);
	}

	let points = []
	input.forEach(pointStr => {
		let pointArr = pointStr.split(',');
		let point = new Point(Number(pointArr[0]), Number(pointArr[1]));
		points.push(point);
	});

	const outerPoints = convexHullPoints(points, points.length);
	let outerPointsStr = [];
	outerPoints.forEach(point => {
		outerPointsStr.push(point.toString());
	})
	console.log(`the outer limits are: {${outerPointsStr.join(', ')}}`);
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

function orientation(p, q, r) { 
  let value = (q.y - p.y) * (r.x - q.x) - 
  						(q.x - p.x) * (r.y - q.y); 

  if (value === 0) return 0; 
  return (value > 0) ? 1 : 2;
} 

function convexHullPoints(points, n) { 
	if (n < 3) return; 

	let hull = []; 

	l = 0; 
	for (let i = 1; i < n; i++) {
		if (points[i].x < points[l].x) {
			l = i; 
		}
	}

	let q, p = l; 
	do { 
		hull.push(points[p]);
 
		q = (p + 1) % n; 
		for (let i = 0; i < n; i++) { 
			if (orientation(points[p], points[i], points[q]) === 2) {
				q = i; 
			}
		} 

		p = q; 
	} while (p != l);

	return hull;
} 


main()