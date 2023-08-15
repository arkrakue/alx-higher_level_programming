#!/usr/bin/node

const val = parseInt(process.argv[2]);
if (isNaN(val)){
	console.log("Missing number of occurrences")
}

for (let x = 0; x < val; x++){
	console.log("C is fun");
}
