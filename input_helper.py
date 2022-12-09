def convert_data_to_list(file_name):
    new_list = []
    with open(file_name) as f:
        for line in f:
            new_list.append(line.strip())
    return new_list