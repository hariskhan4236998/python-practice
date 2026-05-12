def large():
    threshold = 3
    results = []

    for x in range(10):
        x += 1

        if x > threshold:
            results.append(x)

    if results:
        return "Greater values: " + str(results)
    else:
        return "No large Numbers....!"


print(large())