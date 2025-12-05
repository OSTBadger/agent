from functions.get_files_info import get_files_info

def results(arg1,arg2):
    result = get_files_info(arg1,arg2)
    print(f'Result for \'{arg2}\' directory:\n{result}')


results("calculator", ".")
results("calculator", "pkg")
results("calculator", "/bin")
results("calculator", "../")