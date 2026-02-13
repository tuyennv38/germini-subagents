import sqlite3
from google_play_scraper import Sort, reviews
import datetime

# Cấu hình mặc định
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

    def fetch_and_save(self, app_id):
        print(f"\n🔄 Đang cào dữ liệu cho App ID: {app_id}...")
        
        try:
            # Lấy 50 reviews mới nhất
            result, continuation_token = reviews(
                app_id,
                lang='vi',
                country='vn',
                sort=Sort.NEWEST,
                count=50
            )
        except Exception as e:
            print(f"❌ Lỗi khi lấy dữ liệu từ Google Play: {e}")
            return False

        new_count = 0
        for r in result:
            try:
                # Dùng .get() để an toàn hơn với các key có thể thiếu
                self.cursor.execute('''
                    INSERT OR IGNORE INTO reviews (reviewId, userName, content, score, at, appVersion)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (r['reviewId'], r['userName'], r['content'], r['score'], r['at'], r.get('reviewCreatedVersion', 'N/A')))
                if self.conn.total_changes > 0:
                    new_count += 1
            except Exception as e:
                print(f"⚠️ Lỗi lưu review {r['reviewId']}: {e}")

        self.conn.commit()
        print(f"✅ Hoàn tất! Đã cập nhật {new_count} reviews mới vào database.")
        return True

    def display_top_5(self):
        print("\n⭐ TOP 5 BÌNH LUẬN MỚI NHẤT:")
        print("="*50)
        self.cursor.execute('''
            SELECT userName, score, content, at 
            FROM reviews 
            ORDER BY at DESC 
            LIMIT 5
        ''')
        rows = self.cursor.fetchall()
        for row in rows:
            print(f"👤 {row[0]} | ⭐ {row[1]}")
            print(f"💬 {row[2][:100]}..." if len(row[2]) > 100 else f"💬 {row[2]}")
            print(f"📅 {row[3]}")
            print("-" * 30)

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    scraper = ReviewScraper()
    
    # Bước 1: Nhập ID App
    app_id_input = input("👉 Nhập ID ứng dụng trên Google Play (VD: com.facebook.katana): ").strip()
    
    if app_id_input:
        # Bước 2: Cào và lưu
        success = scraper.fetch_and_save(app_id_input)
        
        # Bước 3: Hiển thị ngay
        if success:
            scraper.display_top_5()
    else:
        print("❌ Bạn chưa nhập ID ứng dụng.")
        
    scraper.close()
