class FitnessTracker:
    def __init__(self):
        self.workouts = []

    def add_workout(self, workout):
        self.workouts.append(workout)

    def show_workouts(self):
        for workout in self.workouts:
            print(workout)

# Example usage:
fitness_tracker = FitnessTracker()
fitness_tracker.add_workout("Ran 5 miles")
fitness_tracker.add_workout("Cycled 10 miles")
fitness_tracker.show_workouts()
