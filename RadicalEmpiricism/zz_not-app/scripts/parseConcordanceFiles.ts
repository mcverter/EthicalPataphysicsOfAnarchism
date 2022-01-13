const fs = require("fs");
const readline = require("readline");
var JSSoup = require("jssoup").default;
const axios = require("axios");
const cheerio = require("cheerio");

let wordDefinitions = {};

const LITTRE_DEFINITION_PREFIX = "https://www.littre.org/definition/";

const CNTRL_DEFINITION_PREFIX = "https://www.cnrtl.fr/definition/";
const CNTRL_ACADEMIE9_DEFINITION_PREFIX =
  "https://www.cnrtl.fr/definition/academie9/";
const CNTRL_ETYMOLOGIE_PREFIX = "https://www.cnrtl.fr/etymologie/";
const CNTRL_MORPHOLOGIE_PREFIX = "https://www.cnrtl.fr/morphologie/";

axios
  .get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
  .then((response) => {
    console.log(response.data.url);
    console.log(response.data.explanation);
  })
  .catch((error) => {
    console.log(error);
  });

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
  const WordRegex = /(^.+?):(.+)./;
  const BookRegex = /(\w\w)(.+);/g;

  wordMatch = WordRegex.exec(line);
  word = wordMatch[1];

  allWords[word] = {};
  wordMatch[2].split(";").forEach((book) => {
    bookName = book.match(/\w+/)[0];
    citationCount = 1 + (book.indexOf(",") > -1 ? book.match(/,/g).length : 0);
    allWords[word][bookName] = citationCount;
  });
  console.log("word", word);
});

function getMorphology(word) {
  axios.get(``);
}
// oikos nomos

function getDefinition(word) { }

function getEtymology(word) { }

frenchConcordanceReadLine.on("close", () => {
  let wordList = [];


  function sleep(ms) {
    return new Promise((resolve) => {
      setTimeout(resolve, ms);
    });
  }

  async function processWordList() {
    if (wordList.length > 0) {
      const word = wordList.pop().toLowerCase();
      await sleep(1000);

      if (wordList.length % 100 === 0) {
        await sleep(100000);
      }

      console.log('process word list word processed', word)
      wordDefinitions[word] = {};
      axios
        .get(`${CNTRL_ACADEMIE9_DEFINITION_PREFIX}${word}`)
        .then((response) => {
          const data = response.data;
          const $ = cheerio.load(data);
          const entry = $("#contentbox").html();
          // console.log("cntrl entry", entry);
          wordDefinitions[word]['def_academie9'] = entry;

          axios
            .get(`${CNTRL_DEFINITION_PREFIX}${word}`)
            .then((response) => {
              const data = response.data;
              const $ = cheerio.load(data);
              const entry = $("#contentbox").html();
              // console.log("cntrl entry", entry);
              wordDefinitions[word]['def_cntrl'] = entry;

              axios
                .get(`${CNTRL_ETYMOLOGIE_PREFIX}${word}`)
                .then((response) => {
                  const data = response.data;
                  const $ = cheerio.load(data);
                  const entry = $("#contentbox").html();
                  // console.log("cntrl entry", entry);
                  wordDefinitions[word]['ety_cntrl'] = entry;

                  axios
                    .get(`${CNTRL_MORPHOLOGIE_PREFIX}${word}`)
                    .then((response) => {
                      const data = response.data;
                      const $ = cheerio.load(data);
                      const entry = $("#contentbox").html();
                      // console.log("cntrl entry", entry);
                      wordDefinitions[word]['mor_cntrl'] = entry;
                
                      processWordList();
                
                /*      
                axios
                        .get(`${LITTRE_DEFINITION_PREFIX}${word}`)
                        .then((response) => {
                          const data = response.data;
                          const $ = cheerio.load(data);
   //                       console.log('littre data', data);
                          const entry = $("section.definition").html();
                          // console.log("cntrl entry", entry);
                          wordDefinitions[word]['lit_def'] = entry;

                          processWordList();
                        })
                        .catch(err => console.log('fetch error 1', err));
                        */
                    })
                    .catch(err => {
                      console.error('fetch error 2',word, err)
                      processWordList();
                    });
                })
                .catch(err => {
                  console.error('fetch error 3',word, err)
                  processWordList();
                });
            })
            .catch(err => {
              console.error('fetch error 4',word, err)
              processWordList();
            });
        })
        .catch(err => {
          console.error('fetch error 5',word, err)
          processWordList();
        });

    }
    if (wordList.length === 0) {
      fs.writeFileSync(__dirname + "/definition.output.min.json", JSON.stringify(wordDefinitions));
      fs.writeFileSync(
        __dirname + "/definition.output.json",
        JSON.stringify(wordDefinitions, null, "  ")
      );
    }
  }

  console.log("me voici");
  fs.writeFileSync(__dirname + "/frequency.output.min.json", JSON.stringify(allWords));
  fs.writeFileSync(
    __dirname + "/frequency.output.json",
    JSON.stringify(allWords, null, "  ")
  );

  wordList = Object.keys(allWords).filter((word) => {
    if (word.match(/\d/)) {
      console.error("bad word", word);
      return false;
    }
    return true;
  });

  processWordList();
});
