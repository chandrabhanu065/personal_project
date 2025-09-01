import re
def log_parsing(filepath):
    error_pattern = re.compile(r'(.*(?:ERROR|error).*)', re.MULTILINE)
    with open(filepath, 'r') as f:
        content = f.read()
    Error_message = error_pattern.findall(content)
    return Error_message

if __name__ == '__main__':
    filepath = '/Users/chandrabhanu/Documents/LOG_FILE/log_1.txt'
    result = log_parsing(filepath)
    print("Errors in log file {}".format(result))