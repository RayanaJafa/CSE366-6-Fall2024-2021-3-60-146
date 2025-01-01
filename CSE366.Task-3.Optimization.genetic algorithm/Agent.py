class Student:
    def __init__(self, id, availability, preferences):
        self.id = id
        self.availability = availability  # List of available time slots
        self.preferences = preferences  # Dictionary of time slot preferences
        self.schedule = []  # Assigned schedule

    def assign_class(self,class_assignments):
        self.schedule = []  # Reset schedule before assigning
        for class_id, (student, slot) in enumerate(class_assignments):
            if student == self.id and self.availability[slot] == 1:
                # Assign the class to the student if the student is available
                self.schedule.append((class_id, slot))

    def clear_schedule(self):
        self.schedule = []
