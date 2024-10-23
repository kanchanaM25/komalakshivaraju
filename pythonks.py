class Patient:
    def __init__(self, name, age, health_issue):
        self.name = name
        self.age = age
        self.health_issue = health_issue

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Health Issue: {self.health_issue}")

class HealthAdministration:
    def __init__(self):
        self.patients = []

    def add_patient(self, name, age, health_issue):
        patient = Patient(name, age, health_issue)
        self.patients.append(patient)
        print(f"Patient {name} added successfully.")

    def view_patients(self):
        if not self.patients:
            print("No patients found.")
        else:
            print("\nPatient Records:")
            for patient in self.patients:
                patient.display_info()

    def search_patient(self, name):
        for patient in self.patients:
            if patient.name.lower() == name.lower():
                patient.display_info()
                return
        print(f"Patient {name} not found.")

if __name__ == "__main__":
    health_admin = HealthAdministration()

    while True:
        print("\nHealth Administration Menu:")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Search Patient")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            name = input("Enter patient name: ")
            age = input("Enter patient age: ")
            health_issue = input("Enter health issue: ")
            health_admin.add_patient(name, age, health_issue)
        elif choice == '2':
            health_admin.view_patients()
        elif choice == '3':
            name = input("Enter patient name to search: ")
            health_admin.search_patient(name)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
