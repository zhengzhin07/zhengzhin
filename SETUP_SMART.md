# Zhengzhin Smart System V1 — hướng dẫn triển khai

## Đã tích hợp vào file gốc
- `index.html`: chỉ thêm các thẻ script trước `</body>`; toàn bộ code giao diện/nhạc/IPA Apps gốc được bảo toàn.
- `smart/assistant.js`: chatbot góc phải. Khi chưa cấu hình backend, chatbot báo chưa kết nối chứ KHÔNG giả là AI đang hoạt động.
- `smart/updates.js` + `updates.json`: thông báo cập nhật; sửa nội dung tại `updates.json`.
- `.github/workflows/check-links.yml` và `scripts/`: mỗi ngày kiểm tra 4 link Link4M; báo cáo ở Actions Artifacts và issue khi cần kiểm tra. 403/429/captcha có thể là chặn bot chứ không hẳn link hỏng.
- `worker/`: backend cho chatbot qua Cloudflare Workers AI, KHÔNG triển khai trên GitHub Pages.

## Cài đặt trên GitHub Pages
1. Backup repo hiện tại; giải nén ZIP này rồi đưa nội dung **bên trong thư mục** lên root repo GitHub Pages (giữ `.github` và thư mục nhạc).
2. Bật GitHub Actions và Issues nếu muốn nhận báo cáo link. Vào Actions > Check IPA download links > Run workflow để chạy thử.
3. Mở `updates.json` và chỉnh tiêu đề/nội dung thông báo theo ý muốn.

## Kích hoạt chatbot AI
1. Tạo Cloudflare Worker và bật Workers AI binding tên `AI`, dùng `worker/index.js` và `worker/wrangler.toml` làm ví dụ; chỉnh ALLOWED_ORIGIN nếu đổi domain.
2. Deploy Worker. URL của Worker dạng `https://...workers.dev` (không thêm `/chat`).
3. Trong `index.html` tìm `window.ZHENGZHIN_SMART={apiBase:""}` và điền URL Worker vào `apiBase`.
4. Kiểm tra `GET /health`, sau đó thử gửi câu hỏi. Worker hiện chỉ kiểm tra Origin và không có rate limit đủ mạnh: cần bổ sung Cloudflare WAF/rate limiting và giới hạn chi phí trước khi công khai để tránh người lạ tiêu quota. Origin không phải là xác thực.
5. Không lưu API key hay mật khẩu trong HTML/JS công khai.

## Thống kê
Sử dụng Google Analytics 4: tạo web stream, lấy Measurement ID `G-...`, cài mã GA4 theo hướng dẫn chính thức vào `<head>` cùng banner/cấu hình đồng ý theo quy định áp dụng. Không được tự ý thay `G-...` bằng ID mẫu. Chỉ số là dữ liệu GA4, không phải bộ đếm mọi lượt truy cập tuyệt đối.

## Quản trị
GitHub Pages là static hosting: KHÔNG đặt mật khẩu Admin trong HTML, JS hoặc JSON công khai. Quản lý cập nhật qua GitHub repo có 2FA; xem thống kê trên GA4; xem vấn đề link qua Actions/Issues. Trang Admin có đăng nhập riêng cần backend xác thực, quyền người dùng, lưu dữ liệu (Cloudflare Access/D1 hoặc tương đương), chưa có trong bản V1.

## Kiểm thử
Sau upload: kiểm tra màn hình chào > vào site > nhạc > 4 nút tải > thông báo > chatbot. Không thể đảm bảo dịch vụ Cloudflare/GA4 hoạt động trước khi tài khoản chủ website được kết nối.
