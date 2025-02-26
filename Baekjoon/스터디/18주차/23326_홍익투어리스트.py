from sortedcontainers import SortedSet

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    idx = 0
    n = int(data[idx])
    q = int(data[idx + 1])
    idx += 2

    m = SortedSet()
    for i in range(n):
        b = int(data[idx])
        idx += 1
        if b == 1:
            m.add(i)

    cur = 0

    results = []
    for i in range(q):
        query = int(data[idx])
        idx += 1

        if query == 1:
            x = int(data[idx]) - 1
            idx += 1
            if x in m:
                m.remove(x)
            else:
                m.add(x)

        elif query == 2:
            x = int(data[idx])
            idx += 1
            cur = (cur + x) % n

        elif query == 3:
            if len(m) == 0:
                results.append(-1)
            else:
                pos = m.bisect_left(cur)
                if pos == len(m):
                    step = (n - cur) + m[0]
                else:
                    step = m[pos] - cur
                results.append(step)

    sys.stdout.write("\n".join(map(str, results)) + "\n")

if __name__ == "__main__":
    main()
