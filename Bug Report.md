# BÁO CÁO LỖI (BUG REPORTS)

---

## Danh sách lỗi tổng hợp
| ID | Tóm tắt | Mức độ | Trạng thái |
|---|---|---|---|
| BUG-001 | Hệ thống bị sập (Connection Refused) dưới tải trọng lớn trong kịch bản Spike Test | Critical | Mới tạo |

---

## Chi tiết từng Bug

### BUG-001: Hệ thống bị sập (Connection Refused) dưới tải trọng lớn trong kịch bản Spike Test

**Mô tả:** 
Trong quá trình thực hiện kịch bản Spike Test với tải trọng tăng vọt lên 1000 VUs, hệ thống Node.js (cổng 3000) không thể xử lý kịp lượng kết nối và đã bị sập (ngừng nhận request mới).

**Mức độ nghiêm trọng (Severity):** Critical

**Các bước tái hiện:**
1. Khởi động server Node.js EShop trên cổng 3000 (localhost:3000).
2. Chạy kịch bản Spike Test bằng JMeter.
3. Thiết lập Thread Group với 1000 Virtual Users, Ramp-up trong 10 giây.
4. Gửi các request POST đến `/api/login` và `/api/products`.
5. Quan sát Listener View Results Tree và file log `.jtl`.

**Kết quả thực tế (Actual Result):**
- Server từ chối kết nối khi số lượng threads vượt mốc 521.
- Ghi nhận 114 lỗi trong báo cáo HTML Report của JMeter (chiếm 100% tổng số lỗi và 3.8% tổng số requests).
- Thông báo lỗi trong log: `Non HTTP response code: org.apache.http.conn.HttpHostConnectException - Connect to localhost:3000 failed: Connection refused: connect`.

**Kết quả mong đợi (Expected Result):**
- Hệ thống duy trì được kết nối hoặc có cơ chế hàng đợi (queue) hoặc từ chối request một cách thanh lịch (graceful degradation) trả về mã lỗi 503 thay vì bị sập `Connection refused`.

**Môi trường:**
- Backend: Node.js (localhost:3000)
- Công cụ test: Apache JMeter
- OS: Windows

**Bằng chứng đính kèm:**
- File log: `23127212_Spike.jtl`
- HTML Report: Thống kê 114 lỗi Connection refused.
