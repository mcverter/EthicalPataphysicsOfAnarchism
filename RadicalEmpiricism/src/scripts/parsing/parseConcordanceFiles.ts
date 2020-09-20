const fs = require("fs");
const readline = require("readline");
var JSSoup = require('jssoup').default;

const frenchConcordanceReadLine = readline.createInterface({
  input: fs.createReadStream(
    __dirname + "/../../data/Concordance/Sections/French.txt"
  ),
//  output: process.stdout,
  console: false,
});

function exitOnError(message, err) {
  console.error(message, err);
  process.exit(1);
}
let lineCount = 0;
const allWords = {};

frenchConcordanceReadLine.on("line", (line) => {
  lineCount++;
  let wordMatch, word, bookMatch, citationCount, bookName;
  const WordRegex = /(\w+):(.+)./;
  const BookRegex = /(\w\w)(.+);/g;

  wordMatch = WordRegex.exec(line);
  word = wordMatch[1];
  console.log('word', word);

  allWords[word] = {};
  wordMatch[2].split(";").forEach((book) => {
    bookName = book.match(/\w+/)[0];
    citationCount = 1 + (book.indexOf(",") > -1 ? book.match(/,/g).length : 0);
    allWords[word][bookName] = citationCount;
  });
});

function getMorphology(word) {}
// oikos nomos 

function getDefinition(word) {}

function getEtymology(word) {}

frenchConcordanceReadLine.on("close", () => {
//    console.log(JSON.stringify(allWords));  
  console.log("me voici");
  fs.writeFileSync(__dirname +'/output.min.json', JSON.stringify(allWords));
  fs.writeFileSync(__dirname + '/output.json', JSON.stringify(allWords, null, "  "));
  Object.keys(allWords).forEach((word) => {
    getMorphology(word);
    getDefinition(word);
    getEtymology(word);
  });
});
