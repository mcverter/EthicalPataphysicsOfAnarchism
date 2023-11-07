import Select from "react-select";
import React from "react";

export const WordSelecter = ({
  selectedOption,
  changeSelectedWord,
  options,
}) => (
  <>
    <label
      htmlFor="select-word"
      style={{ fontSize: 24, fontWeight: 700, lineHeight: 1.5 }}
    >
      {" "}
      Search / Chercher{" "}
    </label>
    <Select
      value={selectedOption}
      onChange={changeSelectedWord}
      options={options}
      isSearchable={true}
      name="select-word"
    />
  </>
);
