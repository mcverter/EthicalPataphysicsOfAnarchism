const fs = require("fs");
const readline = require("readline");

const frenchConcordanceReadLine = readline.createInterface({
  input: fs.createReadStream(
    __dirname + "/../../data/Concordance/Sections/French.txt"
  ),
  output: process.stdout,
  console: false,
});

function exitOnError(message, err) {
  console.error(message, err);
  process.exit(1);
}

const allWords = {};

frenchConcordanceReadLine.on("line", (line) => {
  let wordMatch, word, bookMatch, citationCount, bookName;
  const WordRegex = /(\w+):(.+)./;
  const BookRegex = /(\w\w)(.+);/g;

//  console.log(line);
  wordMatch = WordRegex.exec(line);
  // console.log(wordMatch);
  if (wordMatch && wordMatch.length > 1) {
  word = wordMatch[1];
  }
  else {
    console.log(wordMatch)
  }
//  console.log("word", word);
  allWords[word] = {};

  wordMatch[2].split(";").forEach((book) => {
    bookName = book.match(/\w+/)[0];
    citationCount = 1 + (book.indexOf(",") > -1 ? book.match(/,/g).length : 0);
    allWords[word][bookName] = citationCount;
    // console.log("book", book, "bookName", bookName, "citations", citationCount);
  });
  //    console.log(line); //    ABAISSEMENT: TI 229:14; NP 43:32; ADV 20:34; DQVI 62:11; TEI 61:10, 61:14, 61:17; HN 134:7, 136:19, 150:37.
});

frenchConcordanceReadLine.on("close", () => {
  console.log("me voici");
//  console.log(allWords);
});
