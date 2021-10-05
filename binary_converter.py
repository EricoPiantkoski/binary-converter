import os

def singlecalc(binary, index):
    if binary == 1:
        return 2**index
    else:
        return 0

def init():    
    raw = []
    result = 0
    binary_value = input('enter a binary value to be converted to decimal: ')
    #print(type(len(binary_value)))
    for index in range(len(binary_value)):
        print('index', index)
        print('value[index]: ', binary_value[index])
        if int(binary_value[index]) != 0 and int(binary_value[index]) !=1:
            return 'wrong'
        raw.append(singlecalc(int(binary_value[index]), index))
        print(raw)
    for item in raw:
        result += item
    return result
    
    #print('equivalent decimal value: ', result, '\n\n')

if __name__ == '__main__':
    while True:
        result = init()
        if result == 'wrong':
            os.system('clear')
            print('wrong value entered')
            continue
        else: 
            print('equivalent decimal value: ', result, '\n\n')
            while True:
                decision = input('do you want to do a new conversion? y/n: ')
                if decision.lower() == 'n':
                    exit()
                elif decision.lower() == 'y':
                    break
                else:
                    continue
    