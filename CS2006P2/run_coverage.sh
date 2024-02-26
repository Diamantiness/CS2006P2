#!/bin/bash

# Run the coverage command
coverage run test.py

# Generate HTML report
coverage html

# Open the HTML report in the default web browser
xdg-open htmlcov/index.html
