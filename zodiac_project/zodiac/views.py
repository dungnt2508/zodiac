from django.shortcuts import render
from .models import DailyPrediction
from django.utils import timezone
import random


def zodiac_info(request):
    """trang info 12 con giáp"""
    # Dữ liệu tĩnh (sau này có thể dùng database)
    zodiac_signs = [
        {"name": "Tý (Chuột)", "description": "Thông minh, nhanh nhẹn, thích nghi tốt.", "compatibility": "Thìn, Thân",
         "fortune_2025": "Tài lộc dồi dào."},
        {"name": "Sửu (Trâu)", "description": "Chăm chỉ, kiên nhẫn, đáng tin cậy.", "compatibility": "Tỵ, Dậu",
         "fortune_2025": "Công việc ổn định."},
        {"name": "Dần (Hổ)", "description": "Dũng cảm, tự tin, thích lãnh đạo.", "compatibility": "Ngọ, Tuất",
         "fortune_2025": "Sự nghiệp thăng hoa."},
        {"name": "Mão (Mèo)", "description": "Dịu dàng, tinh tế, yêu hòa bình.", "compatibility": "Mùi, Hợi",
         "fortune_2025": "Gia đạo bình an."},
        {"name": "Thìn (Rồng)", "description": "Quyền lực, sáng tạo, đầy tham vọng.", "compatibility": "Tý, Thân",
         "fortune_2025": "Cơ hội lớn."},
        {"name": "Tỵ (Rắn)", "description": "Bí ẩn, thông thái, quyến rũ.", "compatibility": "Sửu, Dậu",
         "fortune_2025": "Đột phá lớn."},
        {"name": "Ngọ (Ngựa)", "description": "Tự do, năng động, yêu khám phá.", "compatibility": "Dần, Tuất",
         "fortune_2025": "Sự nghiệp thăng tiến."},
        {"name": "Mùi (Dê)", "description": "Hiền lành, nghệ thuật, yêu thiên nhiên.", "compatibility": "Mão, Hợi",
         "fortune_2025": "Gia đạo hạnh phúc."},
        {"name": "Thân (Khỉ)", "description": "Linh hoạt, thông minh, hài hước.", "compatibility": "Tý, Thìn",
         "fortune_2025": "Cẩn trọng đầu tư."},
        {"name": "Dậu (Gà)", "description": "Cần cù, tổ chức tốt, yêu cái đẹp.", "compatibility": "Sửu, Tỵ",
         "fortune_2025": "Công việc thuận lợi."},
        {"name": "Tuất (Chó)", "description": "Trung thành, chính trực, bảo vệ.", "compatibility": "Dần, Ngọ",
         "fortune_2025": "Tài lộc tăng."},
        {"name": "Hợi (Lợn)", "description": "Chân thành, rộng lượng, yêu đời.", "compatibility": "Mão, Mùi",
         "fortune_2025": "Năm bình yên."},
    ]
    return render(request, 'zodiac/zodiac_signs.html', {'zodiac_signs': zodiac_signs})


def zodiac_predict(request):
    """trang dự đoán"""
    today = timezone.now().date()
    daily_predictions = DailyPrediction.objects.filter(date=today)

    if not daily_predictions.exists():
        # Tạo dự đoán ngẫu nhiên nếu chưa có (tạm thời)
        zodiacs = ["Tý (Chuột)", "Sửu (Trâu)", "Dần (Hổ)", "Mão (Mèo)", "Thìn (Rồng)", "Tỵ (Rắn)",
                   "Ngọ (Ngựa)", "Mùi (Dê)", "Thân (Khỉ)", "Dậu (Gà)", "Tuất (Chó)", "Hợi (Lợn)"]
        fortunes = {
            "Tý (Chuột)": "Tài lộc dồi dào, nhưng cẩn thận chi tiêu.",
            "Sửu (Trâu)": "Công việc ổn định, sức khỏe cần chú ý.",
            # Thêm các con giáp khác tương tự
        }
        for zodiac in zodiacs:
            DailyPrediction.objects.create(zodiac=zodiac, date=today, fortune=fortunes.get(zodiac, "Chưa có dự đoán."))

    daily_predictions = DailyPrediction.objects.filter(date=today)
    context = {'daily_predictions': daily_predictions}
    return render(request, 'zodiac/fortune_telling.html', context)