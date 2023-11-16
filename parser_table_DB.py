import re

def data_open():
    str = ''
    with open('/path/name.txt', mode='r+',encoding="utf8")  as file_data:

        for line in file_data.readlines():
            reg = re.search("^[-+].*$", line)
            if reg == None:str += line
            else:str += '/tab'
        str = str.replace('\n', '')
        str = str.replace('"', '')
        return str
        file_data.close()

if __name__ == '__main__':
    str = data_open()
    spl = str.split(re.search("\/tab\S*", str).group(0))
    name = []
    name.append(spl[0].split('|'))
    name = name[0]
    example = []
    example.append(spl[1].split('|'))
    example =example[0]
    int =0
    for len in name:
        try:
            print(f'{name[int].replace(" ","")}:{example[int].replace(" ","")}')
            int += 1
        except: continue
