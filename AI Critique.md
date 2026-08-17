# Đánh giá và Phản biện AI (AI Critique)

---

### 1. Những sai sót và điểm chưa hoàn thiện của AI

Trong quá trình thực hiện bài tập, AI đã mắc phải một số sai sót nghiêm trọng ở cả giai đoạn thiết kế kịch bản và giai đoạn phân tích dữ liệu. Về thiết kế, AI gặp vấn đề "ảo giác" với API Contract khi tự ý đổi endpoint từ `/api/login` thành `/api/auth/login` và sai kiểu dữ liệu của biến môi trường (port). Đáng chú ý nhất là ở khâu phân tích file log `.jtl` (Task 2), AI đã đọc lướt qua lỗi "Connection refused" khi số lượng thread vượt ngưỡng 520 ở kịch bản Spike Test, dẫn đến kết luận thiếu độ sâu về ngưỡng phá vỡ của hệ thống (Breaking point). Thêm vào đó, AI đã đưa ra một đề xuất tối ưu "ảo giác" là thêm Database Index cho API đăng nhập, trong khi thực tế sự cố thắt cổ chai ở đây là do cạn kiệt tài nguyên CPU để xử lý thuật toán mã hoá mật khẩu (bcrypt).

---

### 2. Nguyên nhân AI bỏ sót các vấn đề

Sự yếu kém trong việc phát hiện nguyên nhân gốc rễ (Root Cause Analysis) bắt nguồn từ việc AI xử lý một lượng lớn văn bản thô từ file `.jtl` bằng cách lấy mẫu (sampling) hoặc tổng hợp dữ liệu thống kê chung thay vì rà soát từng dòng log dị biệt. Khi đối mặt với tỉ lệ lỗi nhỏ (3.8%), AI đã gộp chung chúng vào các lỗi "quá tải" thông thường mà không bóc tách chi tiết thông điệp Exception của JMeter. Đề xuất thêm Index DB là một ví dụ điển hình của việc AI sử dụng kiến thức chung chung học được về tối ưu hoá hiệu năng, áp dụng một cách rập khuôn mà không phân tích đặc thù của chức năng Authentication.

---

### 3. Bài học rút ra khi cộng tác với AI

Bài học quan trọng nhất là áp dụng nguyên tắc "AI-First nhưng Human-Verified" một cách khắt khe. AI đóng vai trò như một trợ lý giúp tăng tốc độ thiết lập môi trường và cấu trúc dữ liệu, nhưng không thể thay thế tư duy kỹ thuật của một kỹ sư. Con người phải luôn chịu trách nhiệm cuối cùng trong việc thiết lập hợp đồng API (API Contracts), xác định các điểm bất thường trong log dữ liệu lớn, và đặc biệt là phải sử dụng tư duy phản biện (Critical Thinking) để thẩm định tính khả thi của các đề xuất tối ưu kiến trúc hệ thống mà AI đưa ra.
