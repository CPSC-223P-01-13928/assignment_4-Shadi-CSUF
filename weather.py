import json

# The function should open the filename in read mode and return a dictionary of the JSON decoded contents of the file.
# If the file does not exist, the function should accept the FileNotFoundError and return an empty dictionary.
def read_data(fileName):
    try:
        with open(fileName, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def max_tempature(data, date):
    x = 0
    for key in data:
        if data == key[0:8]:
            if data[key]['t'] > x:
                x = data[key]['t']
    return x

def max_hunmidity(data, date):
    x = 999
    for key in data:
        if data == key[0:8]:
            if data[key]['h'] > x:
                x = data[key]['h']
    return x

def min_tempature(data, date):
    x = 9999
    for key in data:
        if data == key[0:8]:
            if data[key]['t'] < x:
                x = data[key]['t']
    return x

def tot_rain(data, date):
    x = 0
    for key in data:
        if data == key[0:8]:
            x += data[key]['r']
    return x

# The function should open the filename in write mode and write the dictionary data into the file encoded as JSON.
def write_data(fileName, data):
    with open(fileName, 'w') as f:
        json.dump(data, f)