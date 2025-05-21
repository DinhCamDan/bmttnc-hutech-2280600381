# Khai báo biến
x= 10 #Biến lưu trữ giá trị số ngyên là 10
name = "CamDan" #Biến name lưu trữ chuỗi "CamDan
is_valid = True #Biến is_valid lưu giữ giá trị boolean True
  #x, name, is_valid là tên biến
  #Tuy nhiên, chúng ta không thể sử dụng từ khoá(Keywords) làm tên biến
  if = 5 #Lỗi! " if" là từ khoá, không thể sử dụng làm tên biến

#Một số từ khoá trong Python
#False: Đại diện cho giá trị logic sai
is_active = False
if not is_active: 
    print("Tài khoản không hoạt động")

#None: đại diện cho giá trị không có hoặc thiếu
ten = None
if ten is None:
    print("Chưa có tên")

#and Thực hiện phép toán logic "và"
account = True
password = True
if account and password 
    print("Đăng nhập thành công")

#as: Được sử dụng để đặt bí danh cho các module hoặc các thành phần khác
import math as toan
    print(toan.sqrt(16))
    # đổi tên module math thành toan

#assert: Kiểm tra điều kiện và nếu điều kiện sai thì ném ra một lỗi
tuoi = 18
assert tuoi> = 18, "bạn chưa đủ tuổi"
print("Đã đủ tuổi")

#async: Khai báo hàm chạy song song đồng bộ
import asyncio
async def chao():
    print("Xin chao")

#await: Chờ kết quả trong hàm bất đồng bộ
import asyncio
async def doi_1_giay():
    print("Đang chờ...")
    await asyncio.sleep(1)
    print("Xong")
#break: Dừng vòng lặp ngay lập tức
for so in range(10):
    if so == 3:
        break
        print("So")

#class Được sử dụng để định nghĩa một lớp
class Person:
  name = "John"
  age = 36

#continue: Bỏ qua phần còn lại của vòng lặp hiện tại và tiếp tục với lần lặp tiếp theo
i = 0
while i < 9:
  i += 1
  if i == 3:
    continue
  print(i)

#del: Xoá một biến hoặc một phần tử ra khỏi danh sách
x = ["apple", "banana", "cherry"]

del x[0]

print(x)

#def: Định nghĩa một hàm
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#elif: else if, dùng trong câu lệnh rã nhánh
for i in range(-5, 5):
  if i > 0:
    print("YES")
  elif i == 0:
    print("WHATEVER")
  else:
    print("NO")

#else: Dùng trong câu rẻ nhánh
x = 2
if x > 3:
  print("YES")
else:
  print("NO")

#except; Xử lý các ngoại lệ
try:
  x > 3
except:
  print("Something went wrong")

#finally: xác định khối mã sẽ được thực thi sau khi thực thi các khôi try, except
try:
  x > 3
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
finally:
  print("The try...except block is finished")

#for: Được sử dụng để tạo vòng lặp
fruits = ["apple", "banana", "cherry"]

for x in fruits:
  print(x)

#from: Được dùng khi import một phần (module hay package) từ một module 
from datetime import time

x = time(hour=15)

print(x)

#global: được dùng để xác định rằng biến nằm trong phạm vi toàn cục
#create a function:
def myfunction():
  global x
  x = "hello"

#execute the function:
myfunction()

#x should now be global, and accessible in the global scope.
print(x)

#if: Sử dụng trong câu lệnh rẽ nhánh. Nếu A thì B, nếu C thì D
if 5 > 2:
 print("Five is greater than two!")
        print("Five is greater than two!")

#import: Dùng để import các module vào chương trình
import datetime

x = datetime.datetime.now()
print(x)

#in: Kiểm tra một giá trị có tồn tại trong một chuỗi,danh sách, tuple
fruits = ["apple", "banana", "cherry"]

for x in fruits:
  print(x)

#is: Dùng để so sánh hai đối tượng xem nó có tham chiếu hay không
x = ["apple", "banana", "cherry"]

y = x

print(x is y)

#lambda: tạo các hàm nặc danh
x = lambda a : a + 10

print(x(5))

#not thực hiện các phép toán logic "Không"
x = False

print(not x)

#nonlocal: Được dùng để xác định rằng biến nằm ở phạm vi không phải toàn cục cũng không phải cục bộ
def myfunc1():
  x = "John"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

#or: thực hiện phép toán logic "hoặc" 
x = (5 > 3 or 5 > 10)

print(x)

#pass: Đánh dấu để bỏ qua đoạn mã mà không làm gì cả
for x in [0, 1, 2]:
  pass

#return: Dùng để trả về kết quả từ một hàm
def myfunction():
  return 3+3

print(myfunction())

#while: Được sử dụng để tạo vòng lặp while
x = 0

while x < 9:
  print(x)
  x = x + 1

#yield: Dùng trong hàm để trả về giá trị, lưu trạng thái của hàm đó
def myFunc():
  yield "Hello"
  yield 51
  yield "Good Bye"

x = myFunc()

for z in x:
  print(z)

#raise: Sử dụng để ném một ngoại lệ
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")

#try Dùng để thực hiện các lệnh có khả năng gây ra những ngoại lệ khác nhau
try:
  x > 3
except:
  print("Something went wrong")

#with: Dùng khi làm việc với các nguồn tài nguyên được quản lý tự động
with open("dulieu.txt", "r", encoding=utf-8) as file:
    noi_dung = file.read()
    print(noi_dung)

#KIỂU DỮ LIỆU

# - Kiểu dữ liệu số
int ; Kiểu dữ liệu số nguyên
float ; kiểu dữ liệu số thực
complex ; Kiểu dữ liệu số phức

# - kiểu dữ liệu chuỗi
str : Lưu trữ chuỗi kí tự, được bao quanh bởi '' hoặc ""

# - Kiểu dữ liệu boolean
bool ; có hai giá trị True và False

# - Kiểu dữ liệu dạng danh sách
list ; lưu trữ tập hợp các phần tử có thứ tự và có thể thay đổi

# - kiểu dữ liệu tuple
tuple ; tương tự như danh sách nhưng không thể thay đổi

# - Kiểu dữ liệu từ điển 
dict ; lưu trữ các cặp key-value không có thứ tự, key không thay đổi, value có thể thay đổi

# - kiểu dữ liệu tập hợp
set ; dùng để lưu trữ một tập hợp các phần tử không trùng lặp và không có thứ tự

# - Kiểu dữ liệu bộ nhớ đóng
frozenset ; tương tự như kiểu dữ liệu set nhưng không thể thay đổi

# - Kiểu dữ liệu nhị phân
bytes ; Lưu trữ một chuỗi bytes
bytearray ; tương tự như bytes nhưng có thể thay đổi

# - Kiểu dữ liệu None
NoneType: Chỉ có một giá trị là none 

#  CÁC TOÁN TỬ SỐ HỌC
# CỘNG
a = 5
b = 3
result = a + b 

# TRỪ
a = 8
b = 4
result = a - b 

# Nhân
a = 5
b = 3
result = a * b 

# Chia
a = 5
b = 3
result = a / b 

# Chia lấy phần nguyên
a = 5
b = 3
result = a // b 

# Chia lấy dư
a = 5
b = 3
result = a % b 

# Luỹ thừa
a = 5
b = 3
result = a ** b 

# CÁC TOÁN TỬ LOGIC KẾT QUẢ TRUE HOẶC FALSE

# phép toán AND
x=5
y=3
result = (x>2) and (y<4)

# PHÉP TOÁN OR
x=5
y=3
result = (x>2) or (y>4)

# phép toán not
x = 5
result = not (x==5)

# Phép so sánh ==
x = 5
result = (x==5)

# Phép so sánh không bằng !=
X = 5
result = (X !=3)

# phép so sánh lớn hơn, nhỏ hơn
x = 5
result = (x>=3)
result = (x<=3)

# Nhập xuất dữ liệu
name = input ("Nhập tên của bạn: ")
    print("xin chào,"name)
# Hàm “print()” được sử dụng để hiển thị dữ liệu ra màn hình hoặc console. Ta có thể truyền biến, chuỗi, hoặc giá trị cần hiển thị vào hàm “print()”.

# Ngoài ra, “print()” cũng cho phép định dạng hiển thị qua việc sử dụng các đối số 
#khác như “sep” (ký tự phân cách), “end” (ký tự kết thúc), và các chuỗi định dạng f-string. Ví dụ:
print ("Python", "là", "ngôn", "ngữ", "lập","trình", sep="-")
# kết quả: Python - là - ngôn - ngữ - lập - trình
print ("Xin chào", end="")
print ("Các bạn!")
# kết quả: Xin chào các bạn

# Các cấu trúc điều kiện
# - Câu lệnh điều kiện if, elif, else
x = 10
if x > 5:
  print ("x lớn hơn 5")
elif x == 5:
  print ("x bằng 5")
else x < 5:
  print ("x nhỏ hơn 5")
# Kết quả: x lớn hơn 5

# - Vòng lặp: for và while
  # Vòng lặp “for” được dùng để duyệt qua một chuỗi hoặc một tập hợp các phần tử
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  print (fruit)
# kết quả: apple, banana, cherry
  # Vòng lặp “while” thực hiện việc lặp lại mã đến khi điều kiện không còn đúng nữa
count = 0
while count < 5:
  print (count)
  count +=1 
  #Câu lệnh nhảy (Jump Statements): Câu lệnh nhảy được dùng để thay đổi luồng điều khiển của chương trình. “break”, “continue” và “pass”.
Sử dụng câu lệnh “break” để kết thúc một vòng lặp:
# Tìm số chia hết cho 5 đầu tiên trong khoảng từ 1 đến 100
for i in range(1, 101):
    if i % 5 == 0:
        print("Số chia hết cho 5 đầu tiên là:", i)
        break
Sử dụng câu lệnh “break” để kết thúc một vòng lặp:
# In các số chẵn từ 1 đến 10 và bỏ qua các số lẻ
for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)
Câu lệnh “continue” được dùng để bỏ qua phần còn lại của vòng lặp hiện tại và 
chuyển sang vòng lặp kế tiếp:
x = 5 
if x > 20
  print (" x lớn hơn 20")
else:
  pass

# CHUỖI
# - khai báo chuỗi trong python
string_single_quotes = 'Đây là chuỗi sử dụng dấu ngoặc đơn'
string_double_quotes = " Đây là một chuỗi sử dụng dấu ngoặc kép"
string_triple_quotes = ''' Đây là một chuỗi
                          sử dụng dấu ngoặc ba
                          có thể trãi nhiều dòng'''

 # - Truy cập ký tự trong chuỗi
 my_string = "hello, word"
  print(my_string[0]) # Kết quả: 'H'
  print(my_string[7]) # Kết quả: 'W'

# - các phép sử lý chuỗi trong python
    cắt chuỗi
    my_string = "Hello, World!"
print(my_string[7:])  # Lấy từ ký tự thứ 7 đến hết: Kết quả: 'World!'
print(my_string[:5])  # Lấy từ đầu đến ký tự thứ 4: Kết quả: 'Hello'
print(my_string[3:8])  # Lấy từ ký tự thứ 3 đến ký tự thứ 7: Kết quả: 'lo, W'

    ghép chuỗi
 string1 = "Hello"
 string2 = "World"
 concatenated_string = string1 + " " + string2 # Kết quả: 'Hello World'

  Độ dài chuỗi
  my_string = "Hello, World!"
  length = len(my_string) # Kết quả: 13

  Một số hàm dùng để xử lý các chuỗi trong Python:
"upper()": Chuyển đổi chuỗi thành chữ hoa.
"lower()": Chuyển đổi chuỗi thành chữ thường.
"strip()": Loại bỏ khoảng trắng ở đầu và cuối chuỗi.
"split()": Phân tách chuỗi thành danh sách các từ hoặc phần tử.
"replace()": Thay thế một phần của chuỗi bằng một chuỗi khác

 my_string = "  Hello, World!  "
 print(my_string.strip()) # Loại bỏ khoảng trắng: Kết quả: 'Hello, World!'
 my_string = "Hello, World!"
 print(my_string.split(", "))
 # Phân tách chuỗi: Kết quả: ['Hello', 'World!']
 my_string = "Hello, World!"
 print(my_string.replace("Hello", "Hi"))
 # Thay thế chuỗi: Kết quả: 'Hi, World!'

# HÀM
# Khai báo hàm
def my_function(parameter1, parameter2):
     # Khối mã của hàm
     # Thực hiện các hoạt động dựa trên tham số được truyền vào
     result = parameter1 + parameter2
     return result

# Gọi hàm
result = my_function(10, 20) # Gọi hàm và lưu kết quả vào biến result
print(result) # in ra kết quả của hàm

#Kiểu dữ liệu có cấu trúc
để sử dụng mảng trong python. chúng ta cần import module "array"
from array import array
#Khai báo mảng số nguyên
int_array = array('i', [1, 2, 3, 4, 5])
Các kiểu dữ liệu (Typecodes) trong module array:
'b': signed char (1 byte)
'B': unsigned char (1 byte)
'I': signed int (2 bytes)
'I': unsigned int (2 bytes)
'f': float (4 bytes)
'd': double (8 bytes)
và nhiều typecodes khác.
#Truy cập vào các phần tử của array
print(int_array[0]) #truy cập vào phần tử đầu tiên trong mảng số nguyên
#Cập nhật giá trị của các phần tử trong mảng array
int_array[2] = 10 # Cập nhật giá trị của phần tử thứ ba trong mảng số nguyên

Sử dụng các phương thức của mảng: Module "array" cung cấp một số phương thức để thực hiện các thao tác với mảng:
"append()": Thêm một phần tử vào cuối mảng.
"insert()": Chèn một phần tử vào vị trí chỉ định.
"remove()": Xóa phần tử ở vị trí đầu tiên có giá trị xác định.
"pop()": Xóa phần tử ở vị trí chỉ định và trả về giá trị của phần tử đó.
"extend()": Mở rộng mảng bằng cách thêm các phần tử từ một mảng khác.
"index()": Trả về chỉ số đầu tiên của một phần tử cụ thể.
"count()": Đếm số lần xuất hiện của một phần tử trong mảng.
int_array.append(6)   # Thêm phần tử 6 vào cuối mảng số nguyên
float_array.remove(6.7) # Xóa phần tử 6.7 khỏi mảng số thực

# DANH SÁCH (LIST)
Khai báo một danh sách (List):
 # Danh sách số nguyên
 my_list = [1, 2, 3, 4, 5]
 # Danh sách chuỗi
 names = ["Alice", "Bob", "Charlie"]
 # Danh sách kết hợp kiểu dữ liệu
 mixed_list = [10, "hello", 3.14, True]

 Cách sử dụng danh sách:

Truy cập vào phần tử ở trong danh sách:
 print(my_list[0]) # Truy cập phần tử đầu tiên: Kết quả: 1
 print(names[2])   # Truy cập phần tử thứ ba: Kết quả: 'Charlie'

Cập nhật giá trị của một phần tử ở trong danh sách:
  my_list[1] = 20 # Thay đổi giá trị của phần tử thứ hai
  print(my_list)  # Kết quả: [1, 20, 3, 4, 5]

Thêm một phần tử vào danh sách:
  names.append("David") # Thêm phần tử vào cuối danh sách
  print(names)         # Kết quả: ['Alice', 'Bob', 'Charlie', 'David']

Xóa một phần tử khỏi danh sách:
   del my_list[2] # Xóa phần tử thứ ba khỏi danh sách
   print(my_list) # Kết quả: [1, 20, 4, 5]

Duyệt qua từng phần tử trong danh sách
   for element in names:
    print(element) # in từng phần tử trong danh sách

# Kiểu Tuple
- Đặc điểm kiểu Tuple
  + Không thay đổi
  + Có thứ tự
  + Có thể chứa nhiều dữ liệu 
- Ưu điểm
  + Sử dụng khi muốn đảm bảo các dữ liệu không thay đổi và không bị sửa sau khi khởi tạo
  + Tốc độ truy cập nhanh hơn

- Khai báo Tuple
 # Tuple các số nguyên
 my_tuple = (1, 2, 3, 4, 5)
 # Tuple các chuỗi
 names = ("Alice", "Bob", "Charlie")
 # Tuple kết hợp kiểu dữ liệu
 mixed_tuple = (10, "hello", 3.14)

- Truy cập vào phần tử trong tuple
 print(my_tuple[0]) # Truy cập phần tử đầu tiên: Kết quả: 1
 print(names[2])   # Truy cập phần tử thứ ba: Kết quả: 'Charlie'

- Các phương thức trong tuple
- count(value): Đếm số lần một giá trị cụ thể trong tuple xuất hiện. Ví dụ:
 my_tuple = (1, 2, 3, 1, 4, 1)
 print(my_tuple.count(1)) # Kết quả: 3 (1 xuất hiện 3 lần trong tuple)

- index(value): Trả về chỉ số đầu tiên của một giá trị cụ thể trong tuple. Ví dụ:
 my_tuple = ('a', 'b', 'c', 'd', 'b')
 print(my_tuple.index('b'))
 # Kết quả: 1 (chỉ số đầu tiên của 'b' trong tuple là 1)

# Kiểu Dictionary
Khai báo dictionary:
 # Khai báo một dictionary rỗng
 my_dict = {}
 # Khai báo một dictionary với các cặp key-value
 person = {"name": "Alice", "age": 25, "city": "New York"}

Truy cập vào giá trị trong dictionary:
Có thể truy cập giá trị trong dictionary bằng cách sử dụng key tương ứng, ví dụ:
 print(person["name"]) # In giá trị của key "name": Kết quả: "Alice"
 print(person["age"])  # In giá trị của key "age": Kết quả: 25


Dưới đây là nội dung của ảnh:

Khai báo dictionary:
 # Khai báo một dictionary rỗng
 my_dict = {}
 # Khai báo một dictionary với các cặp key-value
 person = {"name": "Alice", "age": 25, "city": "New York"} 

Truy cập vào giá trị trong dictionary:
Có thể truy cập giá trị trong dictionary bằng cách sử dụng key tương ứng, ví dụ:
 print(person["name"]) # In giá trị của key "name": Kết quả: "Alice"
 print(person["age"])  # In giá trị của key "age": Kết quả: 25

Thêm hoặc cập nhật giá trị trong dictionary:
 # Thêm một cặp key-value mới
 person["email"] = "alice@example.com"
 # Cập nhật giá trị của key đã tồn tại
 person["age"] = 26

Xóa một phần tử trong dictionary:
 # Xóa một cặp key-value từ dictionary
 del person["city"]
 # Xóa phần tử và lấy giá trị của key
 age = person.pop("age")

Các phương thức và phương dành cho dictionary:
"keys()": Trả về tất cả các keys trong dictionary.
"values()": Trả về tất cả các values trong dictionary.
"items()": Trả về tất cả các cặp key-value trong dictionary dưới dạng tuple.
 print(person.keys())   # In ra tất cả các keys trong dictionary
 print(person.values()) # In ra tất cả các values trong dictionary
 print(person.items())  # In ra tất cả các cặp key-value trong

Lưu ý:
Dictionary trong Python không có thứ tự, nghĩa là không giữ trật tự của các phần tử đã được thêm vào.
Key trong dictionary phải là duy nhất, không thể thay đổi. Còn Value có thể là bất kỳ một kiểu dữ liệu nào.

# OPP Trong python

# - Lớp class và đối tượng (object)
Lớp (Class): Là một khuôn mẫu để tạo ra các đối tượng. Nó chứa các thuộc tính (attributes) và phương thức (methods).
Đối tượng (Object): Là một thể hiện cụ thể của một lớp, có thể được tạo ra từ lớp bằng cách sử dụng từ khóa class.
 # Định nghĩa một lớp đơn giản
 class Car:
     def __init__(self, brand, model):
         self.brand = brand
         self.model = model
     def get_info(self):
         return f"{self.brand} {self.model}"
 # Tạo đối tượng từ lớp Car
 my_car = Car("Toyota", "Corolla")
 # Gọi phương thức của đối tượng
 print(my_car.get_info()) # Kết quả: Toyota Corolla

 # Khởi tạo
 class ClassName:
     def __init__(self, parameter1, parameter2, ...):
         self.parameter1 = parameter1
         self.parameter2 = parameter2
         # ...
Trong đó:
"__init__" là tên của constructor trong Python.
"self" là tham số đặc biệt đại diện cho chính đối tượng được tạo ra từ lớp.
"parameter1", "parameter2"... là các tham số bạn muốn truyền vào khi tạo đối tượng.
VD:
class Car:
     def __init__(self, brand, model):
         self.brand = brand
         self.model = model

     def get_info(self):
         return f"{self.brand} {self.model}"
 # Tạo đối tượng từ lớp Car và truy cập thông tin
 my_car = Car("Toyota", "Corolla")
 print(my_car.get_info()) # Kết quả: Toyota Corolla

 # Thuộc tính
Attribute (thuộc tính) là các biến được liên kết với đối tượng của một lớp.
Phân loại thuộc tính trong Python:
+ Thuộc tính instance (Instance Attributes): Là các thuộc tính chỉ thuộc về một đối tượng cụ thể của một lớp.
+ Thuộc tính lớp (Class Attributes): Là các thuộc tính thuộc về toàn bộ lớp, không chỉ thuộc về một đối tượng cụ thể nào đó. Chúng được chia sẻ giữa tất cả các đối tượng của lớp.

#Định nghĩa thuộc tính trong Python:
 class ClassName:
     def __init__(self, attribute1, attribute2):
         self.attribute1 = attribute1  # Thuộc tính instance
         self.attribute2 = attribute2  # Thuộc tính instance
         class_attribute = "Class Attribute"  # Thuộc tính lớp
Trong đó:
"attribute1", "attribute2": Là các thuộc tính instance, được gán giá trị khi một đối tượng được tạo.
"class_attribute": Là một thuộc tính lớp, có thể truy cập thông qua tất cả các đối tượng của lớp.

#Truy cập thuộc tính trong Python:
 # Tạo đối tượng từ lớp và truy cập các thuộc tính
 object_name = ClassName(value1, value2)
 print(object_name.attribute1)       # Truy cập thuộc tính instance
 print(object_name.class_attribute)  # Truy cập thuộc tính lớp

# Phương thức (Methods)
  #Định nghĩa một phương thức trong Python:
 class ClassName:
     def method_name(self, parameter1, parameter2):
         # Các thao tác hoặc xử lý
         return something # Trả về kết quả (nếu cần)
Trong đó:
"method_name": Tên của phương thức.
"self": Tham chiếu đến chính đối tượng của lớp. self là bắt buộc và được dùng để truy cập các thuộc tính và phương thức khác trong cùng lớp.
"parameter1", "parameter2": Các tham số mà phương thức có thể nhận (tùy chọn).
"return": Cho biết phương thức trả về một giá trị nếu cần.

  #Truy cập phương thức trong Python:
 # Tạo đối tượng từ lớp và gọi phương thức
 object_name = ClassName()
 # Gọi phương thức và truyền các tham số
 object_name.method_name(value1, value2)

# Kế thừa (Inheritance)
Trong Python, kế thừa (inheritance) là khả năng của một lớp con (child class) kế thừa thuộc tính và phương thức từ một lớp cha (parent class). Tuy nhiên, đa kế thừa (multiple inheritance) sẽ cho phép một lớp con kế thừa từ nhiều lớp cha.

- Kế thừa đơn (Single Inheritance):
 class ParentClass:
     # Định nghĩa các thuộc tính và phương thức của lớp cha
 class ChildClass(ParentClass):
     # Định nghĩa các thuộc tính và phương thức mới hoặc mở rộng từ
     # lớp cha

- Đa kế thừa (Multiple Inheritance):
 class ParentClass1:
     # Định nghĩa các thuộc tính và phương thức của lớp cha 1
 class ParentClass2:
     # Định nghĩa các thuộc tính và phương thức của lớp cha 2
 class ChildClass(ParentClass1, ParentClass2):
     # Định nghĩa các thuộc tính và phương thức mới hoặc mở rộng từ
     # các lớp cha

# Đa Hình (Polymorphism)
#Đa hình (Polymorphism) là khả năng của các đối tượng có thể hiện thực hành vi khác nhau thông qua cùng một phương thức hoặc tên hàm. 
Phân loại:
- Đa hình ở thời điểm biên dịch (Compile-time Polymorphism):
    + Được triển khai thông qua kỹ thuật "overloading" và "overriding":
      "Overloading" (Nạp chồng): Là khả năng có nhiều hàm hoặc phương thức cùng tên nhưng có các tham số khác nhau 
      hoặc kiểu dữ liệu khác nhau. Ví dụ:
      class Calculation:
          def add(self, a, b):
              return a + b
          def add(self, a, b, c):
              return a + b + c

      "Overriding" (Ghi đè): Là khả năng của một lớp con thay đổi triển khai của một phương thức
       mà đã được định nghĩa trong lớp cha. Ví dụ:
       class Animal:
           def make_sound(self):
               return "Generic sound"
       class Dog(Animal):
           def make_sound(self):
               return "Woof!"
- Đa hình ở thời điểm chạy (Runtime Polymorphism):
    + Được triển khai thông qua kỹ thuật gọi phương thức của đối tượng dựa trên lớp của đối tượng đó. Ví dụ:
 class Animal:
     def make_sound(self):
         return "Generic sound"
 class Dog(Animal):
     def make_sound(self):
         return "Woof!"
 class Cat(Animal):
     def make_sound(self):
         return "Meow!"
 # Đa hình tại thời điểm chạy
 def animal_sound(animal):
     return animal.make_sound()
 dog = Dog()
 cat = Cat()
 print(animal_sound(dog)) # Kết quả: Woof!
 print(animal_sound(cat)) # Kết quả: Meow!
 
 # Trừu tượng hóa
 Ví dụ về trừu tượng hóa
      from abc import ABC, abstractmethod
 # Lớp trừu tượng
      class Animal(ABC):
            @abstractmethod
          def make_sound(self):
              pass
 # Lớp con thực hiện (định nghĩa phương thức cụ thể)
      class Dog(Animal):
          def make_sound(self):
              return "Woof!"
 # Lớp con thực hiện (định nghĩa phương thức cụ thể)
      class Cat(Animal):
          def make_sound(self):
              return "Meow!"
 # Sử dụng các đối tượng trừu tượng
      dog = Dog()
      cat = Cat()
      print(dog.make_sound()) # Kết quả: Woof!
      print(cat.make_sound()) # Kết quả: Meow!

 Trong ví dụ trên, lớp "Animal" là lớp trừu tượng và có một phương thức trừu tượng "make_sound()", không có triển khai cụ thể. 
 Hai lớp con "Dog" và "Cat" kế thừa từ lớp "Animal" và triển khai phương thức "make_sound()" một cách cụ thể cho từng loài động vật.




