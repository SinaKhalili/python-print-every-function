# python-print-every-function
Take a file or folder of files and add a print log of the function name and arguments to every function. For my fellow print debuggers.

If you're looking for actual sophisticated tracing, look at the various [SO answers](https://stackoverflow.com/questions/8315389/how-do-i-print-functions-as-they-are-called) and the stdlib's [trace module](https://docs.python.org/3/library/trace.html). This is just a quick n dirty.

## Usage

First grab the `print_every_function.py` file. 

Then use it like so
```shell
python print_every_function.py [FILE OR FOLDER]

# For example
python print_every_function.py test.py
# => Created new python file with logging statements at test.py.log.py

python print_every_function.py test_folder
# => Created a copy of the source files with logging statements in a new folder test_folder__log
```

This will turn 

```python
def func(interval):
    a = [i for i in range(interval)]
    return a
```
into
```python
def func(interval):
    print(f'func({interval})', 'test.py')
    a = [i for i in range(interval)]
    return a
```
for every function. 

Giving, for example, `func2(21) test.py` as an ouput.

If you're changing the source in a loop but want to keep
the print statements, and you rerun `python test.py` from your terminal every time 
you can rerun something like
```shell
rm test.py.log && python print_every_function.py test.py && python test.py.log.py
```
