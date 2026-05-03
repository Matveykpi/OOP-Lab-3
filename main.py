class EducationalInstitution:

#конструктор для ініціалізації об'єкту
    def __init__(self, name, inst_type, student_count, foundation_year, rating):
        self.name = name
        self.inst_type = inst_type
        self.student_count = student_count
        self.foundation_year = foundation_year
        self.rating = rating

#Повертає рядкове представлення об'єкта
    def __repr__(self):
        return (f"Institution(Name: {self.name}, Type: {self.inst_type}, "
                f"Students: {self.student_count}, Year: {self.foundation_year}, "
                f"Rating: {self.rating})")

#порівнює об'єкт з іншими на індетичність полів
    def __eq__(self, other):
        if not isinstance(other, EducationalInstitution):
            return False
        return (self.name == other.name and
                self.inst_type == other.inst_type and
                self.student_count == other.student_count and
                self.foundation_year == other.foundation_year and
                self.rating == other.rating)


#виконавчий клас
class Main:
    @staticmethod
    def run():

#створюємо масив об'єктів
        institutions = [
            EducationalInstitution("KPI", "University", 30000, 1898, 95.5),
            EducationalInstitution("KNU", "University", 25000, 1834, 94.8),
            EducationalInstitution("Lyceum 208", "Lyceum", 400, 1990, 88.0),
            EducationalInstitution("KNEU", "University", 25000, 1906, 85.0),
            EducationalInstitution("Gymnasium 1", "Gymnasium", 1200, 1995, 85.5)
        ]

        print("Початковий список")
        for item in institutions:
            print(item)

#сортування
        institutions.sort(key=lambda x: (x.student_count, -x.foundation_year))

        print("\nВідсортований список")
        for item in institutions:
            print(item)

#пошук заданого об'єкта
        target = EducationalInstitution("KPI", "University", 30000, 1898, 95.5)

        found = next((x for x in institutions if x == target), None)

        print("\nПошук об'єкта")
        if found:
            print(f"Знайдено ідентичний об'єкт: {found}")
        else:
            print("Об'єкт не знайдено.")


if __name__ == "__main__":
    Main.run()
