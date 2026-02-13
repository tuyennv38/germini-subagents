// Logic tính toán (Core)
const calculator = {
    add: (a, b) => a + b,
    subtract: (a, b) => a - b,
    multiply: (a, b) => a * b,
    divide: (a, b) => {
        if (b === 0) throw new Error("Không thể chia cho 0");
        return a / b;
    }
};

// Điều phối UI
function handleCalc(op) {
    const n1 = parseFloat(document.getElementById('num1').value);
    const n2 = parseFloat(document.getElementById('num2').value);
    const resultSpan = document.getElementById('result');
    const resultBox = document.getElementById('result-box');

    try {
        if (isNaN(n1) || isNaN(n2)) {
            throw new Error("Bạn hãy nhập đủ 2 số");
        }

        let res;
        switch (op) {
            case '+': res = calculator.add(n1, n2); break;
            case '-': res = calculator.subtract(n1, n2); break;
            case '*': res = calculator.multiply(n1, n2); break;
            case '/': res = calculator.divide(n1, n2); break;
        }

        resultSpan.innerText = res;
        resultBox.classList.remove('error');
    } catch (err) {
        resultSpan.innerText = err.message;
        resultBox.classList.add('error');
    }
}

// Export cho QA nếu dùng Node.js test
if (typeof module !== 'undefined') {
    module.exports = calculator;
}
