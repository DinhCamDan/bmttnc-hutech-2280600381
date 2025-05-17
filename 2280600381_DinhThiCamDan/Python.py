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


