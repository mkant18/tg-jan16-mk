const sqlite3 = require('sqlite3').verbose();
const fs = require('fs');
let db = new sqlite3.Database('./mysite/data.sqlite');

db.serialize(function() {
  db.all('SELECT content FROM messages', function(err, rows) {
    if (err) {
      console.error(err);
      return;
    }

    let html = '<html><body>';

    // Generate HTML for each message
    rows.forEach((row) => {
      html += `<p>${row.content}</p>`;
    });

    html += '</body></html>';

    // Save the generated HTML to a file
    fs.writeFileSync('index.html', html);
  });
});

db.close();