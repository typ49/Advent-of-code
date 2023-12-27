def hash(s):
    res = 0

    for ch in s:
       res += ord(ch)
       res *= 17
       res %= 256

    return res


def day15p2(filepath):
    f = open(filepath, 'r')
    boxes = [[] for _ in range(256)]
    focal_lengths = {} #dictionary for labels to numbers

    for instruction in f.read().split(','):
        if "-" in instruction:
            label = instruction[:-1]
            index = hash(label)
            if label in boxes[index]:
                boxes[index].remove(label)
        else:
            label, length = instruction.split('=')
            length = int(length)

            index = hash(label)
            if label not in boxes[index]:
                boxes[index].append(label)
            
            focal_lengths[label] = length

    print("boxes : \n", boxes)
    print("focal length : ", focal_lengths)

    total = 0

    for box_number, box in enumerate(boxes, 1):
        for slot, label in enumerate(box, 1):
            total += box_number * slot * focal_lengths[label]

    return total


# main
filepath = "./input.txt"
if __name__ == '__main__':
    print(day15p2(filepath))