
def matchingStrings(strings, queries):
    # Write your code here
    arr = []
    for a in queries:
        arr.append(strings.count(a))
    return arr



