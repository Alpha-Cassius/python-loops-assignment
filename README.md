# Weekly Temperature Analysis

**Student Name:** Vaibhav Pandey
**Roll Number:** IITP_AIML_2602282
**Assignment:** Python Loops & Automation - Subjective Question

## Overview
This project contains a Python script (`temperature_analysis.py`) designed to analyze weekly temperature data. The script demonstrates the use of fundamental Python control structures, including `for` loops, conditional logic (`if`), and loop control statements (`break` and `continue`).

## Project Structure
* `temperature_analysis.py`: The main source code containing solutions for all three tasks.
* `README.md`: This documentation file.

## Tasks and Logic Implemented

### Task 1: Find Maximum and Minimum
**Objective:** Identify the highest and lowest temperatures in a list without using built-in `max()` or `min()` functions.
* **Logic:** The script initializes variables with the first element of the list. It iterates through the remaining temperatures, comparing each one to the current recorded maximum and minimum, updating the variables if a higher or lower value is found.
* **Input:** `[28, 32, 35, 29, 31, 27, 30]`
* **Output:** Highest: 35°C, Lowest: 27°C

### Task 2: Count Hot Days
**Objective:** Count days with temperatures above 30°C, explicitly using the `continue` statement.
* **Logic:** The script loops through the temperature list. If a temperature is 30°C or lower, the `continue` statement is triggered to skip the current iteration. If the temperature is above 30°C, the counter increments.
* **Input:** `[28, 32, 35, 29, 31, 27, 30]`
* **Output:** Hot Days (>30°C): 3

### Task 3: Alert System
**Objective:** Monitor temperatures and stop execution immediately if a threshold (40°C) is reached using `break`.
* **Logic:** The script monitors daily temperatures. If a reading of 40°C or higher is detected, the `break` statement terminates the loop immediately, printing an alert and the day number. It also counts hot days that occurred *before* the alert.
* **Input:** `[28, 32, 35, 40, 31, 33, 30]`
* **Output:** Hot Days before alert: 2, Alert on Day 4.

## How to Run
1. Ensure you have Python installed on your system.
2. Navigate to the directory containing the file.
3. Run the following command in your terminal or command prompt:

```bash
