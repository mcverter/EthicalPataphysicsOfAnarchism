const fs = require('fs');
const process = require('process');

let tiWordFile;
let otbWordFile; 

function exitOnError(message, err) {
    console.error(message, err)    
    process.exit(1);
}

fs.open(__dirname + '../data/TiWords.txt', 'r', (err, fd)=>{
    if (err) {
        exitOnError('could not open totality and infinity ', err)
    }
    tiWordFile = fd;
});

fs.open(__dirname + '../data/OTBWords.txt', 'r',(err, fd)=>{
    if (err) {
        exitOnError('could not open otb ', err)
    }
    otbWordFile = fd;
});

if (!tiWordFile || otbWordFile) {
    exitOnError('could not open book files ', '')
}