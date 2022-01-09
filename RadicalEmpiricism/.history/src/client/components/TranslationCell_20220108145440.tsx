import React from "react";

const EnglishCell = (english) => <td>{english}</td>;
const FrenchCell = (french) => <td>{french}</td>;

/**
 * 
 * @param param0 
 * @returns 
 */
const TranslationRow = ({idx, book, english, french}) => (
  <tr id={book + idx}>
    <EnglishCell english={english} />
    <FrenchCell french={french} />
  </tr>
);
