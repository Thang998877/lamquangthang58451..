"""
Tác giả: Lâm Quang Thắng
Ngày: 23/10/2021
Vấn đề:
  Xác định và kiểm tra hàm myRange. Hàm này sẽ hoạt động giống như Python
hàm phạm vi tiêu chuẩn, với các đối số bắt buộc và tùy chọn, nhưng nó phải
trả lại một danh sách. Không sử dụng hàm phạm vi trong quá trình triển khai của bạn! (Gợi ý:
Nghiên cứu sự trợ giúp của Python về phạm vi để xác định tên, vị trí và những việc cần làm
với các tham số của chức năng của bạn. Sử dụng giá trị mặc định là Không có cho hai tùy chọn
thông số. Nếu cả hai tham số này đều bằng Không, thì hàm đã
được gọi chỉ với giá trị dừng. Nếu chỉ tham số thứ ba bằng Không, thì
hàm cũng đã được gọi với một giá trị bắt đầu. Do đó, phần đầu tiên của mã của hàm thiết lập giá trị của
các tham số là hoặc nên là. Các
phần còn lại của mã sử dụng các giá trị đó để tạo danh sách bằng cách đếm lên hoặc đếm ngược.)

Giải pháp:
    ....
"""
def myrange(start, stop=None, step=None):
    lyst=[]
    if stop == None and step==None:
        stop = start
        start = 0
        step = 1
    if start < stop:
        if step == None:
            step=1
        elif step <=0:
            return lyst
        while start < stop:
            lyst.append(start)
            start+=step
    else:
        if step == None or step>-1:
            return lyst
        while start>stop:
            lyst.append(start)
            start+=step
    return lyst
def main():
    print(myrange(10))
    print(myrange(1,10))
    print(myrange(1,10,2))
    print(myrange(10,1,-1))

main()