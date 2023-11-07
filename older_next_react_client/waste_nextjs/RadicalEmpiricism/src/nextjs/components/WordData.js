import React, { useEffect, useState } from "react";
import axios from "axios";
import cheerio from "cheerio";
import Collapsible from "react-collapsible";
import { Tab, Tabs, TabList, TabPanel } from "react-tabs";
import "react-tabs/style/react-tabs.css";

const CNRTL_BASE_URL = "https://www.cnrtl.fr/etymologie/";
const LITTRE_BASE_URL = "https://www.littre.org/definition/";
const CNRTL_BASE_MORPHOLOGY_URL = "https://www.cnrtl.fr/morphologie/";

export const WordData = ({ word }) => {
  const [cnrtlEtymologyContent, setCnrtlEtymologyContent] = useState();
  const [littreEtymologyContent, setLittreEtymologyContent] = useState();
  const [cnrtlMorphologyContent, setCntrlMorphologyContent] = useState();

  const fetchCtnrlMorphology = async (word) => {
    const response = await axios.get(`${CNRTL_BASE_MORPHOLOGY_URL}${word}`);
    if (response.status === 200) {
      const html = response.data;
      const $ = cheerio.load(html);
      const tabs = [];
      tabs.push({
        heading: $("#vitemselected a").html(),
        content: $("#contentbox").html(),
      });
      const lis = $(
        "div#main_content div#content table tr td div#vtoolbar ul li"
      );

      console.log("length", lis.length);
      let myArray = Array.apply(null, { length: lis.length })
        .map(Number.call, Number)
        .slice(1)
        .map((number) => {
          console.log("number", number);
          return axios
            .get(`${CNRTL_BASE_MORPHOLOGY_URL}${word}//${number}`)
            .then((response) => {
              if (response.status === 200) {
                const html = response.data;
                const $ = cheerio.load(html);
                tabs.push({
                  heading: $("#vitemselected a").html(),
                  content: $("#contentbox").html(),
                });
              }
            });
        });

      await Promise.all(myArray);
      setCntrlMorphologyContent(tabs);
    }
  };

  //      await Promise.all();
  /*      const morphologies = Array.prototype.forEach.call(lis, (li) => {
        const morphologieUrl = li.children[0].attribs.onclick
          .match(/\(.*\)/)[0]
          .slice(1, -1)
          .split(",")[0];
        console.log(morphologieUrl);
        debugger;
        sendRequest(sendRequestArgs[0], sendRequestArgs[1]);
      });

 */

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
    fetchCtnrlMorphology(word);
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
        {cnrtlMorphologyContent && (
          <div>
            <h2>Morphology</h2>
            <Tabs>
              <TabList>
                {cnrtlMorphologyContent.map((morph) => (
                  <Tab>
                    <div dangerouslySetInnerHTML={{ __html: morph.heading }} />
                  </Tab>
                ))}
              </TabList>
              {cnrtlMorphologyContent.map((morph) => (
                <TabPanel>
                  <div dangerouslySetInnerHTML={{ __html: morph.content }} />
                </TabPanel>
              ))}
            </Tabs>
          </div>
        )}

        <div>Semantic Tags</div>
        <div>Part of speech</div>
      </div>
    </Collapsible>
  );
};
