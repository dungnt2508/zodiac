document.addEventListener('DOMContentLoaded', () => {
    const zodiacs = [
        "Tý (Chuột)", "Sửu (Trâu)", "Dần (Hổ)", "Mão (Mèo)",
        "Thìn (Rồng)", "Tỵ (Rắn)", "Ngọ (Ngựa)", "Mùi (Dê)",
        "Thân (Khỉ)", "Dậu (Gà)", "Tuất (Chó)", "Hợi (Lợn)"
    ];

    // Khởi tạo Flatpickr
    const datetimeInput = document.getElementById('datetime');
    flatpickr(datetimeInput, {
        enableTime: true,
        dateFormat: "Y-m-d H:i",
        minDate: "1900-01-01",
        maxDate: "2025-12-31",
        time_24hr: true,
        defaultHour: 12,
        defaultMinute: 0,
        theme: "material_orange",
        onChange: function(selectedDates, dateStr, instance) {
            datetimeInput.value = dateStr;
        }
    });

    // Trang chủ: Tính con giáp và gọi trợ lý ảo
    const exploreBtn = document.getElementById('exploreBtn');
    if (exploreBtn) {
        const userNameInput = document.getElementById('userName');
        const resultDiv = document.getElementById('zodiacResult');
        const aiAssistantDiv = document.getElementById('aiAssistant');

        exploreBtn.addEventListener('click', () => {
            const userName = userNameInput.value.trim();
            const datetimeValue = datetimeInput.value;
            if (!userName || !datetimeValue) {
                resultDiv.textContent = 'Vui lòng nhập tên và chọn ngày giờ!';
                resultDiv.style.color = '#ff6b6b';
                resultDiv.classList.add('pop-up');
                aiAssistantDiv.style.display = 'none';
                return;
            }

            const [datePart, timePart] = datetimeValue.split(' ');
            const [year, month, day] = datePart.split('-').map(Number);
            const [hour, minute] = timePart.split(':').map(Number);

            const maxDays = getMaxDaysInMonth(month, year);
            if (day < 1 || day > maxDays || month < 1 || month > 12 || year < 1900 || year > 2025 ||
                hour < 0 || hour > 23 || minute < 0 || minute > 59) {
                resultDiv.textContent = `Thông tin không hợp lệ! (Tháng ${month} chỉ có tối đa ${maxDays} ngày)`;
                resultDiv.style.color = '#ff6b6b';
                resultDiv.classList.add('pop-up');
                aiAssistantDiv.style.display = 'none';
                return;
            }

            const zodiacIndex = (year - 1900) % 12;
            const zodiac = zodiacs[zodiacIndex];
            resultDiv.textContent = `${userName}, con giáp của bạn là: ${zodiac}`;
            resultDiv.classList.add('pop-up');

            callVirtualAssistant(userName, zodiac, year, month, day, hour, minute);
        });

        function getMaxDaysInMonth(month, year) {
            const daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
            if (month === 2 && isLeapYear(year)) return 29;
            return daysInMonth[month - 1];
        }

        function isLeapYear(year) {
            return (year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0);
        }

        function callVirtualAssistant(userName, zodiac, year, month, day, hour, minute) {
            aiAssistantDiv.style.display = 'block';
            aiAssistantDiv.innerHTML = `
                <p><strong>Trợ lý ảo Grok 3:</strong> Chào ${userName}! Dựa trên thông tin bạn cung cấp (${day}/${month}/${year} ${hour}:${minute}), tôi có một số gợi ý phong thủy:</p>
                <p>- Con giáp: ${zodiac}</p>
                <p>- Hướng tốt: ${getLuckyDirection(zodiac)}</p>
                <p>- Màu sắc may mắn: ${getLuckyColor(zodiac)}</p>
                <p>- Lời khuyên: Hãy giữ tinh thần tích cực và tránh tranh cãi vào giờ ${hour} hôm nay!</p>
                <p>- Thêm thông tin: Đây là một đoạn văn dài để kiểm tra thanh cuộn. Bạn nên chú ý đến các yếu tố phong thủy như hướng nhà, màu sắc quần áo, và thời gian làm việc để tối ưu vận mệnh. Hãy thử thay đổi thói quen hàng ngày để phù hợp với con giáp của bạn. Thêm một chút thông tin nữa để nội dung dài hơn, bạn có thể cuộn để xem toàn bộ nội dung nhé!</p>
                <p>(Lưu ý: Đây là dự đoán mang tính tham khảo. Muốn chi tiết hơn, hãy liên hệ chuyên gia!)</p>
            `;
        }

        function getLuckyDirection(zodiac) {
            const directions = ['Đông', 'Tây', 'Nam', 'Bắc', 'Đông Nam'];
            return directions[Math.floor(Math.random() * directions.length)];
        }

        function getLuckyColor(zodiac) {
            const colors = ['Vàng', 'Đỏ', 'Xanh lá', 'Trắng', 'Đen'];
            return colors[Math.floor(Math.random() * colors.length)];
        }
    }

    // Hamburger Menu Toggle
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');

    if (hamburger && navLinks) {
        hamburger.addEventListener('click', () => {
            hamburger.classList.toggle('active');
            navLinks.classList.toggle('active');
        });

        document.querySelectorAll('.nav-item').forEach(item => {
            item.addEventListener('click', () => {
                hamburger.classList.remove('active');
                navLinks.classList.remove('active');
            });
        });
    }
});