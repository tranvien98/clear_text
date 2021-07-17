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
    wos = word.strip().split('/')
    if mon == 1:
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
        res.append(wos[0])
        res.append('tháng')
        res.append(wos[1])
        res.append('năm')
        res.append(wos[2])
    return ' '.join(res)
def read_text(text):
    res = [read_month(w) for w in text.strip().split(' ')]
    return ' '.join(res)
if __name__ == "__main__":

    print(read_text('thứ 4 3/7'))
