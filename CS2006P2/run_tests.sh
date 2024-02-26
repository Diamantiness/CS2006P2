#!/bin/bash

# Find all test files in the current directory and subdirectories
test_files=$(find . -name 'test*.py')

# Loop through each test file and run it using unittest
for file in $test_files; do
    echo "Running tests in $file ..."
    python "$file"
done
