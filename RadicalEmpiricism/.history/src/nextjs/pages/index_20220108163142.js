import React, { useEffect, useState } from "react";
import Head from "next/head";
import styles from "../styles/Home.module.css";
import { TranslationRow } from "../../client/components/TranslationCell";

let ROOT_URL = "http://localhost:8080/data/sentences/";
//  "https://github.com/mcverter/EthicalPataphysicsOfAnarchism/tree/master/RadicalEmpiricism/src/data/sentences/";
let TIFrenchSentences, TIEnglishSentences;
axios({
  headers: { "Access-Control-Allow-Origin": "*" },
  method: "get",
  url: `${ROOT_URL}TIFrenchSentences.txt`,
}).then(function (response) {
  TIFrenchSentences = response.data.split("\n");
  console.log(TIFrenchSentences);
});
axios({
  headers: { "Access-Control-Allow-Origin": "*" },
  method: "get",
  url: `${ROOT_URL}TIEnglishSentences.txt`,
}).then(function (response) {
  TIEnglishSentences = response.data.split("\n");
  console.log(TIEnglishSentences);
});

export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title>Hello Levinas Scholars</title>
      </Head>

      <main className={styles.main}>
        <h1 className={styles.title}>Welcome to Radical Empiricism</h1>
      </main>
      <div>Look at these lines:</div>
    </div>
  );
}
