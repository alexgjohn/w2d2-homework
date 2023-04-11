class Bus:
    def __init__(self, input_route_number, input_destination):
        self.route_number = input_route_number
        self.destination = input_destination
        self.passengers = []

    def drive(self):
        return "Brum brum"
    
    def passenger_count(self):
        return len(self.passengers)
    
    def pick_up(self, passenger):
        self.passengers.append(passenger)

    def drop_off(self, passenger):
        self.passengers.remove(passenger)

    def empty_bus(self):
        for passenger in self.passengers:
            self.passengers.remove(passenger)

    def pick_up_from_stop(self, bus_stop):
        for passenger in bus_stop.queue:
            self.pick_up(passenger)
        bus_stop.clear_queue
        # for passenger in bus_stop.queue:
        #     bus_stop.queue.remove(passenger)


