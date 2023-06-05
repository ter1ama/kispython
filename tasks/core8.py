import re


def main(string):
    string = string.replace('\n', ' ')
    key = re.compile('[a-zA-Z_?0-9*]+ *=> *[a-zA-Z_?0-9*]+')
    key1 = key.findall(string)
    final_list = []
    for i in key1:
        key2 = i.split('=>')
        rtemp = key2[0]
        rpart = rtemp.strip()
        ltemp = key2[1]
        lpart = ltemp.strip()
        temp = (lpart, rpart)
        final_list.append(temp)

    return final_list
