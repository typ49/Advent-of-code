# github.com/hyper-neutrino

def extrapolate(list):
    """
    find the next number in a sequence
    for example : extrapolate(0, 3, 6, 9, 12, 15) = 15 + extrapolate(3, 3, 3, 3, 3) = 15 + extrapolate(extrapolate(0, 0, 0, 0)) = 15 + 3 - 0 = 18
    
    
    Args:
        list (list of int): the sequence of numbers to extrapolate from
        
    Returns:
        int: the next number in the sequence
    """
    if all(x == 0 for x in list):
        return 0

    new_list = [y - x for x, y in zip(list, list[1:])]
    diff = extrapolate(new_list)
    return list[-1] + diff

total = 0
with open("./day09.txt", 'r') as f:
    for line in f:
        nums = list(map(int, line.split()))
        total += extrapolate(nums)

print(total)