# PrismForce_Assignment
This code generates a balance sheet from input expense and revenue data in JSON format, providing monthly totals and amounts. It utilizes the json and datetime modules for data manipulation and outputs the balance sheet in JSON format.


This repository contains code that generates a balance sheet from input data in JSON format. The code reads an input JSON file, extracts expense and revenue data from it, and calculates the monthly revenue and expense totals. It then generates a balance sheet that includes the balance amount for each month. The balance sheet is outputted in JSON format.

The main function in the code is form_balance_sheet, which takes the input data as a parameter and returns the balance sheet as a list of dictionaries. The code uses the json module to read and write JSON files, and the datetime module to handle date and time calculations.

To use the code, you need to provide an input JSON file containing the expense and revenue data. The file should be named 2-input.json and placed in the same directory as the code file. After running the code, the balance sheet will be printed in JSON format.

Please note that this code is a standalone script and doesn't include any additional functionality or integration with other systems.
