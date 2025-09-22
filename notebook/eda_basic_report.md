---

```markdown
# Báo cáo khám phá dữ liệu (EDA) - Calendar Dataset

## 1. Cấu trúc dữ liệu

Các cột chính trong tập dữ liệu:

- `date`: Ngày diễn ra sự kiện
- `year`: Năm
- `month`: Tháng
- `wday`: Ngày trong tuần
- `event_name`: Tên sự kiện
- `event_type`: Loại sự kiện

## 2. Thống kê mô tả

- Số dòng: **10,000**
- Số cột: **6**
- Các loại sự kiện: Cultural, National, Religious, Sporting

Ví dụ thống kê loại sự kiện:

| event_type | unique_events | total_occurrences |
| ---------- | ------------- | ----------------- |
| Cultural   | 7             | 41                |
| National   | 10            | 52                |
| Religious  | 10            | 56                |
| Sporting   | 3             | 18                |

## 3. Các phát hiện chính

- các dữ liệu trong bộ dữ liệu đã đưa về dạng chuẩn
- không phát hiện dữ liệu trùng lặp, ngoại lai, thiếu, bất thường
```
