def replace(string):
    list = []
    count = 1
    new_str = ''
    for s in string:
        list.append(s)
    for i in range(len(list)-1):
        if list[i] == list[i+1] and i != len(list)-2:
            count += 1
        elif list[i] != list[i+1]  and i != len(list)-2:
            new_str = new_str + str(count) + str(list[i])
            count = 1
        elif list[i] == list[i+1] and i == len(list)-2:
            count += 1
            new_str = new_str + str(count) + str(list[i])
            count = 1
        elif list[i] != list[i+1] and i == len(list)-2:

            new_str = new_str + str(count) + str(list[i]) +'1'++ str(list[i+1])
            count = 1
    return new_str
if __name__=="__main__":
    s = 'AAAABCCDAA'
    newstr = ''
    newstr = replace(s)
    print newstr