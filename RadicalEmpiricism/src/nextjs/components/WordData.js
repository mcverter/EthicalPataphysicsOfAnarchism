import React, { useEffect, useState } from "react";
import axios from "axios";
import cheerio from "cheerio";
import Collapsible from "react-collapsible";

const CNRTL_BASE_URL = "https://www.cnrtl.fr/etymologie/";
const LITTRE_BASE_URL = "https://www.littre.org/definition/";

export const WordData = ({ word }) => {
  const [cnrtlEtymologyContent, setCnrtlEtymologyContent] = useState();
  const [littreEtymologyContent, setLittreEtymologyContent] = useState();

  const fetchLittreEtymology = (word) => {
    axios.get(`${LITTRE_BASE_URL}${word}`).then(
      (response) => {
        if (response.status === 200) {
          const html = response.data;
          const $ = cheerio.load(html);
          setLittreEtymologyContent($(".etymologie"));
        }
      },
      (error) => console.log(`Axios LITTRE error ${error}`)
    );
  };

  const fetchCntrlEtymology = (word) => {
    axios.get(`${CNRTL_BASE_URL}${word}`).then(
      (response) => {
        if (response.status === 200) {
          const html = response.data;
          const $ = cheerio.load(html);
          setCnrtlEtymologyContent($("#art"));
        }
      },
      (error) => console.log(`Axios CNRTL error ${error}`)
    );
  };

  useEffect(() => {
    //    fetchLittreEtymology(word);
    fetchCntrlEtymology(word);
  }, [word]);
  return (
    <Collapsible open={true} trigger={`Details about ${word}`}>
      <div style={{ maxHeight: 150, overflow: "scroll" }}>
        {(littreEtymologyContent || cnrtlEtymologyContent) && (
          <div>
            <h2>Etymology </h2>
            {littreEtymologyContent && (
              <div
                dangerouslySetInnerHTML={{ __html: littreEtymologyContent }}
              />
            )}
            {cnrtlEtymologyContent && (
              <div
                dangerouslySetInnerHTML={{ __html: cnrtlEtymologyContent }}
              />
            )}
          </div>
        )}
        <div>Semantic Tags</div>
        <div>Part of speech</div>
      </div>
    </Collapsible>
  );
};
