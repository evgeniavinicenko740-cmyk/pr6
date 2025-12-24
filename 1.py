
students = {
    "група": "КІ-23",
    "курс": 2,
    "студенти": [
        {
            "ПІБ": "Іваненко Іван Іванович",
            "предмети": {"Математика": 90, "Програмування": 85, "Фізика": 78}
        },
        {
            "ПІБ": "Петренко Олена Сергіївна",
            "предмети": {"Математика": 95, "Програмування": 88, "Фізика": 80}
        }
    ]
}

# Функція для додавання нового студента до словника
def add_student(students_dict):
    try:
        pib = input("Введіть ПІБ студента: ")
        subjects = {}
        n = int(input("Введіть кількість предметів: "))
        for i in range(n):
            subject = input(f"Назва предмета {i+1}: ")
            grade = int(input(f"Оцінка за предмет '{subject}': "))
            subjects[subject] = grade

        new_student = {"ПІБ": pib, "предмети": subjects}
        students_dict["студенти"].append(new_student)
        print("\n✅ Нового студента успішно додано!\n")

    except ValueError:
        print("❌ Помилка: оцінка повинна бути числом.")
    except Exception as e:
        print(f"❌ Сталася помилка: {e}")

# Функція для виведення всіх студентів і їхніх оцінок
def display_students(students_dict):
    print(f"\nГрупа: {students_dict['група']} | Курс: {students_dict['курс']}\n")
    for s in students_dict["студенти"]:
        print(f"ПІБ: {s['ПІБ']}")
        for subj, grade in s["предмети"].items():
            print(f"  {subj}: {grade}")
        print("-" * 25)

# Головна частина програми
if __name__ == "__main__":
    while True:
        print("\nМеню:")
        print("1 - Вивести всіх студентів")
        print("2 - Додати нового студента")
        print("3 - Вихід")
        choice = input("Оберіть дію: ")

        if choice == "1":
            display_students(students)
        elif choice == "2":
            add_student(students)
        elif choice == "3":
            print("Програма завершена.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

