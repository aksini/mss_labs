from datetime import datetime
import math


def random_generator(initial_number=None):
    N = 15
    if not initial_number:
        initial_number = _get_initial_number()
        while len(str(initial_number)) != 4:
            initial_number = _get_initial_number()

    if not isinstance(initial_number, int):
        raise ValueError("Входное значение не является числом!")

    for _ in range(N):
        square_str = str(initial_number ** 2)
        flag = True
        start = 0
        finish = 0
        while len(square_str[start:finish]) != 4:
            if flag:
                flag = False
                start += 1
            else:
                flag = True
                finish -= 1
        if len(str(int(square_str[start:finish]))) != 4:
            start -= 1
            finish -= 1
        initial_number = int(square_str[start:finish])
        yield initial_number


def _get_initial_number():
    now = datetime.now()
    return int(str(now.microsecond)[1:-1])


def math_exp(arr):
    return sum(arr) / len(arr)


def dispersion(arr):
    math_ = math_exp(arr)
    arr = [(math_ - item) ** 2 for item in arr]
    return sum(arr) / len(arr)


def frequency(arr):
    cntLeftNumb = 0
    cntRightNumb = 0
    cntInterval = 0
    math_ = math_exp(arr)
    disp_ = dispersion(arr)
    stDev = math.sqrt(disp_)
    left = math_ - stDev
    right = math_ + stDev
    for item in arr:
        if left <= item <= math_:
            cntLeftNumb += 1
        if right >= item > math_:
            cntRightNumb += 1
        if left <= item <= right:
            cntInterval += 1
    percent_interval = (100 / len(arr)) * cntInterval
    return left, right, percent_interval, cntLeftNumb, cntRightNumb, stDev


def period(arr):
    arr_in_str = ''
    arr = [str(item) for item in arr]
    for s in arr:
        arr_in_str += s
    count_dict = {}
    for s in arr_in_str:
        if s not in count_dict.keys():
            count_dict.update(
                {
                    s: arr_in_str.count(s)
                }
            )
    for num in arr:
        for i, s in enumerate(num[:-1]):
            if s != num[i+1]:
                continue
            if s+s not in count_dict:
                c = 1
            else:
                c = count_dict.pop(s+s)+1
            count_dict.update(
                {
                    s + s: c
                }
            )
        for i, s in enumerate(num[:-2]):
            if s == num[i+1] and s == num[i+2]:
                if s+s+s not in count_dict:
                    c = 1
                else:
                    c = count_dict.pop(s+s)+1
                count_dict.update(
                    {
                        s + s + s: c
                    }
                )
    return dict(
        (item, count_dict.get(item))
        for item in sorted(count_dict)
    )


if __name__ == "__main__":
    arr_ = list(random_generator())
    print('Массив выборки:', *arr_)
    print(f'Математическое ожидание = {math_exp(arr_)}')
    print(f'Дисперсия = {dispersion(arr_)}')
    leftBorder, rightBorder, procentInterval, cntLeftNumb, cntRightNumb, stDev = frequency(arr_)
    print('Среднеквадратичное отклонение = %f' % stDev)
    print('Левая граница = %f' % leftBorder)
    print('Правая граница = %f' % rightBorder)
    print("Процент чисел, попавших в интервал = %d" % procentInterval)
    print('В левой части: %d' % cntLeftNumb)
    print('В правой: %d' % cntRightNumb)
    print('Период генератора:')
    print('число\t количество появлений')
    for key, value in period(arr_).items():
        print(f'{key} \t\t\t {value}')


