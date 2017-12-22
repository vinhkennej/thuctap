# Tìm hiểu về Iptables
### Mục lục


[I. Tổng quan về Iptables](#about-iptables)

[II. Cấu trúc và cơ chế hoạt động của Iptables](#cautruc-iptables)

  [1. Kiến trúc](#kien-truc)
  
  [1.1. Iptables tables và Chains](#iptables-chains)
  
  [1.2. Iptables rules](#iptables-rules)
  
  [1.3. Cơ chế xử lý gói tin](#co-che-iptables)  
  
  [1.4. Sử dụng Iptables](#using-iptables)
  
---
  
### <a name="about-iptables"></a> I. Tổng quan về Iptables

- Iptables là một ứng dụng dùng để quản lý filtering gói tin và NAT rules hoạt động trên console của linux rất nhỏ và tiện dụng. Được cung cấp miễn phí nhằm nâng cao tính bảo mật trên hệ thống Linux.

- ptables bao gồm 2 phần là netfilter nằm bên trong nhân Linux và iptables nằm ở vùng ngoài nhân. iptables chịu trách nhiệm giao tiếp với người dùng và sau đó đẩy rules của người dùng vào cho netfilter xử lý. netfilter thực hiện công việc lọc các gói tin ở mức IP. 

***Một số chức năng của IPtables :***

- Có khả năng phân tích gói tin hiệu quả.
- Filtering gói tin dựa vào MAC và một số cờ hiệu (flags) trong TCP Header.
- Cung cấp kỹ thuật NAT, chi tiết cho các tùy chọn để ghi nhận sự kiện hệ thống.
- Có khả năng ngăn chặn một số cơ chế tấn công theo kiểu DoS.
- Xây dựng một hệ thống tường lửa (firewall).
- Cung cấp, xây dựng và quản lý các rule để xử lý các gói tin.

---

### <a name="cautruc-iptables"></a> I. Cấu trúc và cơ chế hoạt động của Iptables
  
 - Cấu trúc  : iptables -> Tables -> Chains -> Rules 
 
 ![](images/structure.png)
####<a name="iptables-chains"></a>2.1. Iptables tables và chains

- Iptables có 4 bảng :
<ul>
<li>Filer table</li>
<li>NAT table</li>
<li>Mangle table</li>
<li>Raw table</li>
</ul>

***Filter table :***
- Filter là bảng mặc định của iptables. 
- Iptables filter gồm các chains :
    + INPUT chain – Incoming to firewall : Lọc các packet khi đi vào server
    + OUTPUT chain – Outgoing from firewall : Lọc các packet khi đi ra ngoài server.  
    + FORWARD chain – Packet for another NIC on the local server :Lọc gói khi đi đến các server khác.
    
***NAT table***
- PREROUTING chain :  thay đổi địa chỉ đến của gói dữ liệu khi cần thiết.(DNAT)
- POSTROUTING chain :  thay đổi địa chỉ nguồn của gói dữ liệu khi cần thiết. (SNAT)
- OUTPUT chain - Nat với gói dữ liệu được tạo từ local.

***Mangle table***
- Chịu trách nhiệm thay đổi các QoS bits trong TCP header như TOS (type of service), TTL (time to live), và MARK.
- Gồm các chains:
+ PREROUTING chain
+ OUTPUT chain
+ FORWARD chain
+ INPUT chain
+ POSTROUTING chain

***Raw table***
- DÙng cho việc loại trừ cấu hình.
- Gồm các chains:
+ PREROUTING chain
+ OUTPUT chain

![](images/iptables-filter-nat-mangle-tables.png)

---

#### <a name="iptables-chains"></a> 2.2. Iptables rules

***Targets***

- Target là hành động diễn ra khi một gói dữ liệu được kiểm tra phù hợp với một yêu cầu nào đó. Khi một target đã được nhận dạng, gói dữ liệu cần nhảy (jump) để thực hiện các xử lý tiếp theo. Bảng sau liệt kê các targets mà iptables sử dụng.
+ ACCEPT: chấp nhận gói tin, cho phép gói tin đi vào hệ thống.
+ DROP: iptables chặn hoặc loại bỏ gói tin này.
+ REJECT: Tương tự như DROP nhưng nó sẽ trả lại cho phía gửi một thông báo rằng gói đã bị chặn và loại bỏ.
+ LOG: chấp nhận gói tin nhưng có ghi lại log.
+ DNAT: Dùng để thực hiện thay đổi địa chỉ đích của gói dữ liệu.
+ SNAT : Thay đổi địa chỉ nguồn của gói dữ liệu.

#### <a name="iptables-chains"></a> 2.3. Quá trình xử lý gói tin trong iptables:

 ![](images/iptables-process.png)

- Đầu tiên gói tin từ mạng A đi vào hệ thống firewall sẽ phải đi qua bảng Mangle với chain là PREROUTING (với mục đích để thay đổi một số thông tin của gói tin trước khi định tuyến).
- Sau đó gói tin đến bảng NAT với chain PREROUTING tại đây địa chỉ IP đích của gói tin có thể bị thay đổi DNAT, sau đó qua bộ routing và sẽ quyết định xem gói tin đó thuộc firewall hay không:

<ul>
<li> TH1:  Đối với packet đi vào máy : gói tin sẽ đi qua bảng mangle và đến bản filter với chai INPUT. Tại chain INPUT, packet có thể được chấp nhận hoặc bị hủy bỏ. Sau quá trình xử lý gói tin sẽ đi đến bảng mangle tiếp đến là bảng NAT với chain OUTPUT được áp dụng một số chính sách và sau đó đi lần lượt qua các bảng magle với chain POSTROUTING cuối cùng đi đến bảng NAT với chain POSTROUTING để thay đổi địa chỉ nguồn nếu cần thiết.
 </li>
 <li>  TH2  : Đối với packet forward qua máy, sẽ được đưa đến bảng Mangle với chain FORWARD rồi đến bảng filter với chain FORWARD. Đây là chain được sử dụng rất nhiều để bảo vệ người sử dụng mang trong lan với người sử dụng internet các gói tin thoải mãn các rule đặt ra mới có thể được chuyển qua giữa các card mạng với nhau, qua đó có nhiệm vụ thực hiện chính sách với người sử dụng nội bộ nhưng không cho vào internet, giới hạn thời gian,...và bảo vệ hệ thống máy chủ đối với người dung internet bên ngoài chống các kiểu tấn công. sau khi đi qua card mạng với nhau gói tin phải đi lần lượt qua bảng mangle và NAT với chain POSTROUTING để thực hiên việc chuyển đổi địa chỉ nguồn với target SNAT & MASQUERADE.
 
</li>
  </ul>
  
#### <a name="using-iptables"></a>2.4. Sử dụng Iptables
  
  - Cú pháp sử dụng :
```
iptables [-t table] {-A|-C|-D} chain rule-specification

iptables [-t table] -I chain [rulenum] rule-specification

iptables [-t table] -R chain rulenum rule-specification

iptables [-t table] -D chain rulenum

iptables [-t table] -S [chain [rulenum]]

iptables [-t table] {-F|-L|-Z} [chain [rulenum]] [options...]

iptables [-t table] -N chain

iptables [-t table] -X [chain]

iptables [-t table] -P chain target

iptables [-t table] -E old-chain-name new-chain-name

rule-specification = [matches...] [target]

match = -m matchname [per-match-options]

target = -j targetname [per-target-options]   
```

- Các Option :
```
   -t : chọn bảng (default là filter table).

   -i: interface input.

   -o: interface output.

   -A: thêm  1 rule.

   -D: xóa 1 rule.

   -p: chỉ đinh loại giao thức.

   --icmp--type :xác định rõ loại giao thức.

   -J : chuyển đến mục tiêu.

   -s : địa chỉ gói tin nguồn.

   -d: địa chỉ gói tin đích.

   -I : chèn thêm rule.

   -R : Thay thế rule.
   
   -sport : địa chỉ cổng nguồn
   
   -dport: địa chỉ cổng đích
   
    ...
```

***Một số lệnh cơ bản***

`iptables -A INPUT -i eth0 –dport 80 -j ACCEPT ` :  chấp nhận các packet vào cổng 80 trên card mạng eth0.

`iptables  -A INPUT -p tcp -j DROP ` :  Chặn tất cả các gói tin đi vào chạy giao thức TCP 

`iptables -A INPUT -p tcp --dport 6881 -j ACCEPT` : Chấp nhận gói tin tcp với port đích 6881
