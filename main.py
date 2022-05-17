class trip:
    def __init__(self, destination, starting_date, end_date, amount_of_trouser, underwear, socks, pants,shampoo,
                 soap, toothpaste, toothbrush):
        self.destination = destination
        self.starting_date = starting_date
        self.end_date = end_date
        self.amount_of_trouser = amount_of_trouser
        self.underwear = underwear
        self.socks = socks
        self.pants = pants
        self.shampoo = shampoo
        self.soap = soap
        self.toothpaste = toothpaste
        self.toothbrush = toothbrush

def add_trip():
    destination = input("Please enter the destination of your trip: ")
    starting_date = input("Please enter the starting date of your trip: ")
    end_date = input("Please enter the end date of your trip: ")
    underwear = input("Please enter number of underwear(s):")
    socks = input("Please enter number of socks(s):")
    pants = input("Please enter number of pant(s):")
    shampoo = input("Please enter number of shampoo:")
    soap = input("Please enter number of soap:")
    toothpaste = input("Please enter number of toothpaste(s):")
    toothbrush = input("Please enter number of toothbrush(s):")
    amount_of_trouser = input("Please enter the amount of trousers of your trip: ")
    add_new_trip = trip(destination, starting_date, end_date, underwear, socks, pants, shampoo,
                        soap, toothpaste, toothbrush, amount_of_trouser)
    trip_list.append(add_new_trip)


def list_trip():
    print("\n"*100)
    for trip in trip_list:
        print("Destination: " + trip.destination)
        print(f"Starting date: {trip.starting_date}")
        print(f"Ending date: {trip.end_date}")
        print(f"Number of underwear(s): {trip.underwear}")
        print(f"Number of sock(s):  {trip.socks} ")
        print(f"Number of pant(s): {trip.pants}")
        print(f"Number of shampoo(s): {trip.shampoo}")
        print(f"Number of soap(s): {trip.soap}")
        print(f"Number of toothpaste(s): {trip.toothpaste}")
        print(f"Number of toothbrush(es): {trip.toothbrush} ")
        print(f"Amount of trousers of your trip: {trip.amount_of_trouser}\n")




def store_trips():
    with open("trips.txt", 'w', encoding='utf-8') as f:
        for trip in trip_list:
            f.write(f"{trip.destination};")
            f.write(f"{trip.starting_date};")
            f.write(f"{trip.end_date};")
            f.write(f"{trip.underwear};")
            f.write(f"{trip.socks};")
            f.write(f"{trip.pants};")
            f.write(f"{trip.shampoo};")
            f.write(f"{trip.soap};")
            f.write(f"{trip.toothpaste};")
            f.write(f"{trip.toothbrush};")
            f.write(f"{trip.amount_of_trouser};\n")


def restore_trips():
    with open("trips.txt", 'r', encoding='utf-8') as f:
        for line in f.readlines():
            fields = line.split(";")
            trip_list.append(trip(fields[0], fields[1], fields[2], fields[3],
                                  fields[4], fields[5], fields[6], fields[7], fields[8],
                                  fields[9], fields[10]))


def full_text_search(user_search):
    print("\n"*100)
    for trip in trip_list:
        if user_search.lower() in trip.to_string().lower():
            print(f"Destination: {trip.destination}")
            print(f"Starting date: {trip.starting_date}")
            print(f"Ending date: {trip.end_date}")
            print(f"Number of underwear(s): {trip.underwear}")
            print(f"Number of sock(s):  {trip.socks} ")
            print(f"Number of pant(s): {trip.pants}")
            print(f"Number of shampoo(s): {trip.shampoo}")
            print(f"Number of soap(s): {trip.soap}")
            print(f"Number of toothpaste(s): {trip.toothpaste}")
            print(f"Number of toothbrush(es): {trip.toothbrush} ")
            print(f"Amount of trousers of your trip: {trip.amount_of_trouser}\n")

def delete_trip(delete):
    print("\n" * 100)
    for index, trip in enumerate(trip_list):
        if delete.lower() in trip.to_string().lower():
            print(index)
            print(f"Destination: {trip.destination}")
            print(f"Starting date: {trip.starting_date}")
            print(f"Ending date: {trip.end_date}")
            print(f"Number of underwear(s): {trip.underwear}")
            print(f"Number of sock(s):  {trip.socks} ")
            print(f"Number of pant(s): {trip.pants}")
            print(f"Number of shampoo(s): {trip.shampoo}")
            print(f"Number of soap(s): {trip.soap}")
            print(f"Number of toothpaste(s): {trip.toothpaste}")
            print(f"Number of toothbrush(es): {trip.toothbrush} ")
            print(f"Amount of trousers of your trip: {trip.amount_of_trouser}\n")
    delete_option = input("which one you want to delete: ")
    try:
        deleted_item = trip_list.pop(int(delete_option))
        print(f"deleted {deleted_item.destination} trip")
    except IndexError:
        print("Wrong input")

def export_trip():
    with open("exp.txt", 'w', encoding='utf-8') as f:
        for trip in trip_list:
            f.write(f"Destination: {trip.destination}\n")
            f.write(f"Starting date: {trip.starting_date}\n")
            f.write(f"End date: {trip.end_date}\n")
            f.write(f"{trip.underwear}\n")
            f.write(f"{trip.socks}\n")
            f.write(f"{trip.pants}\n")
            f.write(f"{trip.shampoo}\n")
            f.write(f"{trip.soap}\n")
            f.write(f"{trip.toothpaste}\n")
            f.write(f"{trip.toothbrush}\n")
            f.write(f"Amount of trousers: {trip.amount_of_trouser}\n\n")

trip_list = []


try:
    restore_trips()
except:
    print("Cant open the file")
while True:
    print("Main Menu")
    print("What do you want to do next?")
    print("1. Add a new trip")
    print("2. List all trips")
    print("3. Read all trips from file")
    print("4. Save the data")
    print("5. Find the data")
    print("6. Delete trip")
    print("7. Export trips")
    print("x. Exit the program")
    option = input("Your selection: ")
    if (option == "1"):
        add_trip()
    elif (option == "2"):
        list_trip()
    elif (option == "3"):
        restore_trips()
    elif (option == "4"):
        store_trips()
    elif (option == "5"):
        full_text_search(input("Please provide the search string: "))
    elif (option == "6"):
        delete_trip(input("Please provide the search string: "))
    elif (option == "7"):
        export_trip()
    elif (option.lower() == "x"):
        store_trips()
        quit()
    else:
        print("Wrong input, Try again !")