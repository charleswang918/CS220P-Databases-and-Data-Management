# How to Install

## Using Pycharm(Easiest)

Download PyCharm from the JetBrains website. Use this link: https://www.jetbrains.com/help/pycharm/managing-dependencies.html to install the required packages for this project in the file requirements.txt

## Using Ubuntu/WSL

Create a virtual environment(not required but good practice). Once you activate the virtual environment, in your project folder, run

```bash
pip install -r requirements.txt
```

# How to Run Queries Only

You can run the file "relational_algebra_expressions.py" directly from the terminal using "python3  relational_algebra_expressions.py" or by clicking the run button on PyCharm. The file has a sample query provided. To evaluate one of your queries, scroll to the last three lines of the file.

```python
sql_con = sqlite3.connect("sample220P.db")
result = sample_query.evaluate(sql_con=sql_con)
print(result.rows)
```
Here replace sample_query in the second line with the query you want to evaluate and re-run the file. By default, the file will run the sample_query as shown.

# How to run test framework

To run the test framework fill in your expressions in the file "relational_algebra_expressions.py"(don't forget to uncomment the expression by removing the leading "#") and then run "python3 run_tests.py"
This will pass your queries against the sample database and return Errors or pass values depending on the correctness of your query. Note that passing a test case locally does not mean it will pass on Gradescope against the hidden dataset as your query could be hardcoded or have some other inaccuracy.

# Miscellaneous 

1. Always write your expressions in Relational Algebra and then try to convert to Python.

2. Use "https://pypi.org/project/dbis-relational-algebra" to understand the different operators and how they are called.


