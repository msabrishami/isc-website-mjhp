# isc-website-mjhp

This is the bootstrap-based project for the information portal of ISC website

## Process Flow in Phase 1

Our golden database in the Google Doc, so do NOT change anything in html unless it is changed on the Google Doc.

The content on Google Doc. is translated into Markdown using a Google Doc's Ad-On (named Docs to Markdown).

The Markdown file is then translated into html, using this script:

```
python3 translator.py markdown-file.md output-html-file-name.html "the title string"
```

**Important notes for content creators and editors on Google Doc.**

* Make sure the content only consists of the items allowed in our process:
* Header 1
* Header 2
* Header 3
* Normal Text
* Note-Box: Create a single cell table and put your alert note in it.
* Itemized list with bullet points
* Bold text
* Italicized text
* comment sections are tagged as shown below:

```

!TODO-START
some notes here
some other notes here 
maybe something else here
!TODO-END
```

* Make sure the Markdown does not have an invalid item.

* You can first test the html on your computer, but that is NOT enough, it needs to be pushed and viewed to make sure all iconos are correct.

## Important notes and current shortcomings:

* NO dots in H1 (and probably H2) strings.
* Links from Google Doc and Markdwon are not correctly translated.

# How to Write a Markdown File

## Images

First, move your picture file in the `images` folder in this directory. Then, in the text, enter the address of file like below in the parenthesis (using no quotation). You can also choose a title for your pic in the brackets.

`![image_title](./images/pic1.png)`

Now, your image must be showed up in the text.

## Links
