from functions.get_file_contents import get_file_content

def results(arg1,arg2):
    result = get_file_content(arg1,arg2)
    print(f'Result for \'{arg2}\' directory:\n{result}')

results("calculator", "lorem.txt")
results("calculator", "main.py")
results("calculator", "pkg/calculator.py")
results("calculator", "/bin/cat") 
results("calculator", "pkg/does_not_exist.py") 