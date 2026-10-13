import os

# print(dir(os))

print(os.getcwd())

# os.chdir('new_path')


print(os.listdir())

# os.mkdir('_15_2_demo_file')
# os.makedirs() # to make subdirectories as well as top level

# os.rmdir('_15_2_demo_file')
# os.removedirs() # delete subdirectories as well

# os.rename('_15_os_module.py', '_15_1_os_module.py')

from datetime import datetime

print(os.stat("_8_1_modules_std_library.py"))
print(os.stat("_8_1_modules_std_library.py").st_size)
print(os.stat("_8_1_modules_std_library.py").st_mtime)
mod_time = os.stat("_8_1_modules_std_library.py").st_mtime
print(datetime.fromtimestamp(mod_time))

# os.walk() # yields 3 values
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print(f"Current Path: {dirpath}")
    print(f"Directories: {dirnames}")
    print(f"Files: {filenames}")
    print()

# print(os.environ.get(''))

# os.path.join(, )
# os.path.basename('path')
# os.path.dirname('path')
# os.path.split('path')
# os.path.splitext('path')
# os.path.exists('path') # bool
# os.path.isdir('path') # bool
# os.path.isfile('path') # bool
