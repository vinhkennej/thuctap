# Tìm hiểu về load banncing layer 4 và load banncing layer 7

## 1. Load banncing layer 4
## 2. Load banncing layer 7
___
<span style="color:white"> Load banncers chia làm 2 loại chính : Layer 4 và layer 7 </span>

<div style="text-align:center"><img src ="images/loadblance.png" /></div>

<ul>
  <li>
   <span style="color:white"> Layer 4 load balancer xử  lí dữ liệu tìm thấy trong các giao thức ở tầng mạng và tầng giao vận (IP,TCP,UDP,FTP) </span> </li>
 <li>
 <span style="color:white"> Layer 7 load balacer phân phối y/c dựa trên dữ liệu tìm thấy trong tầng ứng dụng , lớp giao thức như HTTP . </span>
 </li>
 </ul>

 `Sơ đồ so sánh giữa Load banncing layer 4 và layer 7 `
 <div style="text-align:center"><img src="images/FreeLoadBalancerLayer4Layer7.jpg" /> </div>
___

### 1. Load balancing layer 4
 <div style="text-align:center"><img src="images/layer4.png" /> </div>
 <ul>
  <li>Layer 4 load balancer chỉ đơn giản là chuyển tiếp gói dữ liệu mạng đến và đi từ máy chủ upstream mà không kiểm tra nội dung của các gói dữ liệu. </li>
  <li>Phương pháp này điều hướng request dựa trên Range Ip và Port. Khi loadbanncer tiếp nhận 1 request , nó sẽ điều hướng dến các server backend , khi một server backend tiếp nhận request nó sẽ trả lời trực tiếp với client .  </li>
  <li> `Nhược điểm` :  Thích hợp với server chỉ có 1 website , nếu có nhiều server hoặc có các y/c phức tạp hơn thì dùng layer 7 </li>
  <li> `Ưu điểm` : Tốn ít tài nguyên do đó nhanh hơn so với cân bằng tải dựa trên layer 7 </li>
 </ul>

 ___

### 2. Load balancing layer 7
 <div style="text-align:center"><img src="images/layer7.png" /> </div>
 <ul>
  <li> Ở layer 7 load balancer hoạt động ở lớp application , nó sẽ xử lí trực tiếp với nội dung của gói dữ liệu. Nó có thể quyết định cân bằng tải dựa trên nội dung của gói tin (URL hoặc cookie...) sau đó sẽ tạo 1 kết nối TCP dến máy chủ uptream đã chọn và tạo ra y/c đến máy chủ . </li>
  <li> Chúng ta có thể chia tải dựa theo request của người dùng . Ta có thể cấu hình để chuyển các request dến static content qua các server xử lí static(html,css,js,ipg...) .  Còn các request khác thì chuyển qua cụm server xử lí dynamic content .</li>
  <li> Khác với layer 4 thì ở layer 7 ta sẽ phải đọc nội dung của request , sau đó dựa theo ALC để chuyển hướng gói tin đến cụm server tương ứng .</li>
  <li>`Nhược điểm` : Tốc độ chậm hơn so với layer 4 </li>
  <li> `Ưu điểm`: Xử lí được những y/c phân tải phức tạp. </li>
 </ul>
