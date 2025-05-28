class Person:
    APPROVED_JOBS = ["Sales", "Engineer", "Artist", "Teacher", "Doctor", "ITC"]

    def __init__(self, name="Unknown", job="Unemployed"):
        self.name = name
        self.job = job

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0 or len(value) > 25:
            print("Name must be string between 1 and 25 characters.")
            self._name = "Unknown"
        else:
            self._name = value.title()

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value not in Person.APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
            self._job = "Unemployed"
        else:
            self._job = value
