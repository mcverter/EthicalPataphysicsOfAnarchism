import React, { useEffect, useState } from "react";
import Head from "next/head";
import styles from "../styles/Home.module.css";
import axios from "axios";

let ROOT_URL = "http://localhost:8080/data/sentences/";
let TIFrenchSentences, TIEnglishSentences;

//  "https://github.com/mcverter/EthicalPataphysicsOfAnarchism/tree/master/RadicalEmpiricism/src/data/sentences/";

export default function Home() {
  useEffect(() => fetchSentences());
  const [frenchTISentences, setFrenchTISentences] = useState([]);
  const [englishTISentences, setEnglishTISentences] = useState([]);

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
      {frenchTISentences &&
        frenchTISentences.length > 0 &&
        englishTISentences ** englishTISentences.length > 0 && (
          <div>
            {frenchTISentences[0]}
            {englishTISentences[0]}
          </div>
        )}
      <main className={styles.main}>
        <h1 className={styles.title}>Welcome to Radical Empiricism</h1>
      </main>
      <div>Look at these lines:</div>
    </div>
  );
}
