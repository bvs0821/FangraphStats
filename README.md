# FangraphStats

FangraphStats is a projected intended to help users more easily analyze baseball statistics compiled from fangraphs.com.

Fangraphs organizes hitter and pitcher statistics in many tables (Standard, Advanced, etc.). This program scraps all hitter and pitcher statistics and outputs a .db and .xlsx files of the fangraphs tables.

User are able to input the number of days they want statistics from, the qualifying number of at bats/inning pitched to be considered, and the number of hitters/pitchers stats are accrued from.

## Usage

The program is ran one of two ways (using Python v3.9), depending on whether the user wants .xlsx and .db files or only .db files.

For both .db and .xlsx output:

```python
python3.9 fangraphexcelexport.py
```

For only .db output:

```python
python3.9 fangraphcompiledb.py
```

Regardless of the entry point, user is then prompted to input the number of days they want stats from (starting from current day). User inputs integers with a space between (creating a list).

Example of requesting statistics from last 5, 10, and 15 days.

```python
"Enter the amount(s) of days you are analyzing: "
5 10 15
```

The user then inputs the minimum number of at bats required to be included as a single integer (based on at bats that occurred in the inputted date range), see below for 5 at bat minimum:

```python
"Enter minimum number of at bats for hitter: "
5 
```

Next, the user inputs the number of hitters (as a single integer) to be included in outputted tables, see below for 50 hitters:

```python
"Enter number of hitters displayed: "
50 
```

The user is prompted to input the same for the minimum innings pitched and number of pitchers to be included. Both require single integer inputs.

Finally, the program outputs .db (and .xlsx) files in the format:

fangraph_{}days.db with {} holding the number of days analyzed.

fangraph_{}days.xlsx with {} holding the number of days analyzed.

## Contact
For inquiries about the project, please email bvs0821@yahoo.com