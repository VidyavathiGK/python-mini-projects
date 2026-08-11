class Patient:
    def __init__(self, name, age, gender, disease):
        self.name = name
        self.age = age
        self.gender = gender
        self.disease = disease

    def __str__(self):
        return f"Patient: {self.name}, Age: {self.age}, Gender: {self.gender}, Disease: {self.disease}"

class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization

    def __str__(self):
        return f"Doctor: {self.name}, Specialization: {self.specialization}"

class Hospital:
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.doctors = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def get_patients(self):
        return self.patients

    def get_doctors(self):
        return self.doctors
