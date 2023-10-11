
def pageCount(n, p):
    # Write your code here
    from_beginning = int(p/2)
    from_end = int(n/2)-from_beginning

    return min(from_beginning,from_end)


