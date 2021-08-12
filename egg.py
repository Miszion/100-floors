import random

class Egg:

    def __init__(self, criticalFloor):
        self.criticalFloor = criticalFloor

    def drop(self, floor):
        if (floor >= self.criticalFloor):
            return True
        else:
            return False



class FloorAlgorithm:

    def __init__(self, floors, criticalFloor):
        self.egg = Egg(criticalFloor)
        self.floors = floors
        self.rec_comparisons = 0
        self.iter_comparisons = 0

    def runIterative(self):

        for i in range(0, self.floors):
            self.iter_comparisons = self.iter_comparisons + 1
            if (self.egg.drop(i)):
                return i
    

    def runRec(self):
        return self.runRecursive(self.egg, self.floors / 2, self.floors)


    def runRecursive(self, egg, currentFloor, totalFloors):
        self.rec_comparisons = self.rec_comparisons + 1
        if (currentFloor == 0 or (egg.drop(currentFloor) and not egg.drop(currentFloor-1))):
            return int(currentFloor) # assuming at least one floor will break the egg
        elif (egg.drop(currentFloor)):
            return self.runRecursive(egg, currentFloor - int(currentFloor / 2), currentFloor)
        else:
            return self.runRecursive(egg, currentFloor + int((totalFloors - currentFloor) / 2), totalFloors)

    def printHistory(self):

        actual_critical_floor = self.egg.criticalFloor
        rec_critical_floor = self.runRec()
        iter_critical_floor = self.runIterative()

        print("Results of Egg Comparison:\n")
        print(f"Actual Critical Floor: {actual_critical_floor}")
        print("---\nIterative Egg:")
        print(f"Critical Floor Returned: {iter_critical_floor}")
        print(f"Number of Comparisons: {self.iter_comparisons}")
        print("---\nRecursive Egg:")
        print(f"Critical Floor Returned: {rec_critical_floor}")
        print(f"Number of Comparisons: {self.rec_comparisons}")
        
    


floor_algo = FloorAlgorithm(100, random.randrange(100))

floor_algo.printHistory()
