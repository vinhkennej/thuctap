# Tìm hiểu cấu trúc thư mục file system

## Cấu trúc thư mục root

![](./images/filesystem-structure.png)

### `bin` (User binaries )
 - Thư mục thực thi của người dùng

### `/sbin` (System binaries)
 - Thư mục thực thi của hệ thống .

### `/boot`(Boot Loader Files )
 - Chứa tập tin của chương trình khởi động máy 

### `/dev` (Device File)
 - Các tập tin thiết bị
 - Chứa file thiết bị như : phân vùng , ổ cứng

### `/etc` (Configure File)
 - Các tập tin cấu hình .
 - Chứa các file cấu hình toàn cục của HT như file script để khởi động hay phục vụ cho mục đích cấu hình .

### `/home` (Home Directories)
 - Thư mục làm việc của người dùng

### `/lib` (Systemlibrary)
 - chứa các file thư viện để hỗ trợ các tập tin thực thi trong `bin` `sbin`

### `/lost+found`  
 - Nếu dữ liệu bị thất lạc trong đĩa cứng thì dc lưu thư mục này và bạn có thể đọc và giữ lại DL đã mất .

### `/mnt`(Mount Directory)
 - Chứa các kết gán tạm `mount` thời đến các ổ đĩa or thiết bị khác .

### `media`(Removable Devices)
 - Tương tụ `mnt` : chứa các ổ đĩa .

### `/tmp` (Temporary Files)
 - Thư mục chứa các tập tin tạm bởi hệ thống và người dùng .

### `/usr` (User Program)
 - Chương trình của người dùng . Như thưc mục **program file** của windows

### `/proc` (Process Information)
 - Chứa thông tin về tiến trình

### `/var` (Variable Files)
 - Các tập tin biến đổi .
 - Chứa đựng các file có sự thay đổi trong quá trình HĐ của HĐH cũng như ứng dụng .
 <ul>
    <li> Nhật ký của hệ thống  *** /var/log *** </li>
    <li> Database File *** /var/lib *** </li>
    <li> Lock file ***/var/lock***</li>
    <li>Các file tạm cần cho quá trình `reboot` : ***/var/tmp*** </li>
    <li>Dữ liệu cho trang web: ***/var/www***</li>
    <li> ...</li>
 </ul>

### `/opt` (Optional add-on Applications)
 - Chứa các phần mềm và phần mở rộng ko nằm trong cài đặt mặc định

### `/sys` (System files)
 - Lưu các tập tin của hệ thống .

### `/srv` (service Data)
 - Chứa các dữ liệu liên quan đến dich vụ trên máy chủ .
