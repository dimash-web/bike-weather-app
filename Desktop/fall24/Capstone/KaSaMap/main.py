import json
import folium

def collect_coordinates():
    locations = []
    
    while True:
        name = input("Enter the name of your business location (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        
        try:
            latitude = float(input(f"Enter the latitude for {name}: "))
            longitude = float(input(f"Enter the longitude for {name}: "))
        except ValueError:
            print("Invalid input. Please enter numeric values for latitude and longitude.")
            continue
        
        locations.append({
            "location": name,
            "latitude": latitude,
            "longitude": longitude
        })
    
    return locations

def save_to_json(locations, filename="locations.json"):
    with open(filename, "w") as f:
        json.dump(locations, f, indent=4)
    print(f"Locations saved to {filename}")

def load_from_json(filename="locations.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"No file named {filename} found.")
        return []

def display_map(locations):
    if locations:
        first_location = locations[0]
        map = folium.Map(location=[first_location["latitude"], first_location["longitude"]], zoom_start=6)

        for location in locations:
            folium.Marker(
                [location["latitude"], location["longitude"]],
                popup=location["location"]
            ).add_to(map)

        map.save("locations_map.html")
        print("Map generated successfully!")
    else:
        print("No locations to display on the map.")

def main():
    print("Welcome! Let's add your business location coordinates.")
    locations = collect_coordinates()
    save_to_json(locations)
    locations_from_file = load_from_json()
    display_map(locations_from_file)

if __name__ == "__main__":
    main()
