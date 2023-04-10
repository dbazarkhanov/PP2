import os
import pathlib
import shutil
workWith = input()
if workWith == 'file':
    file_name = input('File\'s name: ')
    while True:
        cmd = input()
        if cmd == 'delete file':
            os.remove(pathlib.Path(file_name))
            print('File was deleted')
        if cmd == 'rename file':
            print('Print new name')
            os.rename(file_name, input())
            print('File\'s name was changed')
        if cmd == 'add content':
            print('Write content')
            with open(file_name, 'a') as f:
                f.write(input())
                f.close()
            print('Content was added')
        if cmd == 'rewrite content':
            print('Write new content')
            with open(file_name, 'w') as f:
                f.write(input())
                f.close()
            print('Content was changed')
        if cmd == 'return to the parent directory':
            shutil.move(pathlib.Path(file_name), pathlib.Path('..'))
        if cmd == 'quit': break
if workWith == 'directory':
    dir_name = input('Directory\'s name: ')
    while True:
        cmd = input()
        if cmd == "rename directory":
            print('Print new name')
            os.rename(os.path.join(os.getcwd(), input()), os.path.join(os.getcwd(), input()))
            print('Name was changed')
        if cmd == "number of files":
            cnt_file = 0
            for _, dirs, files in os.walk('.'):
                cnt_file += len(files)
            print(cnt_file)
        if cmd == "number of directories":
            cnt_dir = 0
            for _, dirs, files in os.walk('.'):
                cnt_dir += len(dirs)
            print(cnt_dir)
        if cmd == "content of the directory":
            print(*[i for i in os.listdir('.')])
        if cmd == "add file":
            with open(input(), 'a') as f:
                f.write('New file')
            print('Files was added')
        if cmd == "add new directory":
            os.mkdir(pathlib.Path(input()))
            print('New directory was added')
        if cmd == 'quit': break