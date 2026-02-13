import sqlite3
from google_play_scraper import Sort, reviews
import datetime

# Cấu hình
APP_ID = 'com.facebook.katana' # Ví dụ: ID Facebook trên Google Play
DB_NAME = 'google_play_reviews.db'

class ReviewScraper:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.cursor = self.conn.cursor()
        self.init_db()

    def init_db(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS reviews (
                reviewId TEXT PRIMARY KEY,
                userName TEXT,
                content TEXT,
                score INTEGER,
                at DATETIME,
                appVersion TEXT
            )
        ''')
        self.conn.commit()

    def fetch_and_save(self):
        print(f"🔄 Đang cào dữ liệu cho App ID: {APP_ID}...")
        
        # Lấy 50 reviews mới nhất
        result, continuation_token = reviews(
            APP_ID,
            lang='vi', # Ngôn ngữ tiếng Việt
            country='vn',
            sort=Sort.NEWEST,
            count=50
        )

        new_count = 0
        for r in result:
            try:
                self.cursor.execute('''
                    INSERT OR IGNORE INTO reviews (reviewId, userName, content, score, at, appVersion)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (r['reviewId'], r['userName'], r['content'], r['score'], r['at'], r['reviewCreatedVersion']))
                if self.conn.total_changes > 0:
                    new_count += 1
            except Exception as e:
                print(f"⚠️ Lỗi lưu review {r['reviewId']}: {e}")

        self.conn.commit()
        print(f"✅ Hoàn tất! Đã thêm {new_count} reviews mới vào database.")

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    scraper = ReviewScraper()
    scraper.fetch_and_save()
    scraper.close()
