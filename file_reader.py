def format_data(filename):
    data_file = open(filename, "r")
    data = data_file.readline()
    data = data.split()
    return [float(i) for i in data]
