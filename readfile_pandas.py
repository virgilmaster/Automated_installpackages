import pandas


def read_tablemethod(filename):
    data = pandas.read_table(filename, header=None, delim_whitespace=True)
    return data


if __name__ == "__main__":
    data = read_tablemethod('requirements.txt')
    print(data)
