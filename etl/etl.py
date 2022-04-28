def transform(legacy_data):
    output = {}
    for element in legacy_data:
        temp = legacy_data[element]
        for i in range(len(temp)):
            output[temp[i].lower()] = int(element)
    return output