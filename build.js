const sqlite3 = require('sqlite3').verbose();
const fs = require('fs');
let db = new sqlite3.Database('./mysite/data.sqlite');

db.serialize(function() {
  db.all('SELECT content FROM messages', function(err, rows) {
    if (err) {
      console.error(err);
      return;
    }

    // Read the template file
    let template = fs.readFileSync('./mysite/template.html', 'utf8');

    let messagesHtml = '';

    // Generate HTML for each message
    rows.forEach((row) => {
      messagesHtml += `<p>${row.content}</p>`;
    });

    // Replace the placeholder in the template with the messages
    let html = template.replace('{{messages}}', messagesHtml);

    // Save the generated HTML to a file
    fs.writeFileSync('index.html', html);
  });
});

db.close();