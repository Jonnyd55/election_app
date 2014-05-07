May 6th 2014 Election Results
_____________________________

The code for the May 6th live election results app. This is just for the city of Norfolk.

The files:

1. norfolk.py - The script I used to scrape the Virginia State Board of elections site to get live results. It returns a JSON object (norfolk.js) which serves as the data source to feed the rest of the app.
2. index.html - The markup, which includes the underscore.js template for each race. 
3. norfolk.js - A JSON object that feeds the backbone.js app. 
4. main.js - The backbone.js code.
5. styles.css - Making it look pretty
