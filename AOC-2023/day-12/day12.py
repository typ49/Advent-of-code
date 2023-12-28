def count(cfg, nums):
    if cfg == "":
        return 1 if nums == () else 0

    if nums == ():
        return 0 if "#" in cfg else 1

    result = 0
    
    if cfg[0] in ".?":
        result += count(cfg[1:], nums)
        
    if cfg[0] in "#?":
        if nums[0] <= len(cfg) and "." not in cfg[:nums[0]] and (nums[0] == len(cfg) or cfg[nums[0]] != "#"):
            result += count(cfg[nums[0] + 1:], nums[1:])

    return result

def day12(filepath):
    total = 0
    with open(filepath, 'r') as f:
        for line in f:
            cfg, nums = line.split()
            nums = tuple(map(int, nums.split(",")))
            total += count(cfg, nums)

    return total

# main
filepath = "./input.txt"
print(day12(filepath))