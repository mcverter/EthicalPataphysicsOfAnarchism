import Select from "react-select";
import React from "react";
import { WordSelecter } from "./WordSelecter";
import { WordOrderingChooser } from "./WordOrderingChooser";

export const WordSearchForm = ({
  selectedOption,
  changeSelectedWord,
  options,
  onChangeFrequencyOrder,
}) => (
  <div style={{ padding: "5px", border: "5px solid #eaeaea", margin: 15 }}>
    <form>
      <WordSelecter
        selectedOption={selectedOption}
        changeSelectedWord={changeSelectedWord}
        options={options}
      />
      <WordOrderingChooser onChangeFrequencyOrder={onChangeFrequencyOrder} />
    </form>
  </div>
);
