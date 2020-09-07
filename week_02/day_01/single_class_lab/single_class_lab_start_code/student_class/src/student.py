class Student:

# Attributes
    def __init__(self, input_name, input_cohort):
        self.name = input_name
        self.cohort = input_cohort
    
# Methods
    def talk(self):
        return "I can talk!"

    def say_favourite_language(self, language):
        return f"I love {language}"
