# Tìm hiểu về dạng file system trong linux
##  Journaling là gì ?
   ![](http://www.quantrimang.com.vn/photos/image/012012/19/linuxfilesystem--02.jpg)
 - chỉ được sd khi ghi dữ liệu lên ổ cứng và đóng vai trò như chiếc đục lỗ để ghi thông tin lên phân vùng .
 - Nếu không có journaling thì HĐH ko biết được file dữ liệu có được ghi đầy đủ tới ổ cứng hay ko .

  `Qúa trình`
   <ul>
      <li> Đầu tiên , File sẽ được ghi vào Journal ,đẩy vào bên trong lớp quản lí dữ liệu  </li>
      <li> Sau đó , journal sẽ ghi dữ liệu vào phân vùng ổ cứng .  </li>
      <li> Nếu thành công , file sẽ được xóa bỏ khỏi journal ,đảy ra bên ngoài và qtrinh hoàn tất </li>
      <li> Nếu lỗi , file hệ thống kiểm tra lại journal và tất cả thao tác chưa đc thực hiện, đồng thời ghi lại đúng vị trí xảy ra lỗi .</li>
   </ul>

****
## 1. Ext (Extended file system) :
 - Là định dạng file hệ thống đầu tiên dành cho linux .
 - Giờ ít dùng vì ko hỗ trợ nhiều distribution .

## 2. Ext2
 - Ko phải là file hệ thống của journaling , kế thừa định dạng hệ thống cũ .
 - Ko sử dụng journal nên sẽ có ít dữ liệu dc ghi vào ổ đĩa hơn
 - Do yêu cầu viết và xóa DL khá thấp nên phù hợp vs thiết bị lưu trữ ngoài như usb , thẻ nhớ ..

## 3. Ext3
 - Căn bản là Ext2 đi kèm với journal
 - Dễ dàng chuyển đổi 2 chế độ (ext 2-3) mà ko cần format
 - Ưu điểm : Hoạt động nhanh và ổn định .
 - Nhược điểm : Không phù hợp làm định dạng file hệ thống cho máy chủ vì ko hỗ trợ tính năng tạo `disk snapshot` và file được khôi phục sẽ rất khó `xóa bỏ` sau này .

## 4. Ext4
 - Cũng giống ext3 , lưu giữ dc nhiều ưu điểm và tính năng tương thích ngược với các phiên bản trước đó => dễ dàng kết hợp các phân vùng định dạng ext2,ext3,ext4 trong cùng 1 ổ đĩa trong Ubuntu để tăng hiệu suất hoạt động .

 - `Ưu điểm ` : Giảm bớt hiện tượng phân mảnh dữ liệu trong ổ cứng và lưu trữ file và phân vùng có dung lượng lớn .  
 - Thích hợp với ổ SSD so với Ext3 , hđ nhanh hơn .
 - Khá phù hợp để hđ trên server nhưng ko bằng `Ext3`

## 5. Swap
  - Có thể coi ko phải là định dạng file hệ thống , vì cơ chế khác biệt .
  - Sử dụng để làm `Ram ảo` cho máy tính .
  - Nếu muốn sử dụng tính năng ngủ đông `Hibernation` thì fai có `swap`
