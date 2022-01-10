import React, { useEffect, useState } from "react";
import Head from "next/head";
import styles from "../styles/Home.module.css";
import axios from "axios";
import { tiFrench } from "../data/sentences/TIFrenchSentences";
import { tiEnglish } from "../data/sentences/TIEnglishSentences";
import { TranslationRow } from "../components/TranslationCell";
import Select from "react-select";
import {otbFrequencyList, tiFrequencyList, alphabeticalList, combinedFrequencyList} from '../scripts/parseWordFiles'

let ROOT_URL = "http://google.com";
let TIFrenchSentences, TIEnglishSentences;
const tiFrenchArr = tiFrench.split('\n')
const tiEnglishArr = tiEnglish.split('\n')

const tiCombinedArr = []
for (let i=0;i<tiFrenchArr.length; i++){
    tiCombinedArr.push({
        line: i+1,
        english:tiEnglishArr[i],
        french: tiFrenchArr[i]
    })
}

export default function Home() {
  //useEffect(() => fetchSentences());
  const [combinedTISentences, setCombinedTISentences] = useState(
    tiCombinedArr
  );
  const [selectedOption, setSelectedOption] = useState(null);
  const [options, setOptions] = useState(combinedFrequencyList)

    const changeSelectedWord = (w) => {
      setSelectedOption(w)
        const combiledFiltered = tiCombinedArr.filter(s=>{
            const pattern = new RegExp(`[^ \W]${w.value}[$ \W]`);
            return s.french.match(pattern)})
        console.log(combiledFiltered)
        setCombinedTISentences(combiledFiltered)
    }


  return (
    <div className={styles.container}>
      <Head>
        <title>Hello Levinas Scholars</title>
      </Head>
      <main>
        <h1 className={styles.title}>Welcome to Radical Empiricism</h1>
        <Select
          defaultValue={selectedOption}
          onChange={changeSelectedWord}
          options={options}
          isSearchable={true}
        />
          {combinedTISentences && combinedTISentences.map(tca=>
              <TranslationRow
                  idx={tca.line}
                  book={"ti"}
                  english={tca.english}
                  french={tca.french}
              />)
          }
      </main>
    </div>
  );

  const fetchSentences = () => {
    axios({
      headers: { "Access-Control-Allow-Origin": "*" },
      method: "get",
      url: `${ROOT_URL}TIFrenchSentences.txt`,
    })
      .then(function (response) {
        TIFrenchSentences = response.data.split("\n");
        setFrenchTISentences(TIFrenchSentences);
        debugger;
      })
      .catch((err) => console.error("err", err));
    axios({
      headers: { "Access-Control-Allow-Origin": "*" },
      method: "get",
      url: `${ROOT_URL}TIEnglishSentences.txt`,
    })
      .then(function (response) {
        TIEnglishSentences = response.data.split("\n");
        setEnglishTISentences(TIEnglishSentences);
        debugger;
      })
      .catch((err) => console.error("err", err));
  };
}
