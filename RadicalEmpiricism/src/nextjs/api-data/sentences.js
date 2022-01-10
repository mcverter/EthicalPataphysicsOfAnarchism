const TIEnglishSentences = require("./sentences/TIEnglishSentences");
const TIFrenchSentences = require("./sentences/TIFrenchSentences");

function selectWordSentences(book, word) {
  if (book === "otb") {
    return {
      en: [],
      fr: [],
    };
  }

  let selected = { en: [], fr: [] };

  TIFrenchSentences.forEach((sentence, idx) => {
    if (sentence.match(word)) {
    selected.fr.push(sentence);
    selected.en.push(TIEnglishSentences[idx]);
  }});

  return selected;
}

function selectBilingualRange(book, start, end) {
  if (book === "otb") {
    return {
      en: [],
      fr: [],
    };
  }
  return {
    en: TIEnglishSentences.slice(start, end),
    fr: TIFrenchSentences.slice(start, end),
  };
}

export default (req, res) => {
  console.error("req query", req.query, typeof req.query);
  console.error("req body", req.body);
  const { book, start, end, word } = req.query;
  console.error("params", book, start, end, word);

  res.statusCode = 200;

  if (book && word) {
    res.json({ data: selectWordSentences(book, word) });
  } else if (!book || !start || !end || end < start) {
    res.json({ data: selectBilingualRange("ti") });
  } else {
    res.json({ data: selectBilingualRange(book, start, end) });
  }
};
