from django.db import models
from django.contrib.auth.models import User

class DailyPrediction(models.Model):
    zodiac = models.CharField(max_length=50)  # Tên con giáp
    date = models.DateField()  # Ngày dự đoán
    fortune = models.TextField()  # Nội dung dự đoán
    created_at = models.DateTimeField(auto_now_add=True)


class ZodiacSign(models.Model):
    """
        code: Mã duy nhất cho mỗi con giáp.
        name: Tên con giáp.
        name_vn : Tên con giáp tiếng việt
        description: Mô tả chung.
        compatibility: Mức độ hợp với con giáp khác.
        fortune_2025: Vận mệnh trong năm 2025.
        luckyofday: Ngày may mắn.
        usercreated & userupdated: Người tạo & cập nhật.
        timecreated & timeupdated: Thời gian tạo & cập nhật.
    """
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=30)
    name_vn = models.CharField(max_length=30, null=True, blank = True)
    description = models.TextField()
    compatibility = models.CharField(max_length=100)
    fortune_2025 = models.TextField()
    fortune_today = models.TextField(null=True, blank = True)
    luckyofday = models.CharField(max_length=2, null=True, blank=True)
    position = models.CharField(max_length=2)

    usercreated = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name="zodiac_created")
    timecreated = models.DateTimeField(auto_now_add=True)
    userupdated = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name="zodiac_updated")
    timeupdated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-timecreated"]  # Sắp xếp theo thời gian tạo mới nhất

    def __str__(self):
        return self.name

    def __str__(self):
        return f"{self.zodiac} - {self.date}"