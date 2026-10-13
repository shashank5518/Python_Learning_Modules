# f = open('_17_2_test.txt', 'r')

# print(f.name)
# print(f.mode)

# f.close()

with open("_17_2_test.txt", "r") as f:
    # f_contents = f.read()
    # print(f_contents)

    # f_contents = f.readlines()
    # print(f_contents)

    # f_content = f.readline()
    # print(f_content, end='')

    # f_content = f.readline()
    # print(f_content, end='')

    # for line in f:
    #     print(line, end = '')

    # f_contents = f.read(100)
    # print(f_contents, end='')

    # f_contents = f.read(100)
    # print(f_contents, end='')

    # f_contents = f.read(100)
    # print(f_contents, end='')

    # f_contents = f.read(1000)
    # print(f_contents, end='')

    size_to_read = 100
    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end="")
        # print(f.tell())
        # f.seek(position)
        f_contents = f.read(size_to_read)

# print(f.closed)

# print(f.read())

with open("_17_3_test2.txt", "w") as filewrite:
    filewrite.write("hello hello hello")
    filewrite.seek(0)
    filewrite.write("hello chumps")

with open("_17_2_test.txt", "r") as rf:
    with open("_17_4_test3.txt", "w") as wf:
        for line in rf:
            wf.write(line)

# 'rb' and 'wb'
