import re 


def check_month(word):
    """
    check từ có là dạng .../...
    """
    if  re.search('://', word):
        return word
    dem = 0
    for c in word:
        if c == '/':
            dem+=1
    return dem
def read_month(word):
    """
    convert .../.../... -> ngày tháng năm
    """
    if  re.search('://', word):
        return word
    res = []
    mon = check_month(word)
    if mon == 0:
        return word
    word = word.replace('.', '')
    wos = word.strip().split('/')
    if mon == 1:
        if wos[0].isdigit() == False or wos[1].isdigit() == False:
            return word
        if len(wos[0]) <=2 and len(wos[1]) <= 2 and wos[0].isdigit():
            res.append('ngày')
            res.append(wos[0])
            res.append('tháng')
            res.append(wos[1])
        elif len(wos[0]) <=2 and len(wos[1]) and wos[0].isdigit()==4:
            res.append('tháng')
            res.append(wos[0])
            res.append('năm')
            res.append(wos[1])
        else:
            return word

    else:
        if wos[0].isdigit() == False or wos[1].isdigit() == False or  wos[2].isdigit() == False:
            return word
        res.append(wos[0])
        res.append('tháng')
        res.append(wos[1])
        res.append('năm')
        res.append(wos[2])
    return ' '.join(res)

def check_hours(word):
    """
    check từ có là dạng ...:...
    """
    dem = 0
    for c in word:
        if c == ':':
            dem+=1
    return dem
def read_hours(word):
    """
    convert ...:...:... ->  giờ phút giây
    """
    word = word.replace('.', '')
    mon = check_hours(word)
    if mon == 0:
        return word
    wos = word.strip().split(':')
    # print(wos)
    res = []
    if mon == 1:
        if wos[0].isdigit() == False or wos[1].isdigit() == False:
            return word
        elif len(wos[0]) <=2 and len(wos[1]) <= 2 and len(wos[1]) > 0:
            res.append(wos[0])
            res.append('giờ')
            res.append(wos[1])
            res.append('phút')
        elif int(wos[0]) > 23 and len(wos[1]) <= 2 and len(wos[1]) > 0:
            res.append(wos[0])
            res.append('phút')
            res.append(wos[1])
            res.append('giây')
        else:
            return word

    else:
        if wos[0].isdigit() == False or wos[1].isdigit() == False or  wos[2].isdigit() == False:
            return word
        res.append(wos[0])
        res.append('giờ')
        res.append(wos[1])
        res.append('phút')
        res.append(wos[2])
        res.append('giây')
    return ' '.join(res)

def read_text(text):
    res = [read_month(w) for w in text.strip().split(' ')]
    text = ' '.join(res)
    res = [read_hours(w) for w in text.strip().split(' ')]
    return ' '.join(res)
if __name__ == "__main__":

    print(read_text('23:50 thứ 4 3/7/2021.'))
    # word = "232://020"
    # print(re.search('://', word))
