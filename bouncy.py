
def evaluate_number(number : int)->int:
    """main function for calculate the '%' of bouncy numbers
    this function receives the % of numbers bouncy and return the number
    that satisfy this requeriment"""
    if type(number) == int and number >1 and number < 100:
        num = total_numbers = porc = 0
        while porc < number:
            num = num + 1
            clasificate = is_bouncy(str(num))
            result = evaluate(clasificate , num)
            if result:
                total_numbers = total_numbers + 1
            porc = total_numbers * 100 / num
        return num
    return 0

def is_bouncy(number):
    info = [1, 1]
    info[0] = len([(info[0] + 1) for j in range(len(number) - 1) if number[j] >= number[j + 1]]) + 1
    info[1]= len([(info[0] + 1) for j in range(len(number) - 1) if number[j] <= number[j + 1]]) + 1
    return info

def evaluate(list_info , number):
    if list_info[1] == len(str(number)) or list_info[0] == len(str(number)):
        return False
    return True

print(evaluate_number(99))