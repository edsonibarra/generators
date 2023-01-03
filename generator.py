def inclusive_range(start, end):
    for i in range(start, end + 1):
        yield i


for i in inclusive_range(1, 3):
    print(i)
