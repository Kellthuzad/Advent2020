def main():
    filehandle = open("./Day10/input.txt")
    lines = []
    for line in filehandle:
        lines.append(int(line.rstrip()))

    #a sorted version of the input
    D = sorted(lines)

    δ = lowerCaseDelta(D)
    Δ = [1+p for p,d in enumerate(δ) if d==3]
    L = [hi-lo-1 for lo,hi in zip([0] + Δ[:-1], Δ)]

    T = [1, 1, 2]
    while len(T) <= max(L): T += [sum(T[-3:])]
    # Optional, hardcode first 6 (input chains are never longer):
    # T = [1, 1, 2, 4, 7, 13]

    import math
    print('Part 1:', (len(δ)-len(Δ))*len(Δ),
        '\nPart 2:', math.prod(T[l] for l in L))

def lowerCaseDelta(D):
    return [i-j for i,j in zip(D, [0]+D)] + [3]

    # for i,j in zip(D, [0]+D)
    

main()