# Web-Scraping
My script to scrape data from my University's website taking advantage of a bug.
# Dependencies
   - python3
   - selenium
   - firefox 68 (my browser when the script was built)
   - latest geckodriver
   - basic research skills to learn how to include geckodriver before  
     running the script.<br/>
*Hint :export PATH=$PATH:/path/to/the/directory/contaning/the/geckodriver*
   - this script was written and tested in linux distro redhat fedora30.
   
   ## Issues Encountered
   - I wasn't able to open new tab in the browser and researching the problem I found [this](https://gist.github.com/lrhache/7686903). Searching further I found that opening a new window was simple and faster than the trick used in the above link, So I opened a new window for operations.
   - Closing the opened new windows was getting complicated so I didn't bothered to implement it since my main goal was fulfilled and holding ALT+F4 for a few seconds wasn't a big issue :P
