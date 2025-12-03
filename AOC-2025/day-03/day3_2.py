def day3_2(filepath):
    """For each line in `filepath`, choose 12 digits (preserving order)
    that form the largest possible 12-digit number when concatenated,
    convert that 12-digit string to int and sum those ints over all lines.

    Lines that contain fewer than 12 digits are skipped.
    """
    def max_k_digits(sequence, k):
        """Return maximal string of length k by selecting k chars from sequence
        while preserving order (greedy monotone stack algorithm).
        """
        seq = [str(x) for x in sequence]
        n = len(seq)
        if k <= 0 or k > n:
            raise ValueError("k must satisfy 1 <= k <= len(sequence)")
        to_remove = n - k
        stack = []
        for d in seq:
            while stack and to_remove > 0 and stack[-1] < d:
                stack.pop()
                to_remove -= 1
            stack.append(d)
        return ''.join(stack[:k])

    result = 0
    with open(filepath, 'r') as file:
        for raw in file:
            line = raw.strip()
            if not line:
                continue
            # extract digits only (in case of spaces or punctuation)
            digits = [c for c in line if c.isdigit()]
            if len(digits) < 12:
                # skip lines that don't have enough digits
                continue
            best12 = max_k_digits(digits, 12)
            result += int(best12)

    return result

                



if __name__ == "__main__":
    filepath = 'input.txt'
    fileTest = 'test.txt'
    print(day3_2(fileTest))  # Expected output for test file
    print(day3_2(filepath))
