const wordMap = {};
function printFrequencyCell(key) {
    return `<span style="font-weight: 900; font-size: 150%">  ${key} </span>
            <span style="color: green"> TI: ${wordMap[key].ti} </span>
            <span style="color: blue">  AE: ${wordMap[key].otb} </span>
            <span style="color: red">  Total: ${wordMap[key].sum} </span>`;
}

const wordsSortedAlphabetically = Object.keys(wordMap).sort();
const wordsSortedTI = Object.keys(wordMap).sort(
    (a, b) => wordMap[b].ti - wordMap[a].ti
);
const wordsSortedOTB = Object.keys(wordMap).sort(
    (a, b) => wordMap[b].otb - wordMap[a].otb
);
const wordsSortedBoth = Object.keys(wordMap).sort(
    (a, b) => wordMap[b].sum - wordMap[a].sum
);


function printPage() {
    console.log(`
<html>
<head>
<title> Fréquence des mots dans les livres de Lévinas</title>
</head>
<body>
<h1> Fréquence des mots dans les livres de Lévinas</h1>

<table>
    <thead>
        <tr>
            <th>#</th>
            <th>Trié par ordre alphabétique</th>
            <th>Trié par fréquence dans "Totalité et infini"</th>
            <th>Trié par fréquence (ajustée) dans "Autrement qu'être"</th>
            <th>Trié par fréquence (ajustée) dans les deux livres</th>
        </tr>
    </thead>
    <tbody>
`);

    for (let idx = 0; idx < wordsSortedAlphabetically.length; idx++) {
        console.log(`
    <tr>
        <td>${idx}</td>
        <td>${printFrequencyCell(wordsSortedAlphabetically[idx])}</td>
        <td>${printFrequencyCell(wordsSortedTI[idx])}</td>
        <td>${printFrequencyCell(wordsSortedOTB[idx])}</td>
        <td>${printFrequencyCell(wordsSortedBoth[idx])}</td>
    </tr>
    `);
    }

    console.log(`    
    </tbody>
</table>
</body>
</html>
`);


    /*
    let tiWordFile;
    let otbWordFile;

    function exitOnError(message, err) {
      console.error(message, err);
      process.exit(1);
    }
    */
}