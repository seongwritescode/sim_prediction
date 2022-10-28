def double_number(number):
    for idx in range(0, len(number)-1,1):
        str_numbers = number[idx] + number[idx+1]
        print(str_numbers)
        for _idx in range(idx+2, len(number) -1, 1):
            str_numbers_ss = number[_idx] + number[_idx+1]
            if str_numbers == str_numbers_ss:
                return str_numbers
    return '-1'

double_number('967619933')
