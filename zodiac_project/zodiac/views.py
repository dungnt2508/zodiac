from django.shortcuts import render
from .models import DailyPrediction
from django.utils import timezone
import random
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import ZodiacSign  # Đảm bảo bạn có model ZodiacSign lưu dữ liệu


def zodiac_info(request):
    """lấy thông tin 12 con giáp mới nhất hằng ngày"""
    # Dữ liệu tĩnh (sau này có thể dùng database)
    zodiac_signs = ZodiacSign.objects.all()[:12]  # Lấy 12 record mới nhất
    return render(request, 'zodiac/zodiac_signs.html', {'zodiac_signs': zodiac_signs})


def latest_lucky_zodiac(request):
    zodiac = ZodiacSign.objects.filter(luckyofday="1").order_by("-timecreated").first()  # Lấy record mới nhất

    if not zodiac:
        return JsonResponse({"error": "Không tìm thấy con giáp may mắn."}, status=404)

    return JsonResponse({
        "id": zodiac.id,
        "code": zodiac.code,
        "name": zodiac.name,
        "name_vn": zodiac.name_vn,
        "description": zodiac.description,
        "compatibility": zodiac.compatibility,
        "fortune_2025": zodiac.fortune_2025,
        "fortune_today": zodiac.fortune_today,
        "luckyofday": zodiac.luckyofday,
        "timecreated": zodiac.timecreated.strftime("%Y-%m-%d %H:%M:%S"),
    })

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