import time


class Elevator:
    def __init__(self, num_floors):
        self.going_up = False
        self.going_down = False
        self.docked = True
        self.curr_floor = 0
        self.num_floors = num_floors
        self.floors_to_visit = []
        print('elevator created')

    def print_curr_status(self):
        for i in range(self.num_floors):
            if i == self.curr_floor:
                print('.  []')
            else:
                print('.')

    def handle_request(self, floor_num):
        if not self.going_up and not self.going_down:
            self.floors_to_visit = floor_num + self.floors_to_visit
            self.going_up = True
            self.traverse_to(floor_num)

    def traverse_to(self, floor_num):
        diff = abs(self.curr_floor - floor_num)
        time.sleep(diff * .5)



