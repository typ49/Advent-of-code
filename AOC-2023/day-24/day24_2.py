import sympy

# compilation : python3 day24_2.py < day24.in
def day24(filepath):
    f = open(filepath, 'r')
    hailstones = [tuple(map(int, line.replace("@", ",").split(","))) for line in f]

    xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr")

    equations = []

    for i, (sx, sy, sz, vx, vy, vz) in enumerate(hailstones):
        equations.append((xr - sx) * (vy - vyr) - (yr - sy) * (vx - vxr))
        equations.append((yr - sy) * (vz - vzr) - (zr - sz) * (vy - vyr))
        if i < 2:
            continue
        answers = [soln for soln in sympy.solve(equations) if all(x % 1 == 0 for x in soln.values())]
        if len(answers) == 1:
            break
        
    answer = answers[0]

    return answer[xr] + answer[yr] + answer[zr]

# main
filepath = "./input.txt"
if __name__ == '__main__':
    print(day24(filepath))