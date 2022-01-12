import React from "react";

const EnglishCell = (english) => <td>{english}</td>;
const FrenchCell = (french) => <td>{french}</td>;

/**
 * 
 * @param param0 
 * @returns 
 */
export const TranslationRow = ({idx, book, english, french}) => {
  debugger; 
  console.log('foo')
  return (
  <tr id={book + idx} key={idx}>
    <td> {english} </td>
    <td> {french} </td>
  </tr>
);
  }