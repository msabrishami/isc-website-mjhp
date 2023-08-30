# isc-website-mjhp
This is the bootstrap-based project for the information portal of ISC website

## Process Flow in Phase 1

Our golden database in the Google Doc, so do NOT change anything in html unless it is changed on the Google Doc.

The content on Google Doc. is translated into Markdown using a Google Chrome's Add On. 

The Markdown file is then translated into html, using this script: 

```
python3 translator_v2.py markdown-file.md output-html-file-name.html "the title string"
```

**Important notes for content creators and editors on Google Doc.** 
* Make sure the content only consists of the items allowed in our process: 
- Header 1 
- Header 2 
- Header 3 
- Normal Text
- Note-Box: Create a single cell table and put your alert note in it. 
- Itemized list with bullet points
- Bold text 
- Italicized text 

* Make sure the Markdown does not have an invalid item.

* You can first test the html on your computer, but that is NOT enough, it needs to be pushed and viewed to make sure all iconos are correct.


## Important notes and current shortcomings:
* NO dots in H1 (and probably H2) strings. 
* Links from Google Doc and Markdwon are not correctly translated. 
