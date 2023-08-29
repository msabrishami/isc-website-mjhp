# isc-website-mjhp
This is the bootstrap-based project for the information portal of ISC website



## How to use the translator:
Here is the process flow I suggest:
* Make sure the content only consists of the items allowed in our system, i.e. H1, H2, H3, Normal Text, Note-Box, Itemized list with bullet points, bold and italic. If not, tag the person in charge or communicate with me, or just fix it based on your best understanding.
* Our golden database in the Google Doc, so do NOT change anything in html unless it is changed on the Google Doc.
* Put the content for a single H1 in a separate temporary Google Doc
* Extract the document as Markdown, there are different Chrome Plugins for this.
* Make sure the Markdown does not have an invalid item.
* Run the code on input.md and it generates the html for you in output.html
* You can first test the html on your computer, but that is NOT enough, it needs to be pushed and viewed to make sure all iconos are correct.


## Important notes and current shortcomings:
* NO dots in H1 (and probably H2) strings. 
* Links from Google Doc and Markdwon are not correctly translated. 
