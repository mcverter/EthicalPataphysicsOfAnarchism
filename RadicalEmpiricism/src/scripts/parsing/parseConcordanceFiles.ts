const fs = require("fs");
const readline = require("readline");
var JSSoup = require('jssoup').default;
onst axios = require('axios');

axios.get('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY')
  .then(response => {
    console.log(response.data.url);
    console.log(response.data.explanation);
  })
  .catch(error => {
    console.log(error);
  });


const frenchConcordanceReadLine = readline.createInterface({
  input: fs.createReadStream(
    __dirname + "/../../data/Concordance/Section/French.txt"
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
  const WordRegex = /(^.+):(.+)./;
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

/*
https://www.littre.org/definition/abaissement
*/

/*
https://www.cnrtl.fr/definition/abaissement
https://www.cnrtl.fr/definition/academie8/abaissement
https://www.cnrtl.fr/etymologie/abaissement

*/
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
