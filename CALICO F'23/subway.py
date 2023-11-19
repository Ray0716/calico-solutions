def subway_distance(N, M, K, start_stations, end_stations):
    distance = 0
    current_station = 1  # Initial station of the subway
    passengers_on_subway = []  # List to store passengers on the subway

    while passengers_on_subway or start_stations:
        # Remove passengers whose destination is the current station
        passengers_on_subway = [p for p in passengers_on_subway if end_stations[p - 1] != current_station]

        # Add new passengers to the subway until it's full or no more passengers at the current station
        while start_stations and start_stations[0] == current_station and len(passengers_on_subway) < K:
            passengers_on_subway.append(start_stations.pop(0))

        # Move the subway to the next station
        if start_stations or passengers_on_subway:
            distance += 1
            current_station = (current_station % M) + 1

    return distance

def main():
    T = int(input())
    
    for _ in range(T):
        N, M, K = map(int, input().split())
        start_stations = list(map(int, input().split()))
        end_stations = list(map(int, input().split()))

        result = subway_distance(N, M, K, start_stations, end_stations)
        print(result)

if __name__ == "__main__":
    main()
