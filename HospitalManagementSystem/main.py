class Patient:
    def __init__(self, patient_id, name, age, illness):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.illness = illness

    def __str__(self):
        return f"Patient ID: {self.patient_id}\nName: {self.name}\nAge: {self.age}\nIllness: {self.illness}"

class Doctor:
    def __init__(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization

    def __str__(self):
        return f"Doctor ID: {self.doctor_id}\nName: {self.name}\nSpecialization: {self.specialization}"

class Appointment:
    def __init__(self, patient, doctor, date):
        self.patient = patient
        self.doctor = doctor
        self.date = date

    def __str__(self):
        return f"Appointment Details:\nDate: {self.date}\n{self.patient}\n{self.doctor}"

class Hospital:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []
        self.patient_id_counter = 1
        self.doctor_id_counter = 1

    def add_patient(self):
        name = input("Enter patient's name: ")
        age = int(input("Enter patient's age: "))
        illness = input("Enter patient's illness: ")
        patient = Patient(self.patient_id_counter, name, age, illness)
        self.patients.append(patient)
        self.patient_id_counter += 1
        print("Patient added successfully!")

    def add_doctor(self):
        name = input("Enter doctor's name: ")
        specialization = input("Enter doctor's specialization: ")
        doctor = Doctor(self.doctor_id_counter, name, specialization)
        self.doctors.append(doctor)
        self.doctor_id_counter += 1
        print("Doctor added successfully!")

    def schedule_appointment(self):
        self.view_patients()
        patient_id = int(input("Enter patient ID: "))
        patient = self.find_patient(patient_id)
        if not patient:
            print("Patient not found.")
            return

        self.view_doctors()
        doctor_id = int(input("Enter doctor ID: "))
        doctor = self.find_doctor(doctor_id)
        if not doctor:
            print("Doctor not found.")
            return

        date = input("Enter appointment date (YYYY-MM-DD): ")
        appointment = Appointment(patient, doctor, date)
        self.appointments.append(appointment)
        print("Appointment scheduled successfully!")

    def view_appointments(self):
        if not self.appointments:
            print("No appointments scheduled.")
        else:
            for appointment in self.appointments:
                print(appointment)
                print("-" * 20)

    def view_patients(self):
        if not self.patients:
            print("No patients found.")
        else:
            for patient in self.patients:
                print(patient)
                print("-" * 20)

    def view_doctors(self):
        if not self.doctors:
            print("No doctors found.")
        else:
            for doctor in self.doctors:
                print(doctor)
                print("-" * 20)

    def find_patient(self, patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                return patient
        return None

    def find_doctor(self, doctor_id):
        for doctor in self.doctors:
            if doctor.doctor_id == doctor_id:
                return doctor
        return None

def main():
    hospital = Hospital()
    while True:
        print("\nHospital Management System")
        print("1. Add Patient")
        print("2. Add Doctor")
        print("3. Schedule Appointment")
        print("4. View Patients")
        print("5. View Doctors")
        print("6. View Appointments")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            hospital.add_patient()
        elif choice == '2':
            hospital.add_doctor()
        elif choice == '3':
            hospital.schedule_appointment()
        elif choice == '4':
            hospital.view_patients()
        elif choice == '5':
            hospital.view_doctors()
        elif choice == '6':
            hospital.view_appointments()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
