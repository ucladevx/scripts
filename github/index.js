const fetch = require('node-fetch');
const fs = require('fs');

// this should have the github admin:org scope
const token = '';
const outFile = 'results.json';
const inFile = 'members.csv';

const base = 'https://api.github.com/orgs/ucladevx/memberships/';
const role = 'member';

const out = fs.openSync(outFile, 'w');
const usernames = fs.readFileSync(inFile, 'ascii').split('\n');


Promise.all(usernames.map(user => {
    const url = base + user;
    return fetch(url, {
        method: 'PUT',
        headers: {
            Authorization: `token ${token}`
        }
    }).then(res => res.json());
})).then(result => {
    fs.appendFileSync(out, JSON.stringify(result, null, 2));
    console.log('Members added to DevX org, results in results.txt');

    fs.closeSync(out);
}).catch(err => {
    console.log(err);
    fs.closeSync(out);
});




