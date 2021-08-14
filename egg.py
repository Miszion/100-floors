import random

class Egg:

    def __init__(self, critical_floor):
        self.critical_floor = critical_floor

    def drop(self, floor):
        if (floor >= self.critical_floor):
            return True
        else:
            return False



class FloorAlgorithm:

    def __init__(self, floors, critical_floor):
        self.egg = Egg(critical_floor)
        self.floors = floors
        self.rec_comparisons = 0
        self.iter_comparisons = 0

    def run_iterative(self):

        for i in range(0, self.floors):
            self.iter_comparisons = self.iter_comparisons + 1
            if (self.egg.drop(i)):
                return i
    

    def run_rec(self):
        return self.run_recursive(self.egg, self.floors / 2, self.floors)


    def run_recursive(self, egg, current_floor, total_floors):
        self.rec_comparisons = self.rec_comparisons + 1
        if (current_floor == 0 or (egg.drop(current_floor) and not egg.drop(current_floor-1))):
            return int(current_floor) # assuming at least one floor will break the egg
        elif (egg.drop(current_floor)):
            return self.run_recursive(egg, current_floor - int(current_floor / 2), current_floor)
        else:
            return self.run_recursive(egg, current_floor + int((total_floors - current_floor) / 2), total_floors)

    def print_history(self):

        actual_critical_floor = self.egg.critical_floor
        rec_critical_floor = self.run_rec()
        iter_critical_floor = self.run_iterative()

        print("Results of Egg Comparison:\n")
        print(f"Actual Critical Floor: {actual_critical_floor}")
        print("---\nIterative Egg:")
        print(f"Critical Floor Returned: {iter_critical_floor}")
        print(f"Number of Comparisons: {self.iter_comparisons}")
        print("---\nRecursive Egg:")
        print(f"Critical Floor Returned: {rec_critical_floor}")
        print(f"Number of Comparisons: {self.rec_comparisons}")
        
    


floor_algo = FloorAlgorithm(100, random.randrange(100))

floor_algo.print_history()
