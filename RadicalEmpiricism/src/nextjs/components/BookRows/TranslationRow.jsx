import React from "react";

/**
 *
 * @param {number} idx -- Line Number
 * @param {string} book -- book name
 * @param {string} english -- english sentence
 * @param {string} french -- french sentence
 * @returns {*}
 * @constructor
 */
export const TranslationRow = ({idx, book, english, french}) => {
  return (
  <tr>
    <td width="4%" >{book}#{idx}</td>
    <td width="48%" className="english"> {english} </td>
    <td width="48%" className="french"> {french} </td>
  </tr>
);
  }
