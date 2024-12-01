# Advent of Code 2024 – Python Solutions

Welcome to my **Advent of Code 2024** repository!  This repository contains my Python solutions for the daily coding challenges from [Advent of Code 2024](https://adventofcode.com/2024), which gives out two puzzles each day from 1&nbsp;December to Christmas day 25&nbsp;December.

## Folder Structure

The project is organised as follows:

```
.
├── aoc00.py               # Solution for day 0 (optional or preparatory task)
├── aoc01.py               # Solution for day 1
├── ...                    # Other solution files...
├── input/                 # Folder containing input files for each day (not included)
│   └── 01.txt             # Example input file for day 1
│   └── ...                # other solution files
└── main.py                # Entry point to run solutions
```

## A Note on Input Files

In accordance with the request by the Advent of Code developers, **input files are not included in this repository**.  Each participant receives personalised input files.  To run the solutions, you must download your own input files from the [Advent of Code website](https://adventofcode.com/2024) and save them in the `input/` directory using the naming convention `XX.txt` (e.g., `01.txt` for day 1).

## Usage

To execute the solution for a specific day, you can modify `main.py` to customise the days or solutions to run.
 Simply import the module for the day along with the needed functions.

Each day's module will be under the naming format `aocXX` with `XX` representing a 2-digit representation of the day number; for example, day 1 will be `aoc01`.  In them are two functions needed for the day in the naming format `day[2-digit day number]_[2-digit part number]`; for example, the part 2 solution is stored as `day01_02`.

To run, for example, parts 1 and 2 of day 1, simply modify **main.py** to be:

```python
from aoc01 import day01_01, day01_02

def main ():
    day01_01()
    day01_02()

if __name__ == "__main__":
    main()
```

## Licence

This repository is licensed under the **Simplified BSD Licence**.  See the [LICENCE](LICENCE) file for details.

Thank you for visiting my repository!  I hope these solutions inspire you or help you solve your own Advent of Code puzzles. 😊
