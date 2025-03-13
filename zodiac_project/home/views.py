from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
# from .models import ZodiacSign  # Đảm bảo bạn có model ZodiacSign lưu dữ liệu


def home_page(request):
    """Trang chủ với nội dung hiển thị theo quyền của user"""
    current_year = datetime.now().year
    return render(request, 'home/index-1.html', {'year': current_year})




