const fs = require('fs');
const process = require('process');

let tiWordFile;
let otbWordFile; 

function exitOnError(message, err) {
    console.error(message, err)    
    process.exit(1);
}

const tiText = fs.readFileSync(__dirname + '/../data/TIWords.txt', 'utf-8');
const otbText = fs.readFileSync(__dirname + '/../data/OTBWords.txt', 'utf-8');

function countWords(filetext) {
    const wordMap = {};
    let totalWords = 0;

    const words = filetext.split(' ');
    words.forEach(w=>{
        w = w.toLowerCase();
        wordMap[w] = wordMap[w] ? wordMap[w] + 1 : 1;
        totalWords++;
    })
    const countedWords = Object.keys(wordMap).map(w=>[w, wordMap[w]]);

    console.log('There are ', totalWords, ' in book and ', countedWords.length , ' distinct words ')
    
    //console.log(wordMap);
}

countWords(tiText);
countWords(otbText);