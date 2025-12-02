def day2(filepath):
    with open(filepath, 'r') as f:
        """Parse a file with ranges separated by commas, possibly over multiple lines.

        Example format:
        11-22,95-115,998-1012,1188511880-1188511890,...

        The file may include newlines and trailing commas; those are ignored.

        you need to find out if a motif is repeted all along the number.
        for exemple 11 is 1 and 1 185185 is 185 and 185 but 1221222 is not 122 and 122 so it doesn't count for the total
        the new numbers to find out is like 123123123 who is 123 repeated 3 times or 12121212121212 who is 12 repeated 6 times but nor 1231231234 because the patern is broken by the 4 at the end
        
        """
        text = f.read().replace("\n", "").strip()
        ranges = [r.strip() for r in text.split(',') if r.strip()]
        def is_repeated_motif(s: str) -> bool:
            """Return True if `s` is exactly composed of a smaller motif repeated >= 2 times.

            Examples:
            - '11' -> True (1 repeated twice)
            - '185185' -> True (185 repeated twice)
            - '1221222' -> False (not an integer number of motif repeats)
            - '123123123' -> True (123 repeated 3 times)
            """
            n = len(s)
            # motif must be at most half length, to have at least two repetitions
            for k in range(1, n // 2 + 1):
                if n % k != 0:
                    continue
                motif = s[:k]
                if motif * (n // k) == s:
                    return True
            return False

        total_symetrique = 0
        for r in ranges:
            start, end = map(int, r.split('-'))
            for number in range(start, end + 1):
                s = str(number)
                if is_repeated_motif(s):
                    total_symetrique += number
    return total_symetrique


#main
if __name__ == '__main__':
    filepath = "./input.txt"
    testfilepath = "./test.txt"
    print(day2(testfilepath))
    print(day2(filepath))