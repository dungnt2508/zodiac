from pathlib import Path


def print_project_structure(root_dir, exclude_folders=None, exclude_files=None):
    # Đặt giá trị mặc định nếu không có danh sách loại trừ
    if exclude_folders is None:
        exclude_folders = []
    if exclude_files is None:
        exclude_files = []

    root = Path(root_dir)
    # Duyệt tất cả đường dẫn
    for path in sorted(root.rglob('*')):
        # Kiểm tra loại trừ
        relative_path = path.relative_to(root)
        # Bỏ qua nếu path nằm trong danh sách loại trừ
        if any(excluded in relative_path.parts for excluded in exclude_folders):
            continue
        if path.is_file() and path.name in exclude_files:
            continue

        # Tính mức độ thụt đầu dòng
        level = len(relative_path.parts) - 1
        indent = '  ' * level
        suffix = '/' if path.is_dir() else ''
        print(f'{indent}{path.name}{suffix}')


# Đường dẫn đến dự án
project_path = r"C:\Users\pc123\ntdung2508\zodiac_project"

# Danh sách folder và file cần loại trừ
exclude_folders = ['migrations', 'Env3_11', 'useful', 'venv', '__pycache__','.idea'
                    ,'admin','adminlte', 'assets-admin', 'assets-supplier','plugins'
                    , 'vendors', 'fonts','js', 'sass','vendor', 'theme', 'imgs']
exclude_files = ['__init__.py', 'requirements.txt','.gitignore', '.css', '.css.map', '.png', '.svg', '.js', 'ttf', '.woff', '.woff2', '.jpg', '.scss']  # Loại trừ file cụ thể

# Gọi hàm
print_project_structure(project_path, exclude_folders, exclude_files)