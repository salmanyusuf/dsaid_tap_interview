import pandas as pd

# Prepare summary table
dict = [{"Industry": "A",
         "Median Salary": 3150,
         "Count": 83},
        {"Industry": "B",
         "Median Salary": 3300,
         "Count": 53},
        {"Industry": "C",
         "Median Salary": 2650,
         "Count": 47},
        {"Industry": "D",
         "Median Salary": 2400,
         "Count": 12},
        {"Industry": "E",
         "Median Salary": 4100,
         "Count": 30},
        {"Industry": "F",
         "Median Salary": 3400,
         "Count": 23},
        {"Industry": "G",
         "Median Salary": 2800,
         "Count": 12},
        {"Industry": "H",
         "Median Salary": 2300,
         "Count": 8},
        {"Industry": "Others",
         "Median Salary": 2900,
         "Count": 21},

        {"Industry": "A",
         "Median Salary": 3000,
         "Count": 23},
        {"Industry": "B",
         "Median Salary": 3100,
         "Count": 9},
        {"Industry": "C",
         "Median Salary": 2600,
         "Count": 32},
        {"Industry": "D",
         "Median Salary": 2400,
         "Count": 15},
        {"Industry": "E",
         "Median Salary": 3900,
         "Count": 3},
        {"Industry": "F",
         "Median Salary": 3150,
         "Count": 7},
        {"Industry": "G",
         "Median Salary": 2600,
         "Count": 22},
        {"Industry": "H",
         "Median Salary": 2200,
         "Count": 11},
        {"Industry": "Others",
         "Median Salary": 1900,
         "Count": 28},
        ]

data = pd.DataFrame.from_records(dict)
student_group = ['Student Group X'] * 9 + ['Student Group Y'] * 9
job_nature = (['Closely related to course of study'] * 4 + ['Somewhat related to course of study'] * 4 + [
    'Unrelated to course of study']) * 2
data['Student Group'] = student_group
data['Job Nature'] = job_nature
cols = ['Student Group', 'Job Nature', 'Industry', 'Median Salary', 'Count']
data = data[cols]

