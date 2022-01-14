import {TranslationRow} from "./TranslationRow";
import React from "react";

export const BookRows  = ({bookname, sentences}) => (
<table>
    {sentences && sentences.map(s =>
        <TranslationRow
            idx={s.line}
            book={bookname}
            english={s.english}
            french={s.french}
        />)
    }
</table>
)
