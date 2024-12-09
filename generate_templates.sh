#!/bin/bash

# The below code is autogenerated with ChatGPT
# which, of course, wrote it less than perfectly,
# so I had to modify it.
#
# One day they'll write an LLM that works perfectly
# and the world will fill with much rejoicing and trembling.

# Create template Python files for AoC
for i in {8..25}; do
  # Zero-padded day number
  day=$(printf "%02d" $i)
  
  # Filename
  filename="aoc${day}.py"
  
  # Write the template content to the file
  cat <<EOF > $filename
# Advent of Code Day $day

def day${day}_01(input_data):
    """
    Solve part 1 of day $day.
    :param input_data: The input data as a string.
    :return: The solution to part 1.
    """
    pass


def day${day}_02(input_data):
    """
    Solve part 2 of day $day.
    :param input_data: The input data as a string.
    :return: The solution to part 2.
    """
    pass
EOF

  # Notify user
  echo "Created file: $filename"
done

