# table2x

Convert SQLITE tables to CSV, MS Excel, MS Word, ODS, JSON, and LaTex

# Version

![](https://img.shields.io/badge/Version%3A-1.0-success)

# Release date

![](https://img.shields.io/badge/Release%20date-Mar%2C%2014%2C%202023-9cf)

# License

![](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)

# Programming language

<img src="https://img.icons8.com/?size=512&id=13441&format=png" width="50"/>

# OS

<img src="https://img.icons8.com/?size=512&id=17842&format=png" width="50"/> <img src="https://img.icons8.com/?size=512&id=122959&format=png" width="50"/> <img src="https://img.icons8.com/?size=512&id=108792&format=png" width="50"/>

# Requirements

```bash
pip install pandas==2.1.2 openpyxl==3.1.2 docx==0.2.4
```

or

```bash
pip install -r requirements.txt
```

```python
import sqlite3
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from docx import Document
import json
```

# Function list

1. export_to_excel
2. export_to_libreoffice_calc
3. export_to_csv
4. export_to_word
5. export_to_json
6. export_to_latex

All these functions have the same input parameters and as output the file in the format associated with the function.


> Input arguments
>
>> `db_name`: The name of the SQLite database file.
>> 
>> `table_name`: The name of the table in the database you want to export.
>> 
>> `output_filename`: The name of the output JSON file where the exported data will be saved.
>> 
>> `selected_columns` (optional): A list of column names you want to export. If provided, only the specified columns will be exported. If not provided, all columns in the table will be exported.
>
> Returns:
> 
>> None

# How to run

```python
databasename = "news.db"
tablename = "news"
excel_filename = "exported_data.xlsx"
ods_filename = "exported_data.ods"
csv_filename = "exported_data.csv"
word_filename = "exported_data.docx"
json_filename = "exported_data.json"
latex_filename = "exported_data.tex"

selected_columns = ["title", "source", "relevance"]

export_to_word(databasename, tablename, word_filename, selected_columns)
export_to_excel(databasename, tablename, excel_filename, selected_columns)
export_to_libreoffice_calc(databasename, tablename, ods_filename, selected_columns)
export_to_csv(databasename, tablename, csv_filename, selected_columns)
export_to_json(databasename, tablename, json_filename, selected_columns)
export_to_latex(databasename, tablename, latex_filename, selected_columns)
```
