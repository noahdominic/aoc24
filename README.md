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

To execute the solution for a specific day and a specific part, you can run the Python script using the following command:

```bash
pypy main.py day=<day_number> part=<part_number> [final]
```

### Parameters
- **day**: Specifies the day number of the challenge you want to run. Replace `<day_number>` with the desired day (e.g., `day=2`).
- **part**: Specifies the part of the challenge for the given day. Replace `<part_number>` with the desired part (e.g., `part=3`).
- **final** *(optional)*: If provided, runs the script in "final" mode. If omitted, the script defaults to "test" mode.

### Examples
#### Run the script for Day 2, Part 3 using the test input shown in the puzzle text (default):
```bash
pypy main.py day=2 part=3
```

#### Run the script for Day 2, Part 3 in with the final, larger input:
```bash
pypy main.py day=2 part=3 final
```

## Licence

This repository is licensed under the **Simplified BSD Licence**.  See the [LICENCE](LICENCE) file for details.

Thank you for visiting my repository!  I hope these solutions inspire you or help you solve your own Advent of Code puzzles. 😊
