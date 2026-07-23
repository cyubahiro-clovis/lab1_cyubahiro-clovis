#!/bin/bash
# organizer.sh - archives grades.csv with a timestamp and logs the operation

# 1. Make sure the archive directory exists
if [ ! -d "archive" ]; then
    mkdir archive
fi

# 2. Build a timestamp like 20260722-181530
TIMESTAMP=$(date +"%Y%m%d-%H%M%S")

# 3. Refuse politely if there is nothing to archive
if [ ! -f "grades.csv" ]; then
    echo "Error: grades.csv not found in the current directory. Nothing to archive."
    exit 1
fi

# 4. Move grades.csv into the archive with its new timestamped name
NEW_NAME="grades_${TIMESTAMP}.csv"
mv grades.csv "archive/${NEW_NAME}"

# 5. Leave a fresh empty grades.csv behind
touch grades.csv

# 6. Append this operation to the log (>> accumulates)
echo "${TIMESTAMP} | original: grades.csv | archived as: archive/${NEW_NAME}" >> organizer.log

echo "Archived grades.csv to archive/${NEW_NAME}"
echo "A fresh empty grades.csv is ready for the next batch."
