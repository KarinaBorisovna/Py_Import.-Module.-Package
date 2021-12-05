import package_application.salary as salary
import package_application.package_db.people as people


if __name__ == '__main__':
    # name = input('Введите имя сотрудника: ')
    name = 'Peter'
    my_post = people.get_employees(name)
    print(f'Должность сотрудника {name} - {my_post}')

    my_salary = salary.calculate_salary()
    print(f'Зарплата сотрудника {name}: {my_salary} руб.')
