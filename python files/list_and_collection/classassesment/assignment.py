students = [
     ("Alice", 78),
     ("Bob", 45),
     ("Charlie", 90),
     ("Diana", 62)
]

def unpacking(students_list):
    for name, score in students_list:
        print(f"Name: {name}, Score: {score}")

def student_above_60(students_list):
    print([name for name, score in students_list if score >= 60])

def numbers_of_student_with_pass_mark(students_list):
    return len([name for name, score in students_list if score >= 50])


products = [
    ("Laptop", 1200),
    ("Mouse", 6200),
    ("Keyboard", 900),
    ("USB Cable", 100)
]

def product_above_100(products_list):
    return list(filter(lambda product: product[1] > 100, products_list))

def sum_of_all_product_price(products_list):
    return sum([price for name, price in products_list])

def unpacking_products(products_list):
        name, price = products_list[0]
        print(f"Product: {name} -Price: {price}")

print(unpacking_products(products))

points = [
    (2,3),
    (-1,4),
    (0,7),
    (-3,-2)
]

def positive_points(points_list):
    return list(filter(lambda point: point[1] >=0 and point[0] >= 0, points_list))

def positive_unpacking(points_list):
    for point in points_list:
        first_coordinate, second_coordinate = point
        if first_coordinate >= 0 and  second_coordinate >= 0:
            print(point)


employees = [
    ("John", "IT", 50000),
    ("Jane", "HR", 45000),
    ("Mike", "IT", 90000),
    ("Sarah", "Finance", 110000)
]

def unpacking_employees(employees_list):
    for name, department, salary in employees_list:
        print(f"Name: {name}  -Department: {department}  -Salary: {salary}")

def filtering_by_IT(employees_list):
    return list(filter(lambda employee: employee[1] == "IT", employees_list))

def filtering_by_salary(employees_list):
    return list(filter(lambda employee: employee[2] > 55000, employees_list))



# print(filtering_by_sal?ary(employees))

school = [
    [
        ("samuel", 20, 400),
        ("ayobami", 10, 500),
        ("emmanuel", 50, 100)
    ],
    [("english"), ("math"),("yoruba")]

]

def add_10_scores_to_student(student):
    new_student = list(student)
    new_student[2] +=10
    return tuple(new_student)


print(list(map(add_10_scores_to_student, school[0])))
print("hello")

