# Markdown_to_Anki
## A little script to convert my (albeit incredibly specific) flashcards in markdown, to CSV format for import into anki.
---
### What is it?
If you make your flascards in markdown files, in the specific format:
```
Question?
  - answer
  - more answer
More question?
  - even more answer
And why not {{c1::a cloze::something}} for good measure
```
This script can be used to quickly turn this markdown file into 2 CSV files: The first will be the normal flashcards, the second will be the cloze flashcards (which must be imported in to anki seperately).

### How to use?
Start by downloading the python script, ensuring python is installed.
Open the terminal, and type:
```
cd ~/Directory/with/script
python mdcsv.py "~/Path/to/md/file/file.md"
```
This will generate two files, `file.csv` and `file_cloze.csv` in the same directory. As images are not supported, there will also be a terminal output for any flashcard that contains an image, this will need to be delt with manually.

To import into anki, ensure the seperator is a comma, and the card type is "basic" for the normal file,  and "cloze" for the cloze file. 
