with open('file.txt', 'mode') as alias:
    position  = 0
    alias_contents = alias.read()
    alias_contents_limit = alias.read(100)
    alias_content = alias.readline()
    alias_contents_lines = alias.readlines()
    print(alias_contents)

    alias.seek(position)
    alias.write("Content")
    
    for line in alias:
        print(line, end = '')

with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

