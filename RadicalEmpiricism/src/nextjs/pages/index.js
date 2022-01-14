import React, {useState} from "react";
import Head from "next/head";
import styles from "../styles/Home.module.css";
import {tiFrench} from "../data/sentences/TIFrenchSentences";
import {tiEnglish} from "../data/sentences/TIEnglishSentences";
import {otbEnglish} from "../data/sentences/OTBEnglishSentences";
import {otbFrench} from "../data/sentences/OTBFrenchSentences";
import Select from "react-select";
import {otbFrequencyList, tiFrequencyList, alphabeticalList, combinedFrequencyList} from '../data/words/parseWordFiles'
import {BookRows} from "../components/BookRows";

const createCombinedArray = ({englishSentences, frenchSentences}) => {
    const frenchArray = frenchSentences.split('\n');
    const englishArray = englishSentences.split('\n');
    const combinedArray = []
    for (let i = 0; i < frenchArray.length; i++) {
        combinedArray.push({
            line: i + 1,
            english: englishArray[i],
            french: frenchArray[i]
        })
    }
    return combinedArray;
}

const tiCombinedArr = createCombinedArray({englishSentences: tiEnglish, frenchSentences: tiFrench});

const otbCombinedArr = createCombinedArray({englishSentences: otbEnglish, frenchSentences: otbFrench});


const defaultSentence = {
    line: 0,
    english: "Search sentences for matching words",
    french: "Rechercher des phrases pour les mots correspondants"
}

export default function Home() {
    const [combinedTISentences, setCombinedTISentences] = useState([defaultSentence]);
    const [combinedOTBSentences, setCombinedOTBSentences] = useState([defaultSentence]);
    const [selectedOption, setSelectedOption] = useState(null);
    const [options, setOptions] = useState(combinedFrequencyList)

    const changeSelectedWord = (w) => {
        setSelectedOption(w);
        const {value} = w;
        if (value.length > 2) {
            const pattern = value;
            const tiCombinedFiltered = tiCombinedArr.filter(s => {
                return s.french.match(pattern)
            })
            const otbCombinedFiltered = otbCombinedArr.filter(s => {
                return s.french.match(pattern)
            })

            setCombinedTISentences(tiCombinedFiltered)
            setCombinedOTBSentences(otbCombinedFiltered)
        }
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
                <BookRows sentences={combinedTISentences} bookname="TI" />
                <BookRows sentences={combinedOTBSentences} bookname="OTB" />
            </main>
        </div>
    );
}
