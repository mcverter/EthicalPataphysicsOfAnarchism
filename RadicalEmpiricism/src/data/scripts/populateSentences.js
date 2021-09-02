const fs = require('fs')
const {Client} = require('pg')
const client = new Client({
    user: 'postgres',
    host: 'localhost',
    database: 'radicalempiricism',
    password: 'postgres',
    port: 5432,
})
client.connect()
function splitFileContentsIntoArray(contents) {
    return contents.replace(/\r/, '').split(/\n/)
}

const otb_fr = splitFileContentsIntoArray(fs.readFileSync('/home/mitchell/ComputerScience_Shared/EthicalPataphysicsOfAnarchism/RadicalEmpiricism/src/data/sentences/OTBFrenchSentences.txt', 'utf-8'))
const otb_en = splitFileContentsIntoArray(fs.readFileSync('/home/mitchell/ComputerScience_Shared/EthicalPataphysicsOfAnarchism/RadicalEmpiricism/src/data/sentences/OTBEnglishSentences.txt', 'utf-8'))
const ti_fr = splitFileContentsIntoArray(fs.readFileSync('/home/mitchell/ComputerScience_Shared/EthicalPataphysicsOfAnarchism/RadicalEmpiricism/src/data/sentences/TIFrenchSentences.txt', 'utf-8'))
const ti_en = splitFileContentsIntoArray(fs.readFileSync('/home/mitchell/ComputerScience_Shared/EthicalPataphysicsOfAnarchism/RadicalEmpiricism/src/data/sentences/TIEnglishSentences.txt', 'utf-8'))
console.log('hello world')

client.query(`CREATE TABLE if not exists sentences  (id SERIAL PRIMARY KEY, English TEXT NOT NULL, French TEXT NOT NULL,Book TEXT);`)

const ti_lines = ti_en.length
for (let i =0; i< ti_lines; i++ ) {
    const query = '';
    client.query(`INSERT INTO sentences(id, english, french, book) VALUES('${i+1}', '${ti_en[i]}', '${ti_fr[i]}', 'ti')`)
}

