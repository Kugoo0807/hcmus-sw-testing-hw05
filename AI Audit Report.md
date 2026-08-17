**Khoa Công nghệ Thông tin (FIT) – Trường Đại học Khoa học Tự nhiên (HCMUS)**

**CS423 / CSC13003 – Kiểm chứng Phần mềm (AI-augmented · 2026\)**

**CHÍNH SÁCH AI · BIỂU MẪU — 2026 v1.0**

# **AI Audit Report — Mẫu 5 mục cho mỗi Artifact**

*Phụ lục bắt buộc đính kèm cho mọi bài tập có dùng AI (HW\#01–HW\#06, Seminar).*

*Tài liệu được biên soạn lại từ Med Kharbach, PhD (2026) — Mẫu Chính sách Sử dụng AI cho Giáo dục Đại học. Giấy phép CC BY-NC-SA 4.0. Phiên bản này được FIT@HCMUS điều chỉnh cho môn CS423 / CSC15003 Kiểm chứng Phần mềm.*

## **1\. Thông tin Sinh viên**

| Mục | Giá trị |
| :---- | :---- |
| **Họ tên sinh viên (in hoa):** | NGUYỄN QUANG ĐĂNG KHOA |
| **MSSV:** | 23127212 |
| **Lớp / Khoá:** | 23KTPM2 |
| **Mã bài tập (ví dụ HW\#00, HW\#02):** | HW05 |
| **Ngày làm bài:** | 14/08/2026 |
| **Công cụ AI đã dùng:** | Gemini 3.1 Pro; Antigravity (Google DeepMind); Claude Sonnet 4.6 |
| **Công cụ AI đã dùng:** | \[X\] Có  \[ \] Không |

## **2\. Hướng dẫn (đọc trước khi điền)**

* Thêm 1 hàng cho mỗi artifact AI sinh (test case, script, checklist, OpenAPI spec, JMeter plan…).  
* Dán nguyên văn prompt — KHÔNG paraphrase.  
* Dán nguyên văn output AI (hoặc kèm screenshot có chú thích trong báo cáo).  
* Gắn nhãn: VALID / INVALID / INCOMPLETE.  
* Lý do phải dẫn chiếu slide, mục ISTQB, hoặc RFC kỹ thuật.  
* Hiển thị bản sửa với phần thay đổi được tô sáng.  
* Hàng mẫu in nghiêng — thay trước khi nộp.

## **3\. Bảng Audit — 1 hàng / artifact**

| (1) Prompt \+ Công cụ | (2) Output AI | (3) Verdict | (4) Lý do (ISTQB) | (5) Bản SV sửa |
| :---- | :---- | :---- | :---- | :---- |
| (1) Prompt \+ Công cụ | (2) Output AI | (3) Verdict | (4) Lý do (ISTQB) | (5) Bản SV sửa |
| :---- | :---- | :---- | :---- | :---- |
| **Tool: Gemini**<br>Thời gian: 21:52 12/08/2026<br>Prompt:<br>"*Tóm tắt nội dung HW05, các bước cần thực hiện và output của mỗi bước. Kết quả nộp bài là gì và cần kiểm tra gì trước khi nộp bài?*" | # 1. Tóm tắt nội dung HW05<br/>Bài tập HW05 yêu cầu thực hiện Kiểm thử Hiệu năng (Load, Stress, Spike) cho backend API của SUT (EShop) bằng JMeter hoặc k6, áp dụng chiến lược "AI-First". Sinh viên dùng AI để hỗ trợ thiết kế test plan, phân tích log, sau đó phải tự rà soát, đánh giá lỗi sai của AI và đề xuất pipeline kiểm thử liên tục.<br/><br/># 2. Các bước thực hiện & Output<br/>## Bước 1: Chọn API Endpoint<br/>**Hành động:** Chọn 3 nhóm endpoint (Read-heavy, Auth-heavy, Transactional), không trùng với đồng đội.<br/>**Output:** Danh sách 3 endpoint group trong báo cáo.<br/><br/>## Bước 2: AI thiết kế kịch bản<br/>**Hành động:** Dùng AI tạo 3 test plan sử dụng dữ liệu CSV và 3 loại report/listener khác nhau.<br/>**Output:** 3 file test plan (`{StudentID}_{ScenarioType}_{YYYYMMDD}`) và file dữ liệu CSV.<br/><br/>## Bước 3: Đánh giá & sửa lỗi kịch bản AI<br/>**Hành động:** Review kịch bản, tìm lỗi của AI (sai luồng, thiếu xử lý lockout...) và tự sửa.<br/>**Output:** Phân tích lỗi thiết kế của AI trong báo cáo.<br/><br/>## Bước 4: Thực thi & thu thập bằng chứng<br/>**Hành động:** Chạy 3 kịch bản, chụp ảnh màn hình tài nguyên (htop/Task Manager) và phần cứng. Chạy bài test sức bền (endurance test) 10-15 phút để tìm ngưỡng.<br/>**Output:** File log `.jtl`, thư mục báo cáo HTML, ảnh chụp màn hình, chỉ số ngưỡng phần cứng.<br/><br/>## Bước 5: Quay video demo<br/>**Hành động:** Quay video YouTube (unlisted) >= 6 phút, hiển thị tool + monitor, thuyết minh tiếng Việt.<br/>**Output:** Link video YouTube.<br/><br/>## Bước 6: AI phân tích log & Sinh viên phản biện<br/>**Hành động:** AI phân tích log `.jtl`. Sinh viên review xem AI đọc sai chỉ số nào (trích dẫn log thật để chứng minh) và đánh giá các đề xuất tối ưu của AI là khả thi hay "ảo giác".<br/>**Output:** Báo cáo phân tích AI và phần phản biện (misinterpretation hunt).<br/><br/>## Bước 7: Đề xuất Continuous Performance Testing<br/>**Hành động:** Đề xuất pipeline kiểm thử liên tục kèm flow chart và phân tích trade-offs.<br/>**Output:** Phần đề xuất trong báo cáo.<br/><br/>## Bước 8: Báo cáo AI & Git<br/>**Hành động:** Viết AI Audit Report, AI Critique (200-300 từ) và duy trì Git commit.<br/>**Output:** AI Audit Report, AI Critique (MD+PDF), Git commit log (text).<br/><br/># 3. Kết quả nộp bài<br/>File `.zip` (`<StudentID>_HW05_AI_Performance_<SelfAssessedGrade>.zip`) chứa:<br/>- Báo cáo chính (MD+PDF).<br/>- Link GitHub repo.<br/>- 3 test plans, 3 logs `.jtl`, 3 HTML reports.<br/>- Ảnh chụp resource & hardware.<br/>- Link video YouTube.<br/>- AI Critique & Audit Report (MD+PDF).<br/>- Git log (text) & Bug reports.<br/>- File `README.md` (tự đánh giá & tổng kết).<br/><br/># 4. Kiểm tra trước khi nộp (Checklist)<br/>- **Tên file test plan:** Cú pháp `{StudentID}_{ScenarioType}_{YYYYMMDD}`.<br/>- **File log:** Nộp đủ file log `.jtl` thô.<br/>- **Video:** Hiển thị tool + resource monitor trên cùng màn hình, có thuyết minh.<br/>- **Hardware report:** Hostname khớp với các HW trước.<br/>- **Độc lập:** Không chọn trùng endpoint, không chép prompt. Nộp trễ/thiếu tài liệu = 0 điểm. | **VALID** | AI tóm tắt chính xác, đầy đủ các Task, Output và các ràng buộc (Anti-AI-Cheat) trong tài liệu hướng dẫn HW05. | Sinh viên sử dụng tóm tắt này làm checklist cá nhân để theo dõi tiến độ, phân chia các nhóm API Endpoint và chuẩn bị tài nguyên chạy test hợp lệ. |
| (1) Prompt \+ Công cụ | (2) Output AI | (3) Verdict | (4) Lý do (ISTQB) | (5) Bản SV sửa |
| :---- | :---- | :---- | :---- | :---- |
| **Tool: Gemini**<br>Thời gian: 23:06 14/08/2026<br>Prompt:<br>"Thực thi theo hướng dẫn trong thư mục `.skills\agent-skill-hw05` để thiết kế kịch bản Performance Testing bằng JMeter XML (.jmx) cho luồng Admin Workflow của SUT EShop..." | Đã tạo kịch bản **Load Testing** (100 VUs, 60s Ramp-up) cho **Admin Workflow** với **JMeter XML**. Tích hợp CSV Data Set Config (`eshop_import_data.csv`), JSON Extractor (cho `token`) và cấu hình Header. Sử dụng Listener **Summary Report** và Assertion (HTTP 200/201) cho 3 endpoint (Auth-heavy, Read-heavy, Transactional).<br/>**Output:** Đã gen ra file `23127212_Load_20260816.jmx` tại `HW05/`. | **INCOMPLETE** | 1. **Lỗi Environment Setup:** AI gán PORT mặc định 8080 thay vì 3000 theo SRS Mục 1.<br/>2. **Lỗi API Contract:** Endpoint login sai (`/api/auth/login` với key `username` thay vì `/api/login` với key `email`), payload thêm sản phẩm dùng `categoryId` chuỗi thay vì `category_id` số theo API Spec Mục 3.3 (ISTQB: Data Type & Specification Inconsistency). | Sinh viên sửa PORT thành 3000, cấu hình lại login endpoint `/api/login` nhận `email/password` chuẩn (`admin@eshop.com` / `Admin123!`), và sửa payload `POST /api/products` thành `"category_id": ${category_id}`. |
| **Tool: Gemini**<br>Thời gian: 23:16 14/08/2026<br>Prompt:<br>"Thực thi theo hướng dẫn trong thư mục `.skills\agent-skill-hw05` để thiết kế kịch bản Performance Testing bằng JMeter XML (.jmx) cho luồng Admin Workflow của SUT EShop..." | Đã tạo kịch bản **Stress Testing** (500 VUs, 120s Ramp-up) cho **Admin Workflow** với **JMeter XML**. Tích hợp CSV Data Set Config (`eshop_import_data.csv`), JSON Extractor (cho `token`) và cấu hình Header. Sử dụng Listener **Aggregate Report** và Assertion (HTTP 200/201) cho 3 endpoint (Auth-heavy, Read-heavy, Transactional).<br/>**Output:** Đã gen ra file `23127212_Stress_20260816.jmx` tại `HW05/`. | **INCOMPLETE** | 1. **Lỗi Environment Setup:** AI gán PORT mặc định 8080 thay vì 3000 theo SRS Mục 1.<br/>2. **Lỗi API Contract:** Endpoint login sai (`/api/auth/login` với key `username` thay vì `/api/login` với key `email`), payload thêm sản phẩm dùng `categoryId` chuỗi thay vì `category_id` số theo API Spec Mục 3.3 (ISTQB: Data Type & Specification Inconsistency). | Sinh viên sửa PORT thành 3000, cấu hình lại login endpoint `/api/login` nhận `email/password` chuẩn (`admin@eshop.com` / `Admin123!`), và sửa payload `POST /api/products` thành `"category_id": ${category_id}`. |
| **Tool: Gemini**<br>Thời gian: 23:22 14/08/2026<br>Prompt:<br>"Thực thi theo hướng dẫn trong thư mục `.skills\agent-skill-hw05` để thiết kế kịch bản Performance Testing bằng JMeter XML (.jmx) cho luồng Admin Workflow của SUT EShop..." | Đã tạo kịch bản **Spike Testing** (1000 VUs, 10s Ramp-up) cho **Admin Workflow** với **JMeter XML**. Tích hợp CSV Data Set Config (`eshop_import_data.csv`), JSON Extractor (cho `token`) và cấu hình Header. Sử dụng Listener **View Results Tree** và Assertion (HTTP 200/201) cho 3 endpoint (Auth-heavy, Read-heavy, Transactional).<br/>**Output:** Đã gen ra file `23127212_Spike_20260816.jmx` tại `HW05/`. | **INCOMPLETE** | 1. **Lỗi Environment Setup:** AI gán PORT mặc định 8080 thay vì 3000 theo SRS Mục 1.<br/>2. **Lỗi API Contract:** Endpoint login sai (`/api/auth/login` với key `username` thay vì `/api/login` với key `email`), payload thêm sản phẩm dùng `categoryId` chuỗi thay vì `category_id` số theo API Spec Mục 3.3 (ISTQB: Data Type & Specification Inconsistency). | Sinh viên sửa PORT thành 3000, cấu hình lại login endpoint `/api/login` nhận `email/password` chuẩn (`admin@eshop.com` / `Admin123!`), và sửa payload `POST /api/products` thành `"category_id": ${category_id}`. |
| **Tool: Gemini**<br>Thời gian: 23:29 16/08/2026<br>Prompt:<br>"Hãy đọc toàn bộ dữ liệu từ 3 file log .jtl đính kèm (Load, Stress, Spike). Phân tích chi tiết: Throughput (RPS), độ trễ trung bình, P90, P95 latency của từng API endpoint, tỷ lệ lỗi Error Rate và tìm ra điểm nghẽn (bottleneck). Đề xuất cho tôi ngưỡng chịu tải (performance thresholds) và các giải pháp tối ưu hệ thống. Output: FIle AI-Analysis.md" | Đã đọc dữ liệu và tính toán các metrics từ 3 file JTL. Phát hiện điểm nghẽn khi gặp tải đột biến (Spike > 150 RPS), tỷ lệ lỗi đạt 3.8% và P95 tăng vọt hàng nghìn mili-giây, đặc biệt tại `POST /api/login`. Đã đề xuất ngưỡng chịu tải bình thường (10-20 RPS) cùng các biện pháp khắc phục như tăng Connection Pool, Caching và Scale Out. Toàn bộ nội dung báo cáo xuất thành file `AI-Analysis.md`. | | | |


## **4\. Tổng kết Độ chính xác AI**

Tổng hợp verdict từ Mục 3 và điền vào bảng dưới.

| Chỉ số | Số lượng | Tỉ lệ |
| :---- | :---- | :---- |
| **Tổng artifact AI sinh đã audit** |  | % |
| **VALID (đúng, dùng nguyên)** |  | % |
| **INVALID (sai; loại bỏ)** |  | % |
| **INCOMPLETE (chấp nhận sau khi sửa)** |  | % |

## **5\. Kết luận — Khi nào nên / không nên dùng AI?**

- **Nên dùng:**
- **Không nên dùng:**

## **6\. Mandatory Disclosure (dán nguyên văn)**

*""*

## **Chữ ký**

| Họ tên sinh viên (in hoa): | NGUYỄN QUANG ĐĂNG KHOA |
| :---- | :---- |
| **MSSV:** | 23127212 |
| **Lớp / Khoá:** | 23KTPM2 |
| **Môn học:** | CS423 / CSC13003 – Kiểm chứng Phần mềm |
| **Giảng viên:** | Lâm Quang Vũ |
| **Ngày:** | 14/08/2026 |
| **Chữ ký:** | Khoa |

## **Tham khảo**

* Kharbach, M. (2026). AI Use Policy Templates for Higher Education. CC BY-NC-SA 4.0.  
* ISTQB Foundation Level Syllabus (latest version).  
* Hardman, P. (2025). A Post-AI Learning Taxonomy.  
* Fuster Rabella, M. (2025). OECD Education Working Paper No. 338\.  
* Perkins, M., Roe, J., & Furze, L. (2025). AI Assessment Scale.  
* Anthropic (2025). Building reliable AI test agents — engineering blog.  
* DeepEval & Promptfoo documentation — testing frameworks for LLM systems.