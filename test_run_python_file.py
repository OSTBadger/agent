from functions.run_python_file import run_python_file

def results(arg1,arg2,arg3=None):
    result = run_python_file(arg1,arg2,arg3)
    print(f'Result for \'{arg2}\' result:\n{result}')


results("calculator", "main.py")
results("calculator", "main.py", ["3 + 5"])
results("calculator", "tests.py")
results("calculator", "../main.py")
results("calculator", "nonexistent.py")
results("calculator", "lorem.txt")