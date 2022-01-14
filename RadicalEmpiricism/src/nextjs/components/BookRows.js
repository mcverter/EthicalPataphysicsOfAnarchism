import {TranslationRow} from "./TranslationRow";
import React from "react";
import Collapsible from 'react-collapsible'

const LongBooknameMap = {
    "TI": "Totality and Infinity // Totalité et infini",
    "OTB": "Otherwise than Being //Autrement qu'être",
}

export const BookRows = ({bookname, sentences}) => (
    <Collapsible open={true} trigger={LongBooknameMap[bookname]} className={bookname.toLowerCase()}>
        <div style={{maxHeight: 300, overflow: "scroll"}}>
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
        </div>
    </Collapsible>
)
