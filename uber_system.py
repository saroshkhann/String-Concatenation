class System:
    def __init__(self):
        self.online = True
        self.offline = False
        self.current1 = False
        self.cuurent2 = True
        self.riders = []
        self.drivers = []
        self.history = []

    def menu(self):
        print("1. Register Rider")
        print("2. Register Driver")
        print("3. Go Online (Driver)")
        print("4. Request Ride")
        print("5. Complete Ride")
        print("6. View History")
        print("7. Exit")

    def register_rider(self):
        rider_name = input("Enter rider name: ").lower()

        if rider_name in self.riders:
            print("❌ Rider already exists")
            return

        self.riders.append(rider_name)
        print(f"✅Rider '{rider_name}' registered successfully")

    def register_driver(self):
        driver_name = input("Enter driver name: ")

        for item in self.drivers:
            if item["driver_name"] == driver_name:
                print("❌ Driver already exists")
                return

        self.drivers.append({"driver_name": driver_name, "status": self.offline, "current": self.current1})
        print(f"✅Driver '{driver_name}' registered successfully")
        print(self.drivers)

    def driver_online(self):
        driver_name = input("Enter driver name: ")

        found = False

        for item in self.drivers:
            if item["driver_name"] == driver_name:
                found = True
                if item["status"] == self.online:
                    print("❌ Driver already online")
                    return
                else:
                    item["status"] = self.online
                    print(f"✅ Driver '{driver_name}' is now ONLINE")
                    print(self.drivers)

        if not found:
            print("❌ Driver not found")
            return

    def request_ride(self):
        rider_name = input("Enter rider name: ")
        pickup_location  = input("Enter pickup location: ")
        drop_location = input("Enter drop location: ")

        for item in self.drivers:
            if item["status"] == self.online:
                item["current"] = self.cuurent2
                print("🚗 Ride booked successfully")
                print(f"Driver: {item['driver_name']}")
                print(f"From: {pickup_location} -> To: {drop_location}")
                print(f"Status: ONGOING")
                self.history.append({"rider": rider_name, "driver": item["driver_name"], "pos1": pickup_location, "pos2": drop_location})
                return

            elif item["status"] == self.offline:
                print("❌ No drivers available at the moment")

    def complete_rider(self):
        driver_name = input("Enter driver name: ")
        found = False

        for item in self.drivers:
            if item["driver_name"] == driver_name:
                found=True
                if item["current"] == self.current1:
                    print("❌ No active ride for this driver")
                elif item["current"]  == self.cuurent2:
                    print("✅ Ride completed successfully")
                    item["current"] = self.current1
                    print(self.drivers)

        if not found:
            print("❌ Driver not found")

    def view_history(self):
        username = input("Enter username: ")
        print("🛕 Ride History: ")

        for item in self.history:
            if item["rider"] == username:
                print(f"Rider: {item['rider']} | Driver: {item['driver']} | {item['pos1']} -> {item['pos2']}")

user = System()

is_on = True

while is_on:
    user.menu()
    choice = int(input("Enter the number you want to perform "))

    if choice == 1:
        user.register_rider()
    elif choice == 2:
        user.register_driver()
    elif choice == 3:
        user.driver_online()
    elif choice == 4:
        user.request_ride()
    elif choice== 5:
        user.complete_rider()
    elif choice == 6:
        user.view_history()
    elif choice == 7:
        is_on = False
        print("Exiting Program... Goodbye!")
    else:
        print("Invalid input")
