
def unpacking(students_list):
    for student in students_list:
        name, score = student
        print(f"Name: {name}, Score: {score}")

def student_above_60(students_list):
    return [name for name, score in students_list if score == 60]

def numbers_of_student_with_pass_mark(students):
    return len([name for name, score in students if score >= 50])


products = [
    ("Laptop", 1200),
    ("Mouse", 6200),
    ("Keyboard", 900),
    ("USB Cable", 100)
]

def product_above_100(products):
    return list(filter(lambda product: product[1] > 100, products))

def sum_of_all_product_price(products):
    return sum([price for name, price in products])

def unpacking_products(products_list):
    for product in products_list:
        name, price = product
        print(f"Product: {name}-Price: {price}")

points = [
    (2,3),
    (-1,4),
    (0,7),
    (-3,-2)
]

def positive_points(points):
    return list(filter(lambda point: point[1] >=0 and point[0] >= 0, points))

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
    for employee in employees_list:
        name, department, salary = employee
        print(f"Name: {name}  -Department: {department}  -Salary: {salary}")

def filtering_by_IT(employees_list):
    return list(filter(lambda employee: employee[1] == "IT", employees_list))

def filtering_by_salary(employees_list):
    return list(filter(lambda employee: employee[2] > 55000, employees_list))



print(filtering_by_salary(employees))



