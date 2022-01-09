import React, { useEffect, useState } from "react";
import Head from "next/head";
import styles from "../styles/Home.module.css";
import axios from "axios";
import { tiFrench } from "../data/sentences/TIFrenchSentences";
import { tiEnglish } from "../data/sentences/TIEnglishSentences";
import { TranslationRow } from "../components/TranslationCell";
import Select from "react-select";

let ROOT_URL = "http://localhost:8080/src/data/sentences/";
let TIFrenchSentences, TIEnglishSentences;

export default function Home() {
  //useEffect(() => fetchSentences());
  const [frenchTISentences, setFrenchTISentences] = useState(
    tiFrench.split("\n")
  );
  const [englishTISentences, setEnglishTISentences] = useState(
    tiEnglish.split("\n")
  );
  const [selectedOption, setSelectedOption] = useState(null);
  const options = [
    { value: "chocolate", label: "Chocolate" },
    { value: "strawberry", label: "Strawberry" },
    { value: "vanilla", label: "Vanilla" },
  ];

  return (
    <div className={styles.container}>
      <Head>
        <title>Hello Levinas Scholars</title>
      </Head>
      <main>
        <h1 className={styles.title}>Welcome to Radical Empiricism</h1>
        <Select
          defaultValue={selectedOption}
          onChange={setSelectedOption}
          options={options}
          isSearchable={true}
        />

        {frenchTISentences &&
          frenchTISentences.length > 0 &&
          englishTISentences &&
          englishTISentences.length > 0 && (
            <table>
              {[0, 1, 2, 3, 4].map((idx) => (
                <TranslationRow
                  idx={idx}
                  book={"ti"}
                  english={englishTISentences[idx]}
                  french={frenchTISentences[idx]}
                />
              ))}
            </table>
          )}
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
