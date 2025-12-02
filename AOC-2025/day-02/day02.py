def day2(filepath):
    with open(filepath, 'r') as f:
        """Parse a file with ranges separated by commas, possibly over multiple lines.

        Example format:
        11-22,95-115,998-1012,1188511880-1188511890,...

        The file may include newlines and trailing commas; those are ignored.
        """
        text = f.read().replace("\n", "").strip()
        ranges = [r.strip() for r in text.split(',') if r.strip()]
        total_symetrique = 0
        for r in ranges:
            start, end = map(int, r.split('-'))
            for number in range(start, end + 1):
                str_num = str(number)
                length = len(str_num)
                if length % 2 == 0:
                    mid = length // 2
                    if str_num[:mid] == str_num[mid:]:
                        total_symetrique += number
                
                
    return total_symetrique


#main
if __name__ == '__main__':
    filepath = "./input.txt"
    testfilepath = "./test.txt"
    print(day2(testfilepath))
    print(day2(filepath))