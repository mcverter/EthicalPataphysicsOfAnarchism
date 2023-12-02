import React, { useState } from "react";
import Head from "next/head";
import styles from "../styles/Home.module.css";
import { tiFrench } from "../data/sentences/TIFrenchSentences";
import { tiEnglish } from "../data/sentences/TIEnglishSentences";
import { otbEnglish } from "../data/sentences/OTBEnglishSentences";
import { otbFrench } from "../data/sentences/OTBFrenchSentences";
import {
  otbFrequencyList,
  tiFrequencyList,
  combinedFrequencyList,
  alphabeticalList,
} from "../data/words/parseWordFiles";
import { BookRows } from "../components/BookRows/BookRows";
import { WordSearchForm } from "../components/WordSearchForm/WordSearchForm";
import { Introduction } from "../components/Introduction";
import { WordData } from "../components/WordData";

const createCombinedArray = ({ englishSentences, frenchSentences }) => {
  const frenchArray = frenchSentences.split("\n");
  const englishArray = englishSentences.split("\n");
  const combinedArray = [];
  for (let i = 0; i < frenchArray.length; i++) {
    combinedArray.push({
      line: i + 1,
      english: englishArray[i],
      french: frenchArray[i],
    });
  }
  return combinedArray;
};

const tiCombinedArr = createCombinedArray({
  englishSentences: tiEnglish,
  frenchSentences: tiFrench,
});

const otbCombinedArr = createCombinedArray({
  englishSentences: otbEnglish,
  frenchSentences: otbFrench,
});

const defaultSentence = {
  line: 0,
  english: "Search sentences for matching words",
  french: "Rechercher des phrases pour les mots correspondants",
};
const bookToWordFrequency = {
  alpha: alphabeticalList,
  ti: tiFrequencyList,
  otb: otbFrequencyList,
  both: combinedFrequencyList,
};
export default function Home() {
  const [combinedTISentences, setCombinedTISentences] = useState([
    defaultSentence,
  ]);
  const [combinedOTBSentences, setCombinedOTBSentences] = useState([
    defaultSentence,
  ]);

  const [selectedOption, setSelectedOption] = useState(null);
  const [options, setOptions] = useState(combinedFrequencyList);

  const changeWordFrequencyOrder = (event) => {
    const ordering = bookToWordFrequency[event.target.value];
    const foo = selectedOption;
    const selectedOptionInNewOrdering = ordering.find(
      (o) => o.value === selectedOption.value
    );
    setOptions(ordering);
    setSelectedOption(selectedOptionInNewOrdering);
  };
  const changeSelectedWord = (w) => {
    setSelectedOption(w);
    const { value } = w;
    if (value.length > 2) {
      const pattern = value;
      const tiCombinedFiltered = tiCombinedArr.filter((s) => {
        return s.french.match(pattern);
      });
      const otbCombinedFiltered = otbCombinedArr.filter((s) => {
        return s.french.match(pattern);
      });

      setCombinedTISentences(tiCombinedFiltered);
      setCombinedOTBSentences(otbCombinedFiltered);
    }
  };

  return (
    <div className={styles.container}>
      <Head>
        <title>Levinas Radical Empiricism (Empirisme Radical) </title>
      </Head>
      <main>
        <Introduction
          french="Levinas Empirisme Radical"
          english="Levinas Radical Empiricism"
        />
        <WordSearchForm
          options={options}
          changeSelectedWord={changeSelectedWord}
          selectedOption={selectedOption}
          onChangeFrequencyOrder={changeWordFrequencyOrder}
        />
        {selectedOption && <WordData word={selectedOption.value} />}
        <BookRows sentences={combinedTISentences} book="TI" />
        <BookRows sentences={combinedOTBSentences} book="OTB" />
      </main>
      <nav>
        Questions/Comments:{" "}
        <a
          style={{ color: "blue", textDecoration: "underline" }}
          target="_blank"
          href="mailto:roadrunner@waste.org,mitchell.verter@gmail.com?subject=RadicalEmpiricism"
        >
          Me voici (Mitchell Cowen Verter email)
        </a>
      </nav>
    </div>
  );
}