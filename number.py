# source: https://github.com/kurokourou/vnese_preprocessing
# được sửa lại cho phù hợp với project 
class NumberProcessing:
    ''' Đọc số 
    '''
    def __init__(self):
        self.digits = ['0','1','2','3','4','5','6','7','8','9']
        self.reads = ['không','một','hai','ba','bốn','năm','sáu','bảy','tám','chín']
        self.stack = ['','nghìn','triệu']
    
    @staticmethod
    def is_number(number):
        return number.strip().isdigit()
    
    @staticmethod
    def number_clean(number,clear_head=True):
        if len(number) == 0:
            return number
        if number.isdigit():
            temp = number 
        else:
            temp = ''.join([x for x in list(number) if x.isdigit()])
            print(temp)
        if clear_head:
            return str(int(temp))
        else:
            return temp
    
    # Đọc số 
    def is_zero(self, text):
        if len(text) != 0:
            for c in text:
                if c is not '0':
                    return False
        return True
    def read_digit(self, digit):
        if digit in self.digits:
            return self.reads[self.digits.index(digit)]
        else:
            print('%s không hợp lệ')
            return None 
    
    def normal(self, number):
        ''' Đọc số theo cách thường 
        '''        
        nums = list(self.number_clean(number,False))
        return ' '.join([self.read_digit(x) for x in nums])

    def three(self, number):
        ret = []
        if len(number) == 3:
            if number != '000':
                ret.append(self.read_digit(number[0]))
                ret.append('trăm')
                if number[1:] != '00':
                    [ret.append(x) for x in self.two(number[1:])]
        elif len(number) < 3:
            return self.two(number)
        return ret 

    def two(self, number):
        ret = []
        try: # number != ''
            if int(number) != 0:
                if len(number)== 2:
                    # Chữ số đầu 
                    if number[0] == '0':
                        ret.append('linh')
                    elif number[0] == '1':
                        ret.append('mười')
                    else:
                        ret.append(self.read_digit(number[0]))
                        ret.append('mươi')
                    # Chữ số cuối 
                    if number[1] == '1':
                        if int(number[0]) > 1:
                            ret.append('mốt')
                        else:
                            ret.append('một')
                    elif number[1] == '4':
                        if int(number[0]) > 1:
                            ret.append('tư')
                        else:
                            ret.append('bốn')
                    elif number[1] == '5':
                        if int(number[0]) > 0:
                            ret.append('lăm')
                        else:
                            ret.append('năm')
                    elif number[1] == '0':
                        pass
                    else:
                        ret.append(self.read_digit(number[1]))  
                else:
                    ret.append(self.read_digit(number))
        except Exception:
            pass
        return ret    
    
    def ubillion(self, number):
        ''' Đọc các số dưới 1 tỷ 
        '''  
        temp = self.number_clean(number)
        ret = []
        if len(temp) < 10:
            residual = len(temp)%3
            times = int(len(temp)/3)
            stacks = [temp[len(temp)-(i+1)*3:len(temp)-i*3] for i in range(times)]
            if residual:
                stacks.append(temp[:residual])
                times += 1
        while(times > 0):
            [ret.append(x) for x in self.three(stacks[times-1])]
            if times > 1 and int(stacks[times-1])!=0:
                ret.append(self.stack[times-1])
            times -= 1    
        return ret 

    def read(self, number):
        ''' Đọc theo cách chia thành cụm 3 chữ số 
        '''
        if self.is_zero(number):
            return ['không']
        temp = self.number_clean(number)
        ret = []
        if len(temp) < 10:
            return self.ubillion(number)
        elif len(temp) in range(10,29):
            residual = len(temp)%9
            times = int(len(temp)/9)
            stacks = [temp[len(temp)-(i+1)*9:len(temp)-i*9] for i in range(times)]
            if residual:
                stacks.append(temp[:residual])
                times += 1
            while(times > 0):
                [ret.append(x) for x in self.ubillion(stacks[times-1])]
                if times > 1:
                    ret.append(' '.join(['tỷ']*(times-1)))
                times -= 1  
        else:
            # print('Số to quá đọc không nổi ...')
            return number
              
        return ret 