class logParsing:
    def __init__(self, readpath, writepath):
        self.readpath = readpath
        self.writepath = writepath

    def read(self):
        with open(self.readpath, 'r') as f:
            content = f.read()
            return content


    def read_log_extraction(self):
        #with open(readpath, 'r') as f:
         #   content = f.read()
        content = self.read()
        import re
        regex = re.compile("(.*(?:ERROR|error).*)", re.MULTILINE | re.IGNORECASE)
        error_message = re.findall(regex, content)
        #print(error_message)
        return error_message

    def write_log_in_file(self):
        content = self.read_log_extraction()
        content_str = ''.join(content)
        with open(self.writepath, 'w') as f:
            f.write(content_str)

readpath = '/Users/chandrabhanu/Documents/LOG_FILE/log_2.txt'
writepath = '/Users/chandrabhanu/Documents/LOG_FILE/write_log_2.txt'
obj = logParsing(readpath,writepath)
obj.read_log_extraction()
obj.write_log_in_file()