"""
Tác giả: Lâm Quang Thắng
Ngày: 23/10/2021
Vấn đề:
  Lee đã khám phá ra những gì anh ấy nghĩ là một chiến lược đệ quy thông minh để in
các phần tử trong một chuỗi (chuỗi, bộ hoặc danh sách). Anh ấy lý do rằng anh ấy có thể nhận được ở
phần tử đầu tiên trong một chuỗi sử dụng chỉ mục 0 và anh ta có thể nhận được một chuỗi
phần còn lại của các yếu tố bằng cách cắt từ chỉ mục 1. Chiến lược này được thực hiện trong một
hàm chỉ mong đợi chuỗi như một đối số. Nếu trình tự không
rỗng, phần tử đầu tiên trong chuỗi được in và sau đó một cuộc gọi đệ quy là
Thực thi. Trên mỗi lệnh gọi đệ quy, đối số trình tự được cắt bằng cách sử dụng
phạm vi 1:. Đây là định nghĩa hàm của Lee:
def printAll (seq):
nếu seq:
print (seq [0])
printAll (seq [1:])
Viết một tập lệnh kiểm tra chức năng này và thêm mã để theo dõi đối số trên mỗi
gọi. Chức năng này có hoạt động như mong đợi không? Nếu vậy, hãy giải thích cách nó thực sự hoạt động,
và mô tả bất kỳ chi phí ẩn nào trong việc chạy nó.

Giải pháp:
    ....
"""
def printall(seq):
    if seq:
        print(seq, "->", seq[0])
        printall(seq[1:])

printall(list(range(10)))