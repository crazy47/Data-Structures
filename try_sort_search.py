import random

def binarysearch(_num, _sample_set):
    _low = min(_sample_set)
    _high = len(_sample_set) -1
    _mid = 0

    while _low <= _high:
        _mid = (_low + _high) // 2
        if _num > _sample_set[_mid]:
            _low = _mid + 1
        elif _num < _sample_set[_mid]:
            _high = _mid - 1
        else:
            print(f" number {_num} IN index {_mid}")
            return True
    print(f" number {_num} NOT in array")
    return False
            
def buublesort(_arr, _num):
    for i in range(len(_arr)):
        for j in range(0, len(_arr)-i-1):
            if _arr[j] > _arr[j + 1]:
                _arr[j], _arr[j + 1] = _arr[j + 1], _arr[j]
    print(_arr, end=" ") # print each test case sorted
    binarysearch(_num, _arr) # send sorted testcase to binarysearch
    

if __name__ == "__main__":
    def _test_case_generator():
        for i in range(5): # 5 set of test case
            _fill = []
            for _num in range(10):
                num = random.randint(-10, 10)
                if num in set(_fill):
                    continue
                _fill.append(num)
            random_int_guess = random.randint(-10, 10)
            buublesort(_fill, random_int_guess)
    _test_case_generator()