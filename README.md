# RIS Event Scraper

Scrapes all events of the RIS in Heilbronn for usage in a city api / alexa skill / ...

\#odd2018 fun-project   

## Setup
 
 Download [tabular.jar](https://github.com/tabulapdf/tabula-java/releases) into directory `lib`
 
## How does it work? 
 
 We use tabula to extract a csv of the pdf using spreadsheet mode (detects ruling lines separating each cell). Sample command:
 
 `java -jar tabula-1.0.1-jar-with-dependencies.jar -g -r -l --outfile ./data/sitzungsplan.csv ./data/sitzungsplan.pdf`
 
 