const calculator = require('./script.js');
const assert = require('assert');

console.log("🚀 Đang chạy bộ test cho Máy tính...");

try {
    // Test cộng
    assert.strictEqual(calculator.add(10, 5), 15);
    console.log("✅ Test cộng: Pass");

    // Test chia
    assert.strictEqual(calculator.divide(10, 2), 5);
    console.log("✅ Test chia: Pass");

    // Test chia cho 0 (Trường hợp biên quan trọng)
    try {
        calculator.divide(10, 0);
        console.error("❌ Test chia cho 0: Fail (Không báo lỗi)");
        process.exit(1);
    } catch (e) {
        assert.strictEqual(e.message, "Không thể chia cho 0");
        console.log("✅ Test chia cho 0: Pass (Đã chặn được lỗi)");
    }

    console.log("\n🎊 TẤT CẢ BỘ TEST ĐÃ PASSED! Sẵn sàng Release.");
} catch (err) {
    console.error("❌ Có lỗi xảy ra trong quá trình test:", err.message);
    process.exit(1);
}
