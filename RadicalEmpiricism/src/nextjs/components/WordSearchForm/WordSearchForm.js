import Select from "react-select";
import React from "react";

export const WordSearchForm = ({selectedOption, changeSelectedWord, options, onChangeFrequencyOrder}) => (
    <div style={{padding: '5px', border: '5px solid #eaeaea', margin: 15}}>
        <form>
            <label htmlFor="select-word" style={{fontSize: 24, fontWeight: 700, lineHeight: 1.5}}> Search /
                Chercher </label>

            <Select
                defaultValue={selectedOption}
                onChange={changeSelectedWord}
                options={options}
                isSearchable={true}
                name="select-word"
            />
            <div style={{display: 'flex', justifyContent: 'space-around'}}>
                <div>Word Frequency Sort:</div>
                {/*
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
            */}
                <div className="radio">
                    <label>
                        <input
                            type="radio"
                            value="both"
                            name="frequency-type"
                        />
                        Both
                    </label>
                </div>
                {/*
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
            */}
            </div>
        </form>
    </div>
)