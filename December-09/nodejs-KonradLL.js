// Input:
//-Set 1: {1,2,3,4}
//-Set 2: {1,4,9,16}
//-Function: x^2
// Output:
//-Result: It is one-one and onto.
const standard_input = process.stdin;
standard_input.setEncoding("utf-8");
process.stdout.write("Set 1: ");

let input = 0;
let _set1, _set2, _func;
standard_input.on("data", function(data) {
	if (input === 0) {
		_set1 = setToArray(data);
		input++;
		process.stdout.write("Set 2: ");
	} else if (input === 1) {
		_set2 = setToArray(data);
		input++;
		process.stdout.write("Function: ");
	} else if (input === 2) {
		_func = data.replace(' ', '').replace(/(\n|\r)+$/, '').split('');
		_func.forEach((item, index, theArray) => {
			if(!isNaN(Number(item))) theArray[index] = Number(item); 
		});
		input++;
		checkFuncType(_set1, _set2, _func);
		process.exit(0);
	}
});

function setToArray(set) {
	let setArray = set
									.replace(/{|}/g, '')
									.replace(/(\n|\r)+$/, '')
									.split(',');
	setArray.forEach((item, index, theArray) => { 
		theArray[index] = Number(item); 
	});
	return setArray;
}

function checkFuncType(set1, set2, func) {
	let setsMap = populateSetsMap(set2.length);
	for (const setItem of set1) {
		let calculatedVal = calcFunc(func, setItem);
		let indexOfSet2 = set2.indexOf(calculatedVal);
		setsMap[indexOfSet2] += 1;
	};
	printResult(setsMap);
}

function populateSetsMap(length) {
	let setsMap = []
	for (let index = 0; index < length; index++) {
		setsMap[index] = 0;
	}
	return setsMap;
}

function calcFunc(func, param) { // + - * / ^
	let newFunc = checkSubFunc(func, param);

	let left = newFunc[0], right = newFunc[2];
	if (isNaN(left)) {
		left = param;
	} else if (isNaN(right)) {
		right = param;
	}
	
	let operator = newFunc[1];
	return computeFunc(left, right, operator)
}

function computeFunc(left, right, operator) {
	if (operator === '+') {
		return left + right; 
	} else if (operator === '-') {
		return left - right; 
	} else if (operator === '*') {
		return left * right; 
	} else if (operator === '/') {
		return left / right; 
	} else if (operator === '^') {
		return Math.pow(left, right); 
	} else {
		console.log(`unkown operator ${operator}`)
	}
}

function checkSubFunc(func, param) {
	let localFunc = func.slice();
	let index = 0;
	while (index < localFunc.length) {
		if (localFunc[index] === '(') {	
			const closingIndex = findClosingParnthesisIndex(index, localFunc);
			let subFunc = localFunc.splice(index, closingIndex+1);
			subFunc = subFunc.splice(1, subFunc.length-2);	
			localFunc.splice(index, 0, calcFunc(subFunc, param));
			index = closingIndex;
		}
		index++;
	}
	return localFunc;
}

function findClosingParnthesisIndex(openingIndex, array) {
	let indent = 1;
	for(let index = openingIndex+1; index < array.length; index++) {
		if (array[index] === '(') {
			indent++;
		} else if (array[index] === ')' && indent > 1) {
			indent--;
		} else if (array[index] === ')' && indent === 1) {
			return index;
		}
	}
}

function printResult(something) {
	const injective = isInjective(something);
	const surjective = isSurjective(something);
	let result;
	if (injective && surjective) {
		result = 'one-one and onto';
	} else if (injective) {
		result = 'only one-one';
	} else if (surjective) {
		result = 'only onto';
	} else {
		result = 'regular';
	}
	console.log(`Result: it is ${result}`);
}

function isInjective(setsMap) {
	for (const item of setsMap) {
		if (item > 1) return false;
	};
	return true;
}

function isSurjective(setsMap) {
	for (const item of setsMap) {
		if (item < 1) return false;
	};
	return true;
}