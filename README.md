# HW05 - Performance Testing

## 1. Bảng tự đánh giá

| Tiêu chí | Điểm tối đa | Điểm tự đánh giá | Giải trình |
|---|---|---|---|
| 1. Scripting (3 file .jmx, CSV, Listeners) | 30 | 30 | Hoàn thành đầy đủ 3 kịch bản (Load, Stress, Spike), có dùng CSV và các Listeners khác nhau. |
| 2. Execution (Chạy test, báo cáo HTML, Log) | 20 | 20 | Thu thập đủ 3 file `.jtl`, tạo báo cáo HTML, có ảnh chụp giám sát hệ thống. |
| 3. Analysis (Phân tích log, AI Critique, Audit) | 30 | 30 | Phân tích chi tiết AI-Analysis.md, làm đủ AI Audit Report và chỉ ra lỗi ảo giác (hallucination) của AI. |
| 4. Video Demo & Báo cáo hoàn chỉnh | 20 | 20 | Quay video đầy đủ, thuyết minh rõ ràng, hoàn thành README và Bug Report. |
| **Tổng điểm** | **100** | **100** | |

## 2. Test Summary Report

- **Các kịch bản đã chạy:** 
  - Load Testing (100 VUs / 60s Ramp-up)
  - Stress Testing (500 VUs / 120s Ramp-up)
  - Spike Testing (1000 VUs / 10s Ramp-up)
- **Endpoint groups đã phủ:** 
  - Auth-heavy: `POST /api/login`
  - Read-heavy: `GET /api/products`
  - Transactional: `POST /api/products`
- **Ngưỡng chịu tải:** 
  - Max Stable RPS: ~50-60 requests/second.
  - Breaking Point: > 520 threads (bắt đầu từ chối kết nối).
- **Số lượng bug ghi nhận:** 1 Critical Bug (BUG-001: Connection refused).
- **Link Video Demo YouTube:** [Demo](https://youtu.be/KNNecFiiaIs)
- **Link Github:** [Github](https://github.com/Kugoo0807/hcmus-sw-testing-hw05)
