print("hello world")

message = "heLLo bois"
print(message)

message_in_double_quotes = "hello's world's"
print(message_in_double_quotes)

message_in_double_quotes_backslash = 'hello "escape sequence"'
print(message_in_double_quotes_backslash)

multi_line_message = """
Bobby's world was a good
cartoon in the 1990's
"""
print(multi_line_message)

print(len(multi_line_message))
print(len(message_in_double_quotes_backslash))

print(message[:])
print(message[:2])
print(message[3:])
print(message[::2])
print(message[:-1])

print(message.upper())
print(message.lower())
print(message.title())
print(message.capitalize())

print(message.count("L"))
print(message.find("L"))  # returns index else -1 if not found
print(message.count("x"))
print(message.find("x"))  # returns index else -1 if not found

new_message = message.replace("bois", "world")
print(message)
print(new_message)

concatenated_string = message + " " + new_message
print(concatenated_string)

print(f"{message.lower()} how you doing? check out {new_message.upper()}")

print(dir(message))
# print(help(str))
