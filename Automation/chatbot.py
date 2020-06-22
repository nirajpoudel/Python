import re
log = 'December 01 05:21:40 my computer bad_process[12345]: Error performing package upgrade'
def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex,log_line)
    if result is None:
        return ''
    return result[1]
print(extract_pid(log))
12345
