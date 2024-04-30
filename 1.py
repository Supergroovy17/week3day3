#Task 1: Formatting Flight Itineraries
#Create a Python function that takes a list of tuples as an argument.
#Each tuple contains information about a flight itinerary:
#(traveler_name, origin, destination). 

#The function should format and 
#return a string that lists each itinerary. For example, if the input is 
#[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")], 
#the output should be a string formatted as:
#"Itinerary 1: Alice - From New York to London


#Create a Python function that takes a list of tuples as an argument.

flight_itineraries = [
    ("Alice", "New York", "London"),
    ("Bob", "Tokyo", "San Francisco")
]

def format_itineraries(itineraries):
    output = ""
    index = 1  # Initialize index for numbering itineraries
    for itinerary in itineraries:
        traveler_name, origin, destination = itinerary
        output += f"Itinerary {index}: {traveler_name} - From {origin} to {destination}\n"
        index += 1  # Increment index for the next itinerary
    return output

formatted_itineraries = format_itineraries(flight_itineraries)
print(formatted_itineraries)


