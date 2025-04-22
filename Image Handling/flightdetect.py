# flight_search.py

# Sample flight data
flights = [
    {
        "flight_no": "AI202",
        "source": "Delhi",
        "destination": "Varanasi",
        "departure": "08:00 AM",
        "arrival": "09:30 AM",
        "duration": "1h 30m",
        "price": 3200
    },
    {
        "flight_no": "SG404",
        "source": "Delhi",
        "destination": "Varanasi",
        "departure": "02:00 PM",
        "arrival": "03:25 PM",
        "duration": "1h 25m",
        "price": 2800
    },
    {
        "flight_no": "6E101",
        "source": "Delhi",
        "destination": "Mumbai",
        "departure": "09:00 AM",
        "arrival": "11:30 AM",
        "duration": "2h 30m",
        "price": 4500
    },
    {
        "flight_no": "AI301",
        "source": "Varanasi",
        "destination": "Delhi",
        "departure": "07:00 PM",
        "arrival": "08:30 PM",
        "duration": "1h 30m",
        "price": 3100
    },
]


def find_flights(source, destination):
    result = []
    for flight in flights:
        if flight['source'].lower() == source.lower() and flight['destination'].lower() == destination.lower():
            result.append(flight)
    return result


# Main program
if __name__ == "__main__":
    print("🔍 Searching for flights from Delhi to Varanasi...\n")
    source = input("Enter source ").lower().strip()
    destination = input("Enter destination ").lower().strip()
    results = find_flights(source, destination)

    if not results:
        print("No flights found.")
    else:
        for idx, flight in enumerate(results, 1):
            print(f"✈️ Flight {idx}:")
            print(f"  Flight No   : {flight['flight_no']}")
            print(f"  Departure   : {flight['departure']}")
            print(f"  Arrival     : {flight['arrival']}")
            print(f"  Duration    : {flight['duration']}")
            print(f"  Price       : ₹{flight['price']}")
            print("-" * 30)
