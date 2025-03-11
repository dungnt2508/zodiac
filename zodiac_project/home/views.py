from django.shortcuts import render
from datetime import datetime


def home_page(request):
    """Trang chủ với nội dung hiển thị theo quyền của user"""
    current_year = datetime.now().year
    return render(request, 'home/index-1.html', {'year': current_year})