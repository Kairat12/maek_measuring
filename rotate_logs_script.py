#!/usr/bin/env python3
import os
import shutil
import datetime

def rotate_logs(log_path, max_size=50 * 1024 * 1024, backup_count=5):
    if os.path.exists(log_path) and os.path.getsize(log_path) > max_size:
        backup_file = f"{log_path}.{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.bak"
        shutil.move(log_path, backup_file)
        for i in range(backup_count, 0, -1):
            prev_backup = f"{log_path}.{i - 1}.bak"
            new_backup = f"{log_path}.{i}.bak"
            if os.path.exists(prev_backup):
                shutil.move(prev_backup, new_backup)

# Пример использования
log_path = '/home/maek_sklad/logs/gunicorn_access.log'
rotate_logs(log_path)
log_path = '/home/maek_sklad/logs/gunicorn_error.log'
rotate_logs(log_path)