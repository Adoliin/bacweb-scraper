# Bacweb Scraper
A simple python program to download all tests of the "Tunisian Baccalaureate"
of all available sections.
## Getting Started

### Prerequisites
As specified in the "pyproject.toml", these are the modules dependencies for this project:
- python 3.9
- requests
- bs4
- lxml

External dependency:
- wget (for downloading the tests PDFs)
 
### Installing
To install it just do so by pressing the "Code" button and then press "Download ZIP".
Or by git cloning this repository like this:
`git clone https://github.com/adoliin/bacweb-scraper`

## Usage
From GUI:
Go to the project folder and press the "main.py" file

From command line:
Go to the project directory to the:
`cd bacweb-parser`
And execute the program:
`python main.py`

After executing the program, a menu will appear and you can
type the number of the section you want to download the tests from or
type "8" to download all available tests from all sections.
The program will then create a "bac" directory containing all the tests ordered
by year.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
