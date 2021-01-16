# Bacweb Scraper
A simple python program to download all tests of the "Tunisian Baccalaureate"
of all available sections.
# Getting Started

## Prerequisites
As speciefied in the "pyproject.toml", these are the modules dependancies for this project:
- python 3.9
- requests
- bs4
- lxml

External dependancy:
- wget (for downloading the tests PDFs)
 
## Installing
To install it just do so by pressing the "Code" button and then press "Download ZIP".
Or by git cloning this repositopry like this:
`git clone https://github.com/adoliin/bacweb-scraper`

# Usage
From GUI:
Go to the project folder and press the "main.py" file

From command line:
cd to the project diretory to the `cd bacweb-parser`
And execute it `python main.py`

After executing the program you a menu will appear and you can
type the number of the section you want to download the tests from or
type "8" to download all available tests from all sections.
The program will then create a "bac" directory containing all the tests ordered
by year.
