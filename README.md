# Lab1: Grade Evaluator & Archiver

A python application that evaluates a student's academic standing from a CSV file of course grades, plus a Bash script that archives the data file with a timestamp and keeps a persistent log.

## Files
grade-evaluator.py: the grade evaluation program
organizer.sh: the archiving shell script 
grades.csv: sample course data used by the program

## How to run the Python application

python3 grade-evaluator.py

The program then:
1. Reports a missing file politely and refuses an empty file 
2. Validates that every score is between 0 and 100
3. Validates the weights: total must be 100, formative 60, summative 40
4. Calculates the final grade, the GPA = (Total Grade / 100) * 5.0,
and the percentage earned in each category
5. Prints PASSED only if both coategories are at or above 50 percent, otherwise FAILED
6. Lists the failed formative assignments carrying the highest weight as eligible for resubmission. If several share the highest weight, all of them are shown.

Expected output with the included grades.csv:
Final Grade 60.00, GPA 3.000, Status PASSED, and both Group Exercise and Functions and Debuggung Lab listed for resubmission.

## How to run the shell script

 bash organizer.sh

The script creates the archive directory if it does not exist, moves grade.csv into it renamed as grades_YYYYMMDD-HHMMSS.csv, creates a fresh empty grades.csv for the next batch, and appends the operation details to organizer.log. The log accumulates one line per run.

Author: Cyubahiro Clovis
