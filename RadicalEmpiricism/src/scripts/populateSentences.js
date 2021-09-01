const fs = require("fs");
const { Client } = require("pg");

const client = new Client({
  user: "postgres",
  host: "localhost",
  database: "RadicalEmpiricism",
  password: "postgres",
  port: 5432,
});
client.connect();

function searchForWord(word) {
  `select * from sentences where english ilike '%${word}%';`;
}

function insertTISentences() {
  const EnglishTITxt = fs.readFileSync(
    __dirname + "/../data/sentences/TIEnglishSentences.txt",
    "utf-8"
  );
  const FrenchTITxt = fs.readFileSync(
    __dirname + "/../data/sentences/TIFrenchSentences.txt",
    "utf-8"
  );

  const engArray = EnglishTITxt.split("\n");
  const frArray = FrenchTITxt.split("\n");
  const insertTemplate =
    "INSERT INTO sentences(book, english, french) VALUES($1, $2, $3) RETURNING *";

  client
    .query("SELECT * from sentences")
    .then((res) => console.log(res.rows[0]))
    .catch((e) => console.error(e.stack));
  //console.log(engArray.length)

  const insertPromises = engArray.map((english, idx) => {
    client
      .query(insertTemplate, ["ti", english, frArray[idx]])
      .then((res) => {
        console.log(res.rows[0]);
      })
      .catch((e) => console.error(e.stack));
  });

  Promise.all(insertPromises).then(function (results) {
    console.log(results);
  });
}
