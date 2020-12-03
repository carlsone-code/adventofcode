def get_input():
    # TODO: need better way to locate input file. define root dir?
    input_file = 'input.txt'
    with open(input_file) as f:
        return f.readlines()
