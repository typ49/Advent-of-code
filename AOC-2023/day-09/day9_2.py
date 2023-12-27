def extrapolate(list):
    """
    find the previous number in a sequence
    for example : extrapolate(0, 3, 6, 9, 12, 15) = 0 - extrapolate(3, 3, 3, 3, 3) = 0 - extrapolate(extrapolate(0, 0, 0, 0)) = 0 - 3 - 0 = -3
     
    Args:
        list (list of int): the sequence of numbers to extrapolate from
         
    Returns:
        int: the previous number in the sequence
    """
    if all(x == 0 for x in list):
        return 0

    deltas = [y - x for x, y in zip(list, list[1:])]
    diff = extrapolate(deltas)
    return list[0] - diff


# main
total = 0
with open("./input.txt", 'r') as f:
    for line in f:
        nums = list(map(int, line.split()))
        total += extrapolate(nums)

print(total)