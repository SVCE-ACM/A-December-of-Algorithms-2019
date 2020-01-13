// Input: "0,1,*,0,1P" "1,0,0,0P,*" "1,1,0P,*,1" "*,1P,0,1,0" "1P,0,0,0,*"
// Output: 
//- DISK 1 | DISK 2 | DISK 3 | DISK 4 | DISK 5 |
//-   0        1        0        0       1P
//-   1        0        0        0P      1
//-   1        1        0P       1       1
//-   0        1P       0        1       0
//-   1P       0        0        0       1  

function main() {
	const input = storageMatrixArg();
	if (!input) {
		console.log('no storage matrix is given');
		process.exit(1);
	} 

	let restoredStorage = restoreStorage(input);
	printStorage(restoredStorage);
}


function restoreStorage(storageMatrix) {
	let restoredMatrix = [];
	for (const matrixRow of storageMatrix) {
		let restoredRow = restoreStorageRow(matrixRow);
		restoredMatrix.push(restoredRow);
	}

	return restoredMatrix;
}

function restoreStorageRow(storageRow) {
	const [remainingRowValue ,partitionValue, corruptedIndex] = getStorageRowInfo(storageRow);

	if (remainingRowValue % 2 === partitionValue) {
		storageRow[corruptedIndex] = '0';
	} else {
		storageRow[corruptedIndex] = '1';
	}
	return storageRow;
}

function getStorageRowInfo(storageRow) {
	let partitionValue, corruptedIndex;
	let remainingRowValue = 0;
	for (const cell of storageRow) {
		if (!isNaN(Number(cell))) {
			remainingRowValue += Number(cell);
		} else if (/p|P/g.test(cell)) {
			partitionValue = Number(cell.match(/[0-9]+/g)[0]); 
		} else {
			corruptedIndex = storageRow.indexOf(cell);
		}
	}

	return [remainingRowValue ,partitionValue, corruptedIndex];
}

function printStorage(storageMatrix) {
	let storageHead = '';
	for (const index in storageMatrix) {
		storageHead += `DISK ${Number(index)+1} | `;
	}
	console.log(storageHead);

	for (const storageRow of storageMatrix) {
		let rowStr = '  ';
		for (const cell of storageRow) {
			rowStr += cell + (' '.repeat(9 - cell.length))
		}
		console.log(rowStr);
	}
}

function storageMatrixArg() {
	const args = process.argv.slice(2);
	for (const argInd in args) {
		args[argInd] = args[argInd].split(',');
	}
	return args;
}

main();