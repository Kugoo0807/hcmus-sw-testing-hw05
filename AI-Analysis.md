# Báo cáo Phân tích Hiệu năng Hệ thống (JMeter Log Analysis)

Dựa trên dữ liệu từ 3 kịch bản kiểm thử tải (Load, Stress, Spike), dưới đây là phân tích chi tiết về hiệu suất của hệ thống:

## 1. Phân tích Chi tiết các Kịch bản (Metrics)

### 1.1. Load Testing (`23127212_Load.jtl`)
Kịch bản mô phỏng lượng tải tiêu chuẩn.
- **Tổng quan:** 315 requests | Thời gian: 72.86s | **Tổng RPS:** 4.32 req/s | **Error Rate:** 0.0%

| API Endpoint | RPS | Avg Latency (ms) | P90 Latency (ms) | P95 Latency (ms) | Error Rate (%) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `POST /api/login` | 1.44 | 11.05 | 7 | 8 | 0.0 |
| `GET /api/products` | 1.45 | 3.01 | 4 | 5 | 0.0 |
| `POST /api/products` | 1.45 | 13.63 | 17 | 18 | 0.0 |

*Nhận xét:* Ở mức tải bình thường, hệ thống xử lý cực kỳ nhanh chóng. P95 Latency của toàn bộ các API đều dưới 20ms, không ghi nhận lỗi.

### 1.2. Stress Testing (`23127212_Stress.jtl`)
Kịch bản kiểm thử với lượng tải tăng dần và kéo dài.
- **Tổng quan:** 1500 requests | Thời gian: 119.82s | **Tổng RPS:** 12.52 req/s | **Error Rate:** 0.0%

| API Endpoint | RPS | Avg Latency (ms) | P90 Latency (ms) | P95 Latency (ms) | Error Rate (%) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `POST /api/login` | 4.17 | 5.75 | 8 | 9 | 0.0 |
| `GET /api/products` | 4.17 | 9.92 | 24 | 27 | 0.0 |
| `POST /api/products` | 4.17 | 13.64 | 19 | 21 | 0.0 |

*Nhận xét:* Hệ thống vẫn duy trì sự ổn định tuyệt vời khi chịu tải liên tục (gấp ~3 lần so với Load test). Tỷ lệ lỗi vẫn là 0% và độ trễ tăng không đáng kể (vẫn rất thấp, <30ms ở P95).

### 1.3. Spike Testing (`23127212_Spike.jtl`)
Kịch bản mô phỏng lượng truy cập tăng vọt đột biến.
- **Tổng quan:** 3000 requests | Thời gian: 18.34s | **Tổng RPS:** 163.59 req/s | **Error Rate:** 3.8%

| API Endpoint | RPS | Avg Latency (ms) | P90 Latency (ms) | P95 Latency (ms) | Error Rate (%) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `POST /api/login` | 61.00 | 2511.49 | 5606 | 5815 | 3.8 |
| `GET /api/products` | 55.92 | 1511.42 | 2407 | 2538 | 3.8 |
| `POST /api/products` | 54.59 | 1491.03 | 2426 | 2580 | 3.8 |

*Nhận xét:* Dưới áp lực của lượng truy cập đột biến lớn (>160 requests/s), hệ thống bắt đầu bộc lộ sự quá tải trầm trọng. Độ trễ tăng vọt lên hàng nghìn mili-giây (P95 của Login lên tới gần 6 giây). Tỷ lệ lỗi đồng loạt xuất hiện ở mức 3.8% ở tất cả các endpoint.

---

## 2. Tìm ra Điểm nghẽn (Bottlenecks)

1. **Khả năng xử lý đồng thời (Concurrency Limit):**
   Hệ thống không thể xử lý tốt khi tiếp nhận trên 150-160 requests/s trong cùng một thời điểm ngắn. Các request bị treo (queued/blocked) dẫn đến thời gian phản hồi tăng lên mức 2000ms - 6000ms và xuất hiện lỗi timeout hoặc 5xx/Connection Refused.
   
2. **Quá tải tại API Login (`POST /api/login`):**
   Endpoint đăng nhập có mức độ suy giảm hiệu năng nghiêm trọng nhất trong Spike test (Avg = 2511ms, P95 = 5815ms). Lý do thường gặp là thuật toán băm mật khẩu (ví dụ: `bcrypt`) tiêu thụ CPU quá lớn, khi có spike xảy ra, Thread Pool/Worker hoặc CPU của máy chủ bị cạn kiệt, kéo theo sự chậm trễ của tất cả các API khác.

3. **Cạn kiệt Connection Pool cơ sở dữ liệu:**
   Tỷ lệ lỗi chia đều 3.8% trên cả 3 API cho thấy đây là lỗi hệ thống diện rộng, khả năng cao do Pool kết nối tới cơ sở dữ liệu đã bị cạn kiệt (Database Connection Exhaustion). Các request mới không lấy được kết nối DB nên bị lỗi timeout và fail.

---

## 3. Đề xuất Ngưỡng chịu tải (Performance Thresholds)

Dựa trên kết quả đo lường, thiết lập ngưỡng cho hệ thống hiện tại:
- **Ngưỡng Tải Bình Thường (Normal / Optimal Load):** `~10 - 20 RPS`
  * Ở mức độ này, hệ thống hoạt động hoàn hảo, Latency P95 luôn được duy trì ở mức `<30ms` với tỷ lệ lỗi `0%`.
- **Ngưỡng Cảnh Báo (Warning Threshold):** `~50 - 60 RPS`
  * Khi lưu lượng đạt mức này, tài nguyên bắt đầu bị cạnh tranh. Thời gian phản hồi có thể vượt mốc SLA.
- **Ngưỡng Phá Vỡ (Breaking Point / Max Capacity):** `> 150 RPS`
  * Vượt mức này hệ thống rơi vào trạng thái thắt cổ chai, request bắt đầu bị rớt hoặc timeout (`Error Rate > 3%`), Latency vượt quá `2000ms`. Không đáp ứng được các tiêu chuẩn UX thông thường.

---

## 4. Các giải pháp tối ưu hệ thống

1. **Tối ưu hóa Database & Connection Pool:**
   - Tăng kích thước Connection Pool (Max Connections) ở phía Backend để chịu được lượng kết nối đồng thời cao hơn.
   - Kiểm tra và đảm bảo các bảng cơ sở dữ liệu đã được tối ưu Index để thao tác Read/Write (`GET/POST /api/products`) nhanh nhất có thể.

2. **Cấu hình Rate Limiting (Throttling):**
   - Thiết lập Rate Limit trên API Gateway / Nginx / Middleware để ngăn chặn lượng spike gây sập server. Trả về sớm HTTP `429 Too Many Requests` với những request vượt ngưỡng thay vì để request xếp hàng đợi làm cạn kiệt CPU/RAM.

3. **Tối ưu Cơ chế Đăng nhập (Authentication):**
   - Nếu sử dụng bcrypt, cân nhắc điều chỉnh Cost Factor (Work Factor) sao cho vừa đủ an toàn nhưng không ngốn quá nhiều CPU (ví dụ: cost = 10 là mức hợp lý hiện nay). 
   - Đảm bảo cơ chế caching session hoặc JWT generation được thực thi tối ưu.

4. **Caching dữ liệu:**
   - Triển khai Redis / Memcached cho các API chỉ đọc như `GET /api/products`. Điều này sẽ chia sẻ tải cho DB, cho phép RPS tăng mạnh ở thao tác Read.

5. **Mở rộng theo chiều ngang (Scale Out):**
   - Do giới hạn của 1 node/instance khoảng 150 RPS, để phục vụ lượng Spike lớn, cần thiết lập Load Balancer và Auto-scaling chạy nhiều instance (pods/containers) để chia sẻ tải lượng khi có truy cập đột biến.
