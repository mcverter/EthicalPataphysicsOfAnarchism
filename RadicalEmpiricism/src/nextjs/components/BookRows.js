import {TranslationRow} from "./TranslationRow";
import React from "react";
import Collapsible from 'react-collapsible'

const LongBooknameMap = {
    "TI": "Totality and Infinity // Totalité et infini",
    "OTB":  "Otherwise than Being //Autrement qu'être",
}

export const BookRows  = ({bookname, sentences}) => (
<Collapsible trigger={LongBooknameMap[bookname]} className={bookname.toLowerCase()}>
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
</Collapsible>
)
