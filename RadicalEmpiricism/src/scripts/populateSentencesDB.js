const fs = require('fs');
const readline = require("readline");

let ti_en_num = 1;
let ti_fr_num = 1;
// ti_sentences table -- index french, english, 
const englishTI = readline.createInterface({
    input: fs.createReadStream()
})


englishTI.on("line", (line) => {
    lineCount++;
})  

englishTI.on("close",()=> {
    const FrechTI = readline.createInterface({
        input: fs.createReadStream()
    })
    englishTI.on("line", (line) => {
        lineCount++;
    })  
        
})

// open ti french
// keep a counter
// insert line per file
// insert (id, french) VALUES (COUNT, input )

// open ti english 
// for each line in file, populate db from both files
// update ti_sentences, set english=input where id=COUNT

