# Tìm hiểu cấu trúc thư mục file system

## Cấu trúc thư mục root

![](./images/filesystem-structure.png)

### `bin` (User binaries )
 - Chứa các file thực thi của người dùng .
### `/sbin` (System binaries)
 - Chứa file thực thi của hệ thống .
### `/boot`(Boot Loader Files )
 - Chứa các file boot loader khởi động hệ thống .
### `/dev` (Device File)
 - Chứa file thiết bị như : phân vùng , ổ cứng
### `/etc` (Configure File)
 - Chứa các file cấu hình toàn cục của HT như file script để khởi động hay phục vụ cho mục đích cấu hình .
### `/home` (Home Directories)
 - Thư mục làm việc của người dùng
### `/lib` (Systemlibrary)
 - chứa các file thư viện HT .
### `/lost+found`  
 - Nếu dữ liệu bị thất lạc trong đĩa cứng thì dc lưu thư mục này và bạn có thể đọc và giữ lại DL đã mất .
### `/mnt`(Mount Directory)
 - Chứa các kết gán tạm `mount` thời đến các ổ đĩa or thiết bị khác .
### `media`(Removable Devices)
 - Tương tụ `mnt` : chứa các ổ đĩa .
### `/tmp` (Temporary Files)
 - Thư mục tạm chứa các file tạm mà ctrinh chạy tạo ra
### `/usr` (User Program)
 - Chứa các chương trình của người dùng . Như thưc mục **program file** của windows
### `/proc` (Process Information)
