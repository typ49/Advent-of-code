from functools import cache


def day11(filepath):
    graph = {}

    for line in open(filepath):
        src, dests = line.strip().split(": ")
        graph[src] = dests.split()

    @cache
    def count(src, dest):
        if src == dest : return 1
        return sum(count(x, dest) for x in graph.get(src, []))
    
    return (count("svr", "dac") * count("dac", "fft") * count("fft", "out") + count("svr", "fft") * count("fft", "dac") * count("dac", "out"))
        
    

if __name__ == "__main__":
    print(day11("test_p2.txt"))
    print(day11("input.txt"))