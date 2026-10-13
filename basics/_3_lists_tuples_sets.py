# lists

courses = ["math", "history", "computer science", "physics"]

print(courses)
print(len(courses))

print(courses[0])
print(courses[-1])
print(courses[len(courses) - 1])
print(courses[:2])
print(courses[1:])
print(courses[::2])

courses.append("art")
print(courses)

courses.insert(0, "biology")
print(courses)

courses_more = ["chemistry", "english"]
# courses.insert(0, courses_more) # adds whole list at index 0
courses.extend(courses_more)
print(courses)
print(courses_more)

courses.remove("history")
print(courses)

courses.pop()
print(courses)
print(courses.pop())
print(courses)

courses.reverse()
print(courses)

courses.sort()
print(courses)
courses.sort(reverse=True)
print(courses)

new_courses_sorted = sorted(courses)  # returns a new sorted list
print(new_courses_sorted)

nums = [1, 2, 3, 4, 5, 6]
print(min(courses))
print(max(courses))
print(sum(nums))

print(courses.index("computer science"))
# print(courses.index('history'))

print("history" in courses)
print("math" in courses)

for course in courses:
    print(course)

for index, course in enumerate(courses, start=1):
    print(f"{index} is {course} :)")

str_courses = " - ".join(courses)
print(str_courses)

new_list = str_courses.split(" - ")
print(new_list)

# tuples -> cannot be modified once created

list1 = ["art", "math", "comp sci"]
list2 = list1

print(list1)
print(list2)

list1[0] = "physics"
print(list1)
print(list2)

tup1 = ("art", "math", "comp sci")
tup2 = tup1

print(tup1)
print(tup2)

print(id(tup1))
print(id(tup2))

# sets - unordered and unique

courses_set = {"art", "history", "math", "comp sci", "art"}
art_courses = {"history", "math", "biology", "design", "art", "math"}
print(courses_set)
print("math" in courses_set)  # optimized for this method

print(courses_set.intersection(art_courses))
print(courses_set.difference(art_courses))
print(courses_set.union(art_courses))
