paHELP_1 = """🙄**<u>LỆNH QUẢN TRỊ:</u>**

Chỉ cần thêm **c** ở đầu danh sách lệnh để sử dụng cho kênh.

• /pause : Tạm dừng luồng phát hiện tại.
• /resume : Tiếp tục phát luồng đã bị tạm dừng.
• /mute : Tắt tiếng luồng phát hiện tại.
• /unmute : Mở tiếng luồng đang bị tắt.
• /skip : Bỏ qua bài đang phát và bắt đầu phát bài tiếp theo trong danh sách chờ.
• /end hoặc /stop : Xóa danh sách chờ và dừng luồng phát hiện tại.
• /shuffle : Xáo trộn các bài trong danh sách chờ.
• /seek : Tua đến thời điểm đã cho của luồng phát.
• /seekback : Tua ngược lại đến thời điểm đã cho của luồng phát.
• /reboot : Khởi động lại bot cho nhóm của bạn.

🥴<u>**CHẾ ĐỘ LẶP (LOOP PLAY):**</u>

• /loop [disable/enable] hoặc [1-10]  
    : Khi được kích hoạt, bot sẽ lặp lại bài phát hiện tại theo số vòng đã chỉ định (tối đa từ 1 đến 10).

😜<u>**NGƯỜI DÙNG ĐƯỢC XÁC THỰC (AUTH USERS):**</u>

Người dùng xác thực có thể sử dụng các quyền quản trị trong bot mà không cần quyền quản trị ở nhóm.

• /auth [username] : Thêm một người dùng vào danh sách xác thực của bot.
• /unauth [username] : Xóa một người dùng khỏi danh sách xác thực.
• /authusers : Hiển thị danh sách người dùng xác thực của nhóm.
"""

HELP_2 = """💞<u>**LỆNH PHÁT NHẠC:**</u>

Các lệnh có sẵn: play, vplay, cplay

Lệnh bắt buộc (force play): playforce, vplayforce, cplayforce

• **c** tượng trưng cho phát kênh.
• **v** tượng trưng cho phát video.
• **force** tượng trưng cho lệnh phát bắt buộc.

• /play hoặc /vplay hoặc /cplay  : Bắt đầu phát bài theo truy vấn yêu cầu trên videochat.
• /playforce hoặc /vplayforce hoặc /cplayforce : **Phát bắt buộc (force play)** dừng luồng phát đang diễn ra và bắt đầu phát bài yêu cầu.
• /channelplay [username hoặc ID] hoặc [disable] : Kết nối kênh với nhóm và bắt đầu phát bài thông qua lệnh được gửi trong nhóm.

🤨**<u>DANH SÁCH PHÁT TIN TRÊN MÁY CHỦ:</u>**

• /playlist  : Kiểm tra danh sách phát đã lưu trên máy chủ.
• /deleteplaylist : Xóa bất kỳ bài nào đã được lưu trong danh sách phát.
• /play  : Bắt đầu phát bài từ danh sách phát đã lưu trên máy chủ.
"""

HELP_3 = """😉<u>**LỆNH BOT:**</u>

• /stats : Hiển thị top 10 bài phát được, top 10 người dùng, top 10 nhóm trong bot, top 10 bài đã phát trong nhóm và nhiều hơn nữa.
• /sudolist : Hiển thị danh sách người dùng SUDO của bot.
• /lyrics [tên bài] : Tìm kiếm lời bài hát cho bài yêu cầu.
• /song [tên bài] hoặc [link yt] : Tải xuống bài từ YouTube dưới định dạng audio hoặc video.
• /player : Hiển thị bảng điều khiển phát nhạc tương tác.
• /queue : Hiển thị danh sách bài trong hàng chờ.
"""

HELP_4 = """😴<u>**LỆNH BỔ SUNG:**</u>

• /start : Khởi động bot phát nhạc.
• /help  : Hiển thị menu trợ giúp với giải thích các lệnh.
• /ping: Hiển thị thời gian phản hồi (ping) và số liệu hệ thống của bot.

🧐<u>**CÀI ĐẶT NHÓM:**</u>
• /settings : Hiển thị cài đặt nhóm với menu tương tác dạng inline.
"""

HELP_5 = """🥺**<u>THÊM & XÓA NGƯỜI DÙNG SUDO:</u>**
• /addsudo [username hoặc trả lời tin] : Thêm người dùng vào danh sách SUDO.
• /delsudo [username hoặc trả lời tin] : Xóa người dùng khỏi danh sách SUDO.

🥶**<u>HEROKU:</u>**
• /usage : Hiển thị mức sử dụng Dyno của ứng dụng Heroku.

🤯**<u>CÁC THAM SỐ CẤU HÌNH:</u>**
• /get_var : Lấy một biến cấu hình từ file .env.
• /del_var : Xóa một biến cấu hình trên file .env.
• /set_var [tên biến] [giá trị] : Thiết lập hoặc cập nhật một biến cấu hình trên file .env.

🤖**<u>LỆNH BOT:</u>**
• /restart : Khởi động lại bot.
• /update : Cập nhật bot từ kho chứa (upstream repo).
• /speedtest : Kiểm tra tốc độ của máy chủ bot.
• /maintenance [enable/disable] : Chế độ bảo trì
• /logger [enable/disable] : Bot sẽ bắt đầu ghi log các hoạt động của bot.
• /get_log [số dòng] : Lấy log của bot [mặc định 100 dòng].
• /autoend [enable|disable] : Bật/Tắt tự động kết thúc stream nếu không có ai nghe.
"""

HELP_7 = """💌**<u>Ở ĐÂY BẠN CÓ THỂ TÌM ĐƯỢC CÁC TÍNH NĂNG MỚI:</u>**

• /alive : Kiểm tra xem bot Minion Music còn hoạt động hay không.
• /id : Xem ID của người dùng và nhóm.
• /gcast -user -assistant -pin ᴛᴇsᴛɪɴɢ ʙʀᴏᴀᴅᴄᴀsᴛ : Gửi tin broadcast thử.
• /verify : Xác minh bạn trong cơ sở dữ liệu của Minion.
"""

HELP_8 = """💰**<u>TÍNH NĂNG ĐĂNG KÝ PHÁT TIN:</u>**

Bây giờ bạn có thể mua đăng ký phát tin theo tháng và theo tuần từ chúng tôi. Chúng tôi sẽ cung cấp cho bạn 3 lần phát tin mỗi tuần và 14 lần phát tin mỗi tháng, với giới hạn gửi tin sau hai ngày.

**CHỈ DÀNH CHO CHỦ BOT**
• /addweekly [ID người dùng] : Thêm người dùng vào đăng ký phát tin hàng tuần.
• /addmonthly [ID người dùng] : Thêm người dùng vào đăng ký phát tin hàng tháng.
• /removesub [ID người dùng] : Xóa người dùng khỏi đăng ký phát tin.
• /checksubscription [ID người dùng] : Kiểm tra số ngày còn lại và số lần phát tin của người dùng.
• /substats : Xem tổng số đăng ký kèm theo ID và loại đăng ký.
• /subscription_alert : Gửi thông báo cho người dùng đăng ký với số ngày còn lại và số lần phát tin.

**BẤT KỲ AI CŨNG CÓ THỂ SỬ DỤNG**
• /mysubscription : Kiểm tra đăng ký của bạn với số ngày còn lại và số lần phát tin.
• /paidbroadcast : Gửi tin phát tin trả phí đến tất cả người dùng và nhóm khi bạn có đăng ký phát tin đang hoạt động.
"""
