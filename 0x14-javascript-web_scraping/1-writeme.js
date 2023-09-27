#!/usr/bin/node
var fs = require('fs');
var filePath = process.argv[2];
var content = process.argv[3];

fs.writeFile(filePath, content, 'utf8', function(err) {
    if (err) {
        console.error(err);
    }
});
