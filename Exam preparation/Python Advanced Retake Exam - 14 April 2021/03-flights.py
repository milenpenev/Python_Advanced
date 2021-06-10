def flights(*kwargs):
    for key in range(0, len(kwargs), 2):
        if kwargs[key] == "Finish":
            break
        else:
            destination = kwargs[key]
            passengers = kwargs[key + 1]
            if destination not in completed_flights:
                completed_flights[destination] = passengers
                continue
            completed_flights[destination] += passengers
    return completed_flights
completed_flights = {}
print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))