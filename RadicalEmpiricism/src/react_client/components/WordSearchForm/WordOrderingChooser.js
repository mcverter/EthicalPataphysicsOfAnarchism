import React from "react";

export const WordOrderingChooser = ({ onChangeFrequencyOrder }) => (
  <div style={{ display: "flex", justifyContent: "space-around" }}>
    <div>Word Frequency Sort:</div>
    <div className="radio">
      <label>
        <input
          type="radio"
          value="ti"
          name="frequency-type"
          onChange={onChangeFrequencyOrder}
        />
        Totality
      </label>
    </div>
    <div className="radio">
      <label>
        <input
          type="radio"
          value="otb"
          name="frequency-type"
          onChange={onChangeFrequencyOrder}
        />
        Otherwise
      </label>
    </div>
    <div className="radio">
      <label>
        <input
          type="radio"
          value="both"
          name="frequency-type"
          onChange={onChangeFrequencyOrder}
        />
        Both
      </label>
    </div>
    <div className="radio">
      <label>
        <input
          type="radio"
          value="alpha"
          name="frequency-type"
          onChange={onChangeFrequencyOrder}
        />
        A-Z
      </label>
    </div>
  </div>
);
