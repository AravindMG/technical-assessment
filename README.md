# technical-assessment

In this project we are querying JSON data with Python to calculate the average salary for each jobTitleName categorised by region. Also, this project covers test cases written in pytest to test all the methods.

# tech/framework used

Python, Pandas and Pytest

# source code explanation

First we are loading the JSON data and converting the JSON data to pandas dataframe for easier data transformation operations. Then we are filtering only the necessary columns (jobTitleName, region and salary) needed for the average salary calculation in each region and then we are using the necessary columns to filter each jobTitleName in particular region and finding the average salary by applying mean() in salary column. Finally, we are printing/writing all the data to a output file.

# test cases

1. Checking whether we have filtered all the necessary columns needed to generate our output. Also, check whether the actual and expected dataframes have similar dtypes
2. Checking whether we have filtered developer's from CA region
3. Checking whether we are calculating and printing the correct average salary of developer's from CA region
4. Checking whether we have filtered developer's from FA region
5. Checking whether we are calculating and printing the correct average salary of developer's from FA region
6. Checking whether we have filtered developer's from YA region
7. Checking whether we are calculating and printing the correct average salary of developer's from YA region
8. Checking whether we have filtered program directory from CA region, also program directory is only in CA region
9. Checking whether we are calculating and printing the correct average salary of program directory from CA region
10. Checking whether we have filtered productOwner's from CA region
11. Checking whether we are calculating and printing the correct average salary of program directory from CA region
12. Checking whether we have filtered productOwner's from SA region
13. Checking whether we are calculating and printing the correct average salary of program directory from SA region
14. Checking whether we have filtered productOwner's from SA region
15. Checking whether we are calculating and printing the correct average salary of program directory from YA region

# some important notes

- The source code resides in src folder as avg_salary.py
- The test cases are placed in tests folder as test_avg_salary.py
- The output file is stored in outputs folder as output.txt
