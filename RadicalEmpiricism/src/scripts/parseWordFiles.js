const {tiWords} = require( '../data/words/TIWords');
const {otbWords } = require( '../data/words/OTBWords');

const wordMap = {};

const validWord = (w) => {
    return w.match(/\w/) && w.length > 2
}

const normalizeWord = (w) => {
    return w.toLocaleLowerCase()
    ;
}

tiWords.split(" ").forEach((tiw) => {
    if (validWord(tiw)) {
        const tiwLC = normalizeWord(tiw);
        if (tiwLC in wordMap) {
            wordMap[tiwLC].ti++;
        } else {
            wordMap[tiwLC] = {ti: 1, otb: 0};
        }
    }
});

otbWords.split(" ").forEach((otbw) => {
    if (validWord(otbw)) {
        const otbwLC = normalizeWord(otbw);
        if (otbwLC in wordMap) {
            wordMap[otbwLC].otb++;
        } else {
            wordMap[otbwLC] = {ti: 0, otb: 1};
        }
    }
});

// normalize word frequencies according to number of words in text
for (let w in wordMap) {
    wordMap[w].otb =
        Math.round(wordMap[w].otb * tiWords.length / otbWords.length);
    wordMap[w].sum = wordMap[w].otb + wordMap[w].ti;
}
const tiFreq = (word) => `(TI) ${wordMap[word].ti}`;
const bothFreq = (word) => `(Both) ${wordMap[word].sum}`;
const otbFreq = (word) => `(OTB) ${wordMap[word].otb}`;

const alphabeticalList = Object.keys(wordMap)
    .sort((a, b) => a.localeCompare(b))
    .map(w => ({value: `${w}`, label: `${w} ${bothFreq(w)} ${tiFreq(w)} ${otbFreq(w)}`})).slice(0,1000);

const combinedFrequencyList = Object.keys(wordMap)
    .sort((a, b) => (wordMap[b].sum) - (wordMap[a].sum))
    .map(w => ({value: `${w}`, label: `${w} ${bothFreq(w)} ${tiFreq(w)} ${otbFreq(w)}`})).slice(0,1000);

const tiFrequencyList = Object.keys(wordMap)
    .sort((a, b) => wordMap[b].ti - wordMap[a].ti)
    .map(w => ({value: `${w}`, label: `${w} ${tiFreq(w)} ${otbFreq(w)} ${bothFreq(w)}`})).slice(0,1000);

const otbFrequencyList = Object.keys(wordMap)
    .sort((a, b) => wordMap[b].otb - wordMap[a].otb)
    .map(w => ({value: `${w}`, label: `${w} ${otbFreq(w)} ${tiFreq(w)} ${bothFreq(w)}`})).slice(0,1000);

console.log(tiWords, alphabeticalList, tiFrequencyList, otbFrequencyList);
module.exports = {
    tiWords,
    alphabeticalList,
    tiFrequencyList,
    otbFrequencyList
}