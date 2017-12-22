###Understanding the Boot ProcessProcess

![](images/linux-boot-process.png)

- Quá trình khởi động Linux là một thủ tục để khởi tạo hệ thống. Nó bao gồm mọi điều xảy ra từ lúc nhần nút nguồn để khởi động máy tính cho đến khi đăng nhập vào để thực hiện các công việc.
-  Nó sẽ trải qua 6 giai đoạn : Bios - > MBR -> GRUB -> Kernel -> Init -> Runlevel

###1. Power On
- Khi nhấn nút khởi động nguồn, chương trình BIOS sẽ chạy đầu tiên. BIOS sẽ thực hiện một công việc gọi là POST nhằm kiểm tra phần cứng.

- Khi quá trình POST kết thúc thành công, BIOS sẽ tìm kiếm và khởi chạy một hệ điều hành chứa trong ổ cứng, USB…Sau đó phần còn lại của quá trình khởi động được kiểm soát bởi hệ điều hành.

###2. Master Boot Record (MBR)
- Sector đầu tiên của một thiết bị lưu trữ được gọi là MBR.

- BIOS sẽ đọc MRB của thiết bị này để nạp vào bộ nhớ một chương trình rất nhỏ. Chương trình nhỏ này sẽ định vị và khởi động boot loader – đây là chương trình chịu trách nhiệm cho việc tìm và nạp nhân (kernel) của hệ điều hành.

- Đến giai đoạn này, máy tính sẽ không truy cập vào bất kì phương tiện lưu trữ nào. Các thông tin về ngày tháng, thời gian và các thiết bị  ngoại vi quan trọng nhất được nạp từ CMOS.

###3. Boot Loader
- Boot loader sẽ nằm trong Master Boot Record (MBR). Khi khởi động Linux, boot loader có trách nhiệm nạp kernel và Initial RAM Disk (có chứa một số tệp quan trọng và trình điều khiển thiết bị cần thiết để khởi động hệ thống) vào bộ nhớ.

- Bood loader bao gồm hai giai đoạn:

*Giai đoạn thứ nhất:*

<ul>
<li>Đổi với các hệ thống sử dụng BIOS/MBR, boot loader nằm tại sector đầu tiên của bộ nhớ hay còn gọi là Master Boot Record (MBR). Kích thước của MBR vào khoảng 512 bytes. Trong giai đoạn này boot loader kiểm tra các phân vùng để tìm ra phân vùng chứa hệ điều hành. Khi tìm thấy phân vùng khởi động, nó sẽ tìm một boot loader như là GRUB và tải nó vào RAM.</li>

<li>Đối với các hệ thống sử dụng EFI/UEFI, các firmware UEFI sẽ đọc dữ liệu Boot Manager để tìm các ứng dụng UEFI. Firmware sẽ chạy ứng dụng UEFI</li>
</ul>

*Giai đoạn thứ hai:*
<ul>
<li>Boot loader nằm trong thư mục /boot. Một màn hình hiển thị cho phép chúng ta chọn OS để khởi động. Sau đó boot loader sẽ nạp kernel của hệ điều hành đó vào bộ nhớ RAM và chuyển quyền điều khiển máy tính cho kernel này.</li>
</ul>

####4. Linux kernel được nạp và khởi chạy

- Boot loader sẽ nạp hạt nhân và các file system RAM vào bộ nhớ hệ thống để kernel có thể sử dụng trực tiếp. Khi hạt nhận được nạp vào bộ nhớ RAM, nó ngay lập tức khởi tạo và cấu hình bộ nhớ máy tính hoặc tất cả các phần cứng được gắn vào.

###5. Inital RAM Disk

- Các INITRD cung cấp một giải pháp: một tập các chương trình nhỏ sẽ được thực thi khi kernel vừa mới được khởi chạy. Các chương trình nhỏ này sẽ dò quét phần cứng của hệ thống và xác định xem kernel cần được hỗ trợ thêm những gì để có thể quản lý được các phần cứng đó. Chương trình INITRD có thể nạp thêm vào kernel các module bổ trợ. Khi chương trình INITRD kết thúc thì quá trình khởi động Linux sẽ tiếp diễn.

###6. Các run level và service

- init là tiến trình đầu tiên chạy trong hệ thống Linux: ID của tiến trình này là 1.

- File cấu hình runlevel /etc/inittab

Runlevel 0: tắt hệ thống
Runlevel 1: chế độ đơn người sử dụng
Runlevel 2: chế độ multi user
Runlevel 3: chế độ đa người dùng không có giao diện đồ họa
Runlevel 4: không sử dụng
Runlevel 5: chế độ đa người dùng có giao diện đồ họa
Runlevel 6: reboot hệ thống