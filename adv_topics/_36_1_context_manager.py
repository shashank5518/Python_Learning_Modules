# f = open('_36_2_sample_text.txt', 'w')
# f.write('Lorem ipsum dolor sit amet')
# f.close()

# with open('_36_2_sample_text.txt', 'w') as f:
#     f.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')


# class OpenFile():
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode

#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file

#     def __exit__(self, exc_type, exc_val, traceback):
#         self.file.close()

# with OpenFile('_36_2_sample_text.txt', 'w') as f:
#     f.write('Testing')

# print(f.closed)

from contextlib import contextmanager

# @contextmanager
# def open_file(file, mode):
# try:
# f = open(file, mode) # line 1
# yield f # line 2
# finally:
# f.close() # line 3

# with open_file('_36_2_sample_text.txt', 'w') as f: # implication of line 1, upto open()
# f.write('Lorem ipsum dolor sit amet') # implication of line 2 from f to f.write
# line 3 is for everything that executes after contextmanager
# print(f.closed)

import os


@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        # os.chdir('New_Path')
        yield
    finally:
        os.chdir(cwd)


with change_dir("Sample_Dir_One"):
    print(os.listdir())

with change_dir("Sample_Dir_One"):
    print(os.listdir())

print(os.getcwd())
