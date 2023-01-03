def inclusive_range(start, end):
    """
    It will generate a new value till reaches the end
    Values will be generated in a range start and end (inclusive).
    Similar to range() built-in funciton, but this is inclusive in the end param.
    """
    for i in range(start, end + 1):
        yield i


for i in inclusive_range(1, 3):
    print(i)
