import geometry_utils
from text_utils import reverse_string, count_words

print("Периметр квадрата:", geometry_utils.perimeter_square(5))
print("Площадь треугольника:", geometry_utils.area_triangle(10, 6))
print("Объем куба:", geometry_utils.volume_cube(3))

print("Реверс строки:", reverse_string("hello world"))
print("Количество слов:", count_words("Python is awesome"))