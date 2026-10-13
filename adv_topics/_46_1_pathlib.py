from pathlib import Path

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# BASE_DIR = Path(__file__).resolve().parent.parent

# print(Path.cwd())

# for p in Path().iterdir():
#     print(p)

my_dir = Path("adv_topics")
my_file = Path("resources_for_roadmap.md")

# print(my_dir.name)
# print(my_file.name)

print(my_dir.suffix)
print(my_file.suffix)

print(my_dir.stem)
print(my_file.stem)

# new_file = my_dir / "_46_2_new_file.txt"
new_file = my_dir.joinpath("_46_2_new_file.txt")

print(my_dir.exists())
print(my_file.exists())
print(new_file.exists())

print(my_dir.parent)
print(my_file.parent)
print(new_file.parent)
print(new_file.parent.parent)  # same as my_dir.parent

print(my_dir.absolute().parent)
print(my_dir.absolute())

print(my_dir.resolve())

p = Path("..").absolute()
print(p)
p = Path("..").resolve()
print(p)
p = Path(".").resolve()
print(p)
p = Path(__file__).resolve()
print(p)

p = Path("~/dot/files").resolve()
print(p)

p = Path("~/dot/files").expanduser()
print(p)

p = Path.home() / "dotfiles"
print(p)

dotfiles = Path.home() / "dotfiles"

for p in dotfiles.glob("*vscode*", case_sensitive=False):
    print(p)
for p in dotfiles.rglob("*vscode*", case_sensitive=False):
    print(p)
for p in dotfiles.rglob("*.json", case_sensitive=False):
    print(p)

# with dotfiles.open() as f:
#     print(f.read())

# with open(dotfiles) as f:
#     print(f.read())

# p = Path("TempDir/SubDir")
# p.mkdir(parents = True)
# p.rmdir()

# p = Path("Temp_File.txt")
# p.touch()
# p.rename('temp_file.txt')
# p.replace('temp_file_1.txt')

p = Path("temp_file_1.txt")
p.unlink()
