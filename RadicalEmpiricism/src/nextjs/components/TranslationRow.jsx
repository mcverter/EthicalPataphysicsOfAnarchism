import React from "react";

const EnglishCell = (english) => <td>{english}</td>;
const FrenchCell = (french) => <td>{french}</td>;

/**
 * 
 * @param param0 
 * @returns 
 */
export const TranslationRow = ({idx, book, english, french}) => {
  return (
  <tr id={book + idx} key={book + idx}>
    <td width="4%" >L{idx}</td>
    <td width="48%" className="english"> {english} </td>
    <td width="48%" className="french"> {french} </td>
  </tr>
);
  }
