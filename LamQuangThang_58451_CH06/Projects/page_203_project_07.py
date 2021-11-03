"""
Tác giả: Lâm Quang Thắng
Ngày: 23/10/2021
Vấn đề:
  Viết một hàm đệ quy yêu cầu một tên đường dẫn làm đối số. Tên đường dẫn có thể
là tên của một tệp hoặc tên của một thư mục. Nếu tên đường dẫn
đề cập đến một tệp, tên của nó được hiển thị, theo sau là nội dung của nó. Ngược lại, nếu
tên đường dẫn đề cập đến một thư mục, hàm được áp dụng cho mỗi tên trong thư mục.
Kiểm tra chức năng này trong một chương trình mới.
Giải pháp:
    ....
"""
import os
import os.path
def main():
    displayfiles(os.getcwd())

def displayfiles(path):
    if os.path.isfile(path):
        print("File name"+path)
        f=open(path, 'r')
        print(f.read)
    else:
        print("Directory name: " + path)
        lyst=os.listdir(path)
        for element in lyst:
            recursive_element = os.path.join(path, element)
            print("element: ", element)
            print("recursive_element: ", recursive_element)
            displayfiles(recursive_element)
if __name__=='__main__':
    print("Directory: {os.getcwd()}")
    displayfiles(os.getcwd())


main()