class BusStop:
    def __init__(self, input_name):
        self.name = input_name
        self.queue = []

    def add_to_queue(self, person):
        self.queue.append(person)

    def queue_length(self):
        return len(self.queue)
    
    def clear_queue(self):
        for person in self.queue:
            self.queue.remove(person)