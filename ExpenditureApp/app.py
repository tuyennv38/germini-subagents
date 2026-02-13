import json
import os

class ExpenseManager:
    def __init__(self, filename='expenses.json'):
        self.filename = filename
        self.expenses = self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []

    def save_data(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.expenses, f, indent=4, ensure_ascii=False)

    def add_expense(self, description, amount):
        expense = {
            "id": len(self.expenses) + 1,
            "description": description,
            "amount": amount
        }
        self.expenses.append(expense)
        self.save_data()
        print(f"✅ Đã thêm: {description} - {amount} VNĐ")

    def show_all(self):
        print("\n--- DANH SÁCH CHI TIÊU ---")
        total = 0
        for e in self.expenses:
            print(f"{e['id']}. {e['description']}: {e['amount']} VNĐ")
            total += e['amount']
        print(f"--------------------------")
        print(f"💰 TỔNG CỘNG: {total} VNĐ\n")

def main():
    manager = ExpenseManager()
    while True:
        print("1. Thêm khoản chi")
        print("2. Xem danh sách")
        print("3. Thoát")
        choice = input("Chọn chức năng: ")
        
        if choice == '1':
            desc = input("Mô tả: ")
            amount = int(input("Số tiền: "))
            manager.add_expense(desc, amount)
        elif choice == '2':
            manager.show_all()
        elif choice == '3':
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
