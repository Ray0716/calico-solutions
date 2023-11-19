def solve(N: int, M: int, K: int, S: list[int], E: list[int]) -> int:
    """
    Find the total distance the subway must travel until all passengers have
    arrived at their ending station.

    N: the number of passengers
    M: the number of stations
    K: the maximum number of passengers the subway can carry
    S: list of starting stations for each passenger
    E: list of ending stations for each passenger
    """
    # YOUR CODE HERE
    #1 find the first and last passengers
    #2 

    distance = 0
    curr = 1
    onSubway = []

    while (len(onSubway) > 0) or (len(S) > 0):
        onSubway = [p for p in onSubway if E[p-1] != curr]
        while (len(S) > 0) and (S[0] == curr) and (len(onSubway) < K):
            w = S[0]
            S.pop(0)
            onSubway.append(w)

        if (len(S) > 0) or (len(onSubway) > 0):
            distance += 1
            curr = curr + 1 if curr < M else 1

    return distance



def main():
    T = int(input())
    for _ in range(T):
        N, M, K = [int(x) for x in input().split()]
        S = [int(x) for x in input().split()]
        E = [int(x) for x in input().split()]
        print(solve(N, M, K, S, E))


if __name__ == '__main__':
    main()
