# Python-Xml-To-Sqlite

This Python script extracts data from an XML file and stores the data in a SQLite database. The XML file contains information about music tracks, and the database stores the data in three tables: "Artist", "Album", and "Track".

## Requirements

- Python 3
- sqlite3 library
- xml.etree.ElementTree library

## Usage

1. Run the script on a terminal:

    'python main.py'

2. The data from the XML file will be stored in the "Artist", "Album", and "Track" tables in the Musicdb.sqlite database.

3. Open the Musicdb.sqlite file in a SQLite database browser.

## Files

- 'main.py': The Python script that extracts the data from the XML file and stores the data in the SQLite database.

- 'Library.xml': The sample XML file containing information about music tracks.

- 'Musicdb.sqlite': The SQLite database where the data is stored.

## Contribution

If you would like to contribute to this project or you do find a way to improve the code, please fork the repository and create a pull request.
