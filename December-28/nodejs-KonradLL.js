// Input: "1,1,0,1" "1,1,0,0" "0,0,1,0" "1,0,0,1"
// Output: 
//-Number of groups: 2
//-An assasin is present

const input = conncetrionsMatrixArg();
if (!input) {
	console.log('no matrix is given');
	process.exit(1);
}

let groups = getGroups(input);
console.log(`Number of groups: ${groups.length}`);

const assasinPresent = hasAssasin(groups);
console.log(`An assasin is ${assasinPresent ? '' : 'not '}present`);


function getGroups(matrix) {
	// groups is an array of sets, where each set is a connections group of nobles
	let groups = [];
	for (let noble = 0; noble < matrix.length; noble++) {
		if (!existsInGroup(noble, groups)) {
			groups.push(new Set([noble]));
		}
		
		//check nobles connections
		for (let connection = 0; connection < matrix[noble].length; connection++) {
			const haveConnection = matrix[noble][connection] ? true : false;
			if (!haveConnection) continue;
			let noblesGroup = getNoblesGroupIndex(noble, groups);
			groups[noblesGroup].add(connection);
		}
	}

	return groups;
}

function existsInGroup(noble, groups) {
	for(const group of groups) {
		if (group.has(noble)) {
			return true;
		}
	}
	return false;
}

function getNoblesGroupIndex(noble, groups) {
	for(const group in groups) {
		if (groups[group].has(noble)) {
			return group;
		}
	}
	return -1;
}

function hasAssasin(groups) {
	for(const group of groups) {
		if (group.size === 1) {
			return true;
		}
	}
	return false;
}

function conncetrionsMatrixArg() {
	const arg = process.argv.slice(2);
	for (const argRow in arg) {
		arg[argRow] = arg[argRow].split(',');
		arg[argRow].forEach((item, index, arrayRef) => {
			arrayRef[index] = Number(item);
		});
	}
	return arg;
}