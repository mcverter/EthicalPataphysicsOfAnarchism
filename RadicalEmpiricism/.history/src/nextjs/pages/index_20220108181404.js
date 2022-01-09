import React, { useEffect, useState } from "react";
import Head from "next/head";
import styles from "../styles/Home.module.css";
import axios from "axios";
import { tiFrench } from "../data/sentences/TIFrenchSentences";
import { tiEnglish } from "../data/sentences/TIEnglishSentences";

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
  console.log(tiFrench, frenchTISentences);
  console.log(tiEnglish, englishTISentences);

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

  return (
    <div className={styles.container}>
      <Head>
        <title>Hello Levinas Scholars</title>
      </Head>
      <main>
        <h1 className={styles.title}>Welcome to Radical Empiricism</h1>
        {frenchTISentences &&
          frenchTISentences.length > 0 &&
          englishTISentences &&
          englishTISentences.length > 0 && (
            <table>
              <div>
                {frenchTISentences[5]}
                {englishTISentences[5]}
              </div>
            </table>
          )}
      </main>
    </div>
  );
}
