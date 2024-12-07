#!/bin/bash

christmas_error() {
    echo "❄️🎄 Ho ho ho! Not today, Grinch! 🎄❄️"
    echo "This script only works between December 1st and 25th!"
    echo "Come back during the magical days of Advent!"
    echo "To get into the Advent of Code spirit, watch this video!"
    xdg-open "https://www.youtube.com/watch?v=_oNOTknRTSU"
    exit 1
}

# Get current date
current_year=$(date +%Y)
current_month=$(date +%m)
current_day=$(date +%d)

# Check if it's December 1st-25th
if [ "$current_month" != "12" ] || [ "$current_day" -lt 1 ] || [ "$current_day" -gt 25 ]; then
    christmas_error
fi

template_file="template.py"

target_dir="${current_year}/day${current_day}"
mkdir -p "$target_dir"

# Generate new filename
new_filename="day${current_day}.py"
full_path="${target_dir}/${new_filename}"

# If the file doesn't exist, copy template
if [ ! -f "$full_path" ]; then
  cp "$template_file" "$full_path"
fi
cd "$target_dir" || exit
python3 "${new_filename}"

# Open files in PyCharm Professional
pycharm-professional example.txt input.txt "${new_filename}"
