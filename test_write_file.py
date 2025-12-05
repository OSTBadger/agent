from functions.write_file import write_file

def results(arg1,arg2,arg3):
    result = write_file(arg1,arg2,arg3)
    print(f'Result for \'{arg2}\' directory:\n{result}')


results("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
results("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
results("calculator", "/tmp/temp.txt", "this should not be allowed")