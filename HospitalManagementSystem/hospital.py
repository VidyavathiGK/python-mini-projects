import uuid

class Patient:
    def __init__(self, name, age, gender, disease):
        self.id = str(uuid.uuid4())
        self.name = name
        self.age = age
        self.gender = gender
        self.disease = disease

    def __str__(self):
        return f"Patient ID: {self.id}, Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Disease: {self.disease}"

class Doctor:
    def __init__(self, name, specialization):
        self.id = str(uuid.uuid4())
        self.name = name
        self.specialization = specialization

    def __str__(self):
        return f"Doctor ID: {self.id}, Name: {self.name}, Specialization: {self.specialization}"

class Hospital:
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.doctors = []

    def add_patient(self, patient):
        self.patients.append(patient)
        print(f"Patient {patient.name} added with ID: {patient.id}")

    def add_doctor(self, doctor):
        self.doctors.append(doctor)
        print(f"Doctor {doctor.name} added with ID: {doctor.id}")

    def get_patients(self):
        return self.patients

    def get_doctors(self):
        return self.doctors

    def find_patient_by_id(self, patient_id):
        for patient in self.patients:
            if patient.id == patient_id:
                return patient
        return None

    def find_doctor_by_id(self, doctor_id):
        for doctor in self.doctors:
            if doctor.id == doctor_id:
                return doctor
        return None

    def discharge_patient(self, patient_id):
        patient_to_discharge = self.find_patient_by_id(patient_id)
        if patient_to_discharge:
            self.patients.remove(patient_to_discharge)
            print(f"Patient {patient_to_discharge.name} with ID {patient_id} has been discharged.")
            return True
        else:
            print(f"Patient with ID {patient_id} not found.")
            return False
